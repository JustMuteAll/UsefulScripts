import numpy as np

def train_val_test_split(n):
    train = np.sort(np.random.choice(n, size=int(0.8*n), replace=False))
    left = np.setdiff1d(np.arange(n), train)
    val = np.sort(np.random.choice(left, size=int(0.5*len(left)), replace=False))
    test = np.setdiff1d(left, val)
    return train, val, test