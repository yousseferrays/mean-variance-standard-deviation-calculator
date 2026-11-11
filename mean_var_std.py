import numpy as np

def calculate(numbers):
    if len(numbers) != 9: 
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(numbers).reshape(3,3)

    vertical_mean = matrix.mean(axis=0).tolist()
    horizontal_mean = matrix.mean(axis=1).tolist()
    total_mean = matrix.mean().item()
    mean = [vertical_mean, horizontal_mean, total_mean]

    vertical_variance = matrix.var(axis=0).tolist()
    horizontal_variance = matrix.var(axis=1).tolist()
    total_variance = matrix.var().item()
    variance = [vertical_variance, horizontal_variance, total_variance]
    
    vertical_std = matrix.std(axis=0).tolist()
    horizontal_std = matrix.std(axis=1).tolist()
    total_std = matrix.std().item()
    standard_deviation = [vertical_std, horizontal_std, total_std]

    vertical_max = matrix.max(axis=0).tolist()
    horizontal_max = matrix.max(axis=1).tolist()
    total_max = matrix.max().item()
    maximum = [vertical_max, horizontal_max, total_max]

    vertical_min = matrix.min(axis=0).tolist()
    horizontal_min = matrix.min(axis=1).tolist()
    total_min = matrix.min().item()
    minimum = [vertical_min, horizontal_min, total_min]

    vertical_sum = matrix.sum(axis=0).tolist()
    horizontal_sum = matrix.sum(axis=1).tolist()
    total_sum = matrix.sum().item()
    summation = [vertical_sum, horizontal_sum, total_sum]
    
    calculations = {'mean' : mean, 'variance' : variance, 'standard deviation' : standard_deviation, 'max' : maximum, 'min' : minimum, 'sum' : summation} 
    return calculations
