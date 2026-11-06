"""
利用冷启动数据，估计冷启动概率及冷启动前后的平均处理时间；使用全概率公式解
释冷启动对总体均值和右尾的贡献
"""

from src.dataset.dataset import Dataset

new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/service_time.csv"
)

text_hot = new_dataset.get_col_by_other_head(
    {"cold_start": 0, "request_type": "text"}, "gpu_seconds"
)
text_cold = new_dataset.get_col_by_other_head(
    {"cold_start": 1, "request_type": "text"}, "gpu_seconds"
)

image_hot = new_dataset.get_col_by_other_head(
    {"cold_start": 0, "request_type": "image"}, "gpu_seconds"
)
image_cold = new_dataset.get_col_by_other_head(
    {"cold_start": 1, "request_type": "image"}, "gpu_seconds"
)


ave_text_hot = sum(text_hot) / len(text_hot)
ave_text_cold = sum(text_cold) / len(text_cold)
ave_image_hot = sum(image_hot) / len(image_hot)
ave_image_cold = sum(image_cold) / len(image_cold)

print("ave_text_hot: ", ave_text_hot)
print("ave_text_cold: ", ave_text_cold)
print("ave_image_hot: ", ave_image_hot)
print("ave_image_cold: ", ave_image_cold)
