
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns

print("All libraries imported successfully!")

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Seaborn version:", sns.__version__)

# Test Pandas
df = pd.DataFrame({
    "Name": ["Shyam", "Rahul"],
    "Marks": [85, 90]
})

print("\nPandas Test:")
print(df)

# Test NumPy
arr = np.array([10, 20, 30])
print("\nNumPy Test:", arr)

print("\nEverything is working perfectly!")
