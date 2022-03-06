import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('./data/name_gender_dataset.csv')

dataset.describe()

print(1)