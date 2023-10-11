import numpy as np
import pandas as pd
from scipy import stats


def main():
    df = pd.read_csv()
    df = df.dropna()

    sample = df.sample(n=50, replace=True, random_state=5)

    mean = sample['column'].mean()
    standard_error = sample['column'].std() / np.sqrt(sample.shape[0])

    stats.norm.interval(alpha=.95, loc=mean, scale=standard_error)
