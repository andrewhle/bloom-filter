import math
import mmh3
from bitarray import bitarray 

ACCEPTANCE_FALSE_PROPABILITY = 0.01 # Chance of false positive probability = 1%


######### SOURCE: REFERENCE FROM https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/

class BloomFilter(object):

    def __init__ (self, words_count):

        self.false_positive_prob = ACCEPTANCE_FALSE_PROPABILITY
        self.size = self.get_filter_size(words_count)
        self.hash_count = self.get_hash_count(self.size, words_count)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def get_filter_size(self, words_count):
        p = self.false_positive_prob
        n = words_count
        return int(-(n * math.log(p))/(math.log(2)**2))
    
    def add(self, word):
        for i in range(self.hash_count):
            digest = mmh3.hash(word, i) % self.size
            self.bit_array[digest] = True

    def get_hash_count(self, filter_size, words_count):
        return int((filter_size/words_count) * math.log(2))
    
    def is_member(self, word):
        for i in range(self.hash_count):
            digest = mmh3.hash(word, i) % self.size
            if not self.bit_array[digest]:  # If any bit is False, it's not in the set
                return False
        return True
    
############################################################################################
################################# MAIN HELPER FUNCTION #####################################
############################################################################################

def read_file(file_path, encoding):
    words = []  # Use a list to store all words
    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            word = line.strip()  # Processing the line by stripping whitespace
            if word:  # Only add non-empty strings
                words.append(word)
    return words

def calculate_statistics(rockyou, dictionary, bloom_filter):
    TP = FN = FP = TN = 0
    rockyou_set = set(rockyou)  # Using a set for O(1) complexity checks

    total_tests = len(dictionary)

    # Count statistics from query rockyou into dictionary
    for word in dictionary:
        in_rockyou = word in rockyou_set
        in_bloom = bloom_filter.is_member(word)

        if in_bloom and in_rockyou:
            TP += 1
        elif not in_bloom and not in_rockyou:
            TN += 1
        elif in_bloom and not in_rockyou:
            FP += 1
        elif not in_bloom and in_rockyou:
            FN += 1  # This should be rare and expected to be 0

    # Calculate percentage
    if total_tests > 0:
        TP_percent = (TP / total_tests) * 100
        TN_percent = (TN / total_tests) * 100
        FP_percent = (FP / total_tests) * 100
        FN_percent = (FN / total_tests) * 100
    else:
        TP_percent = 0
        TN_percent = 0
        FP_percent = 0
        FN_percent = 0


    return {
        "TP": TP, "TP%": TP_percent,
        "TN": TN, "TN%": TN_percent,
        "FP": FP, "FP%": FP_percent,
        "FN": FN, "FN%": FN_percent
    }

if __name__ == "__main__":

    rockyou = read_file("rockyou.ISO-8859-1.txt", "ISO-8859-1")
    dictionary = read_file("dictionary.txt", "ISO-8859-1")

    words_count = len(rockyou)

    bloom_filter = BloomFilter(words_count)
    for word in rockyou:
        bloom_filter.add(word)

    print("Size of bloom filter array", bloom_filter.size)

    stats = calculate_statistics(rockyou, dictionary, bloom_filter)

    print(f"True Positives: {stats['TP']} or {stats['TP%']:.2f}%")
    print(f"True Negatives: {stats['TN']} or {stats['TN%']:.2f}%")
    print(f"False Positives: {stats['FP']} or {stats['FP%']:.2f}%")
    print(f"False Negatives: {stats['FN']} or {stats['FN%']:.2f}%")