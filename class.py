from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter,hilbert,filtfilt
from scipy.stats import kurtosis


DATA_DIR = Path("C:/Users/sakth/Downloads/files/dataset/IMS/IMS/2nd_test/2nd_test")
FS = 20000

files = sorted(DATA_DIR.iterdir())

print(f"number of files: {len(files)}")
print(f"1st file: {files[0].name}")
print(f"last file: {files[-1].name}")

one = np.loadtxt(files[0])

print(f"shape of one file: {one.shape}")
