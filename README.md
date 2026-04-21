# Probability and Statistics

A sequentially structured series of Jupyter Notebooks exploring probability theory and statistical analysis in Python. The notebooks build progressively from foundational concepts — data types, variable classification, and measures of dispersion — through to discrete and continuous probability distributions, with an applied project implementing a Naive Bayes spam classifier from first principles.

---

## Table of Contents

- [Overview](#overview)
- [Notebooks](#notebooks)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Topics Covered](#topics-covered)
- [Dependencies](#dependencies)
- [Author](#author)

---

## Overview

This repository is a self-directed study log covering the core curriculum of an introductory probability and statistics course, implemented entirely in Python. Each notebook is a self-contained lesson combining written explanation, code, and output in a single document. The notebooks are numbered to indicate the intended reading order.

The applied highlight of the series is notebook 05, which uses Bayes' theorem to build a working spam detection classifier — a concrete demonstration of how probabilistic reasoning translates into a real machine learning technique.

---

## Notebooks

| # | File | Description |
|---|------|-------------|
| 01 | [01datatypes.ipynb](01datatypes.ipynb) | Statistical data types: nominal, ordinal, interval, and ratio scales |
| 02 | [02-variables-.ipynb](02-variables-.ipynb) | Variable classification: discrete, continuous, dependent, and independent |
| 03 | [03-dispersion.ipynb](03-dispersion.ipynb) | Measures of spread: range, variance, standard deviation, and IQR |
| 04 | [04-coin-flips.ipynb](04-coin-flips.ipynb) | Classical probability and the law of large numbers via coin flip simulation |
| 05 | [05-spam-detection.ipynb](05-spam-detection.ipynb) | Bayes' theorem applied: building a Naive Bayes spam classifier from scratch |
| 06 | [06-distribution.ipynb](06-distribution.ipynb) | Discrete distributions: Binomial, Poisson, and Geometric |
| 07 | [07-Continuous-Distributions.ipynb](07-Continuous-Distributions.ipynb) | Continuous distributions: Normal, Uniform, and Exponential |

---

## Project Structure

```
Probability-and-Statistics/
│
├── 01datatypes.ipynb
├── 02-variables-.ipynb
├── 03-dispersion.ipynb
├── 04-coin-flips.ipynb
├── 05-spam-detection.ipynb
├── 06-distribution.ipynb
├── 07-Continuous-Distributions.ipynb
│
├── Python/                     # Supplementary Python scripts
├── assets/                     # Images and plots referenced in the notebooks
│
└── README.md
```

---

## Getting Started

**Prerequisites:** Python 3.7 or higher, with Jupyter Notebook or JupyterLab installed.

```bash
git clone https://github.com/KA6-p/Probability-and-Statistics.git
cd Probability-and-Statistics
pip install numpy pandas matplotlib scipy jupyter
jupyter notebook
```

Open any `.ipynb` file from the Jupyter interface. Notebooks are independent but are best read in numerical order if you are new to the subject.

---

## Topics Covered

### Descriptive Statistics

- The four scales of measurement (nominal, ordinal, interval, ratio) and why the distinction matters for choosing statistical methods
- Discrete versus continuous variables; dependent versus independent variables
- Measures of central tendency and spread: mean, median, range, variance, standard deviation, and interquartile range
- Visualising distributions with histograms and box plots

### Probability Theory

- Sample spaces, events, and the definition of probability
- Simulating coin flips with `numpy.random` to demonstrate the law of large numbers empirically
- Conditional probability and Bayes' theorem: `P(A|B) = P(B|A) * P(A) / P(B)`

### Applied Bayes — Spam Classifier (Notebook 05)

- Representing a labelled email dataset as a frequency table
- Computing prior probabilities for spam and ham classes
- Computing likelihoods for individual words given each class
- Classifying unseen messages by selecting the class with the higher posterior probability
- Understanding the "naive" independence assumption and when it holds in practice

### Discrete Probability Distributions (Notebook 06)

- **Binomial** — modelling the number of successes in a fixed number of independent Bernoulli trials
- **Poisson** — modelling event counts over a fixed interval when events occur independently at a constant rate
- **Geometric** — modelling the number of trials needed to achieve the first success

### Continuous Probability Distributions (Notebook 07)

- **Normal (Gaussian)** — the bell curve; the central limit theorem; z-scores and standardisation
- **Uniform** — equal probability across a bounded interval
- **Exponential** — modelling time between independent events in a Poisson process

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `numpy` | Numerical computation, random simulation |
| `pandas` | Data manipulation and frequency tables |
| `matplotlib` | Plotting distributions and simulation results |
| `scipy` | Probability density and cumulative distribution functions |
| `jupyter` | Interactive notebook environment |

Install all dependencies with:

```bash
pip install numpy pandas matplotlib scipy jupyter
```

---

## Author

**KA6-p** — [github.com/KA6-p](https://github.com/KA6-p)
