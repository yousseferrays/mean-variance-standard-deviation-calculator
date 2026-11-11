# mean-variance-standard-deviation-calculator
# Mean-Variance-Standard-Deviation Calculator

## Description
A Python calculator built using NumPy that calculates statistical measures from a list of nine numbers arranged into a 3×3 matrix.

## Features
- Mean
- Variance
- Standard deviation
- Maximum
- Minimum
- Sum

Each statistic is calculated across columns, rows, and the entire matrix.

## Technologies
- Python
- NumPy

## Usage

```python
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```

## Input validation
The function raises a `ValueError` if the input does not contain exactly nine numbers.
