"""
对工作日高峰的 NT 和 NI 分别建立泊松分布模型，参数分别为 λT 和 λI 。估计参数
λT 和 λI 并给出 95% 置信区间。
"""

from math import sqrt

from src.dataset.dataset import Dataset

new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/request_count.csv"
)

t_r = new_dataset.get_column("text_requests")
i_r = new_dataset.get_column("image_requests")

ave_t_r = sum(t_r) / len(t_r)
ave_i_r = sum(i_r) / len(i_r)

print("lambda_text = ", ave_t_r)
print("lambda_image = ", ave_i_r)

t_r_left = ave_t_r - 1.96 * sqrt(ave_t_r / len(t_r))
t_r_right = ave_t_r + 1.96 * sqrt(ave_t_r / len(t_r))

i_r_left = ave_i_r - 1.96 * sqrt(ave_i_r / len(i_r))
i_r_right = ave_i_r + 1.96 * sqrt(ave_i_r / len(i_r))

print(f"confident interval of text = [{t_r_left}, {t_r_right}]")
print(f"confident interval of image = [{i_r_left}, {i_r_right}]")
