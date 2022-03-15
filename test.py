import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


print(pd.__version__)
print(sns.__version__)


df = sns.load_dataset("mpg")

df.head()
df.tail()
print(df.info())
