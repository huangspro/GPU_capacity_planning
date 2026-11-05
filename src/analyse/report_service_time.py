"""
分别研究文本请求与图像请求的 GPU 处理时间：报告样本量、均值、标准差、中位
数、95% 与 99% 分位数，并画出直方图
"""

import pandas as pd
import matplotlib.pyplot as plt

from src.dataset.dataset import Dataset

new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/service_time.csv"
)

text = new_dataset.get_request_type("text", "gpu_seconds")
image = new_dataset.get_request_type("image", "gpu_seconds")


def calculate_statistics(data, name):
    # Convert to numerical data and remove missing values
    data = pd.to_numeric(pd.Series(data), errors="coerce").dropna()

    stats = {
        "Request Type": name,
        "Sample Size": data.count(),
        "Mean": data.mean(),
        "Standard Deviation": data.std(ddof=1),
        "Median": data.median(),
        "95% Quantile": data.quantile(0.95),
        "99% Quantile": data.quantile(0.99),
    }

    return stats


# Calculate statistics
results = pd.DataFrame([
    calculate_statistics(text, "Text"),
    calculate_statistics(image, "Image"),
])

print(results.to_string(index=False))


# Convert to numerical data and remove missing values
text = pd.to_numeric(pd.Series(text), errors="coerce").dropna()
image = pd.to_numeric(pd.Series(image), errors="coerce").dropna()


# Plot histograms
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

datasets = [
    (text, "Text Requests"),
    (image, "Image Requests")
]

for ax, (data, title) in zip(axes, datasets):

    # Histogram
    ax.hist(
        data,
        bins=50,
        density=True,
        alpha=0.7,
        edgecolor="black"
    )

    # Mean
    ax.axvline(
        data.mean(),
        linestyle="--",
        linewidth=2,
        label=f"Mean = {data.mean():.4f}"
    )

    # Median
    ax.axvline(
        data.median(),
        linestyle=":",
        linewidth=2,
        label=f"Median = {data.median():.4f}"
    )

    ax.set_title(title, fontsize=14)
    ax.set_xlabel("GPU Service Time (seconds)")
    ax.set_ylabel("Probability Density")
    ax.legend()
    ax.grid(alpha=0.3)

plt.tight_layout()

# Display figure only, without saving
plt.show()
