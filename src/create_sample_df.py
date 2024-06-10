import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# fix seed
np.random.seed(42)

# time axis
n_points = 1000
t = np.linspace(0, 4 * np.pi, n_points)  # 4pi

# Sin wave Cos wave
sin_wave = np.sin(t)
cos_wave = np.cos(t)

# add randum noise
noise_lebel = 0.2
sin_wave_noise_added = sin_wave + np.random.randn(n_points)
cos_wave_noise_added = cos_wave + np.random.randn(n_points)

# Create Dataframe
date_range = pd.date_range(start="2024-1-1", periods=n_points, freq="D")

df = pd.DataFrame(
    {
        "Datetime": date_range,
        "sin_wave": sin_wave_noise_added,
        "cos_wave": cos_wave_noise_added,
    },
    index=date_range,
)
print(df.shape)
# (1000, 3)
print(df.head())
# df

# Save csv file
os.makedirs("./data/dst/", exist_ok=True)
df.to_csv("data/dst/sample_wave.csv")

# plot, save png
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
df.plot(ax=ax)
fig.savefig("data/dst/sample_wave.png")
