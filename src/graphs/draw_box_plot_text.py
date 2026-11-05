"""
绘制不同时段的两种请求数量的箱线图
"""

import matplotlib.pyplot as plt
from src.dataset.dataset import Dataset

new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/request_count.csv"
)

periods = ["night", "morning", "daytime", "peak", "late"]

data = [
    new_dataset.get_period(period, "text_requests)
    for period in periods
]

plt.figure(figsize=(10, 6))

plt.boxplot(
    data,
    tick_labels=periods,
    patch_artist=True
)

plt.ylabel("total_requests")
plt.xlabel("Period")
plt.title("Request Count Distribution by Period")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()