# Bloom Filter Implementation

This repository contains a Python implementation of a Bloom filter. The project is designed to efficiently check whether an element is present in a set by using a probabilistic data structure. This implementation uses two files, `rockyou.txt` for loading initial values into the Bloom filter, and `dictionary.txt` for testing these values.

## Project Overview

The Bloom filter is loaded with values from `rockyou.txt`. It then automates the testing of values in `dictionary.txt`, determining if each word is likely present in the `rockyou.txt`. The primary focus is on evaluating the effectiveness of the Bloom filter in distinguishing between words that are present or not in the dictionary. 

## Features

- **Load Data**: Loads data from `rockyou.txt` to populate the Bloom filter.
- **Automate Testing**: Automatically tests all values from `dictionary.txt`.
- **Statistics Calculation**: Calculates and displays statistics on true positive, true negative, false positive, and false negative rates for the values tested against the `rockyou.txt` data set.

## Usage

To run this Bloom filter implementation, simply execute the `main.py` script in your Python environment:
```bash
python main.py
```

## Statistics Explained
The software calculates and displays the following statistics to measure the accuracy of the Bloom filter:

True Positive (TP): Correctly identified as present in the Bloom filter. These are words that are in both rockyou.txt and dictionary.txt.
True Negative (TN): Correctly identified as not present in the Bloom filter. These are words that are in neither file.
False Positive (FP): Incorrectly identified as present in the Bloom filter. These are words that are in dictionary.txt but not in rockyou.txt.
False Negative (FN): Incorrectly identified as not present in the Bloom filter. These are words that are in rockyou.txt but were not detected.

## Important Note
Please be aware that the rockyou.txt file is large and can impact the performance and memory usage of your system. The file can be download here

https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt
