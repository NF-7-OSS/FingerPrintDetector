
# Fingerprint Matching Using SIFT and FLANN

This project demonstrates fingerprint matching using the SIFT (Scale-Invariant Feature Transform) algorithm and FLANN (Fast Library for Approximate Nearest Neighbors) matcher. The goal is to find the best match for an altered fingerprint from a set of real fingerprints.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Fingerprint matching is a crucial task in biometric authentication systems. This project uses the SIFT algorithm to detect keypoints and compute descriptors in the fingerprints, and the FLANN matcher to find the closest matching fingerprints in a dataset. The program identifies the best match by comparing keypoints between a sample (altered) fingerprint and real fingerprints from the dataset.

## Installation

To run this project, you need to have Python and the required libraries installed. Follow the steps below:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/fingerprint-matching.git
    cd fingerprint-matching
    ```

2. **Install dependencies:**

    You can install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure that your `requirements.txt` includes the necessary dependencies such as OpenCV.

    Example of `requirements.txt`:
    ```plaintext
    opencv-python
    numpy
    ```

## Usage

To use the fingerprint matching script, follow these steps:

1. Place the sample fingerprint you want to match in the `SOCO_FINGERS/Altered_1/Altered-Hard_1/` directory.

2. Place the real fingerprints in the `SOCO_FINGERS/Real/` directory.

3. Run the script:

    ```bash
    python fingerprint_matching.py
    ```

    The script will print out the filename of the best-matched fingerprint along with the match score. It will also display the matched keypoints between the sample and the matched fingerprint.

## Results

After running the script, you'll see the best match found in the dataset displayed on your screen. The output includes:

- **Best Match:** The filename of the best-matched fingerprint.
- **Score:** The percentage match between the sample and the best-matched fingerprint.

Example Output:
