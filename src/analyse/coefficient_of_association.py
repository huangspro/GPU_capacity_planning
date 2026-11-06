"""
计算 NT 与 NI 的相关系数，判断两类请求是否可能受到共同流量冲击，即大量多模
态请求的冲击。
"""

from src.dataset.dataset import Dataset

new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/request_count.csv"
)

t_r = new_dataset.get_column("text_requests")
i_r = new_dataset.get_column("image_requests")


def correlation(X, Y):
    n = len(X)

    mean_x = sum(X) / n
    mean_y = sum(Y) / n

    numerator = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))

    denominator = (
        sum((x - mean_x) ** 2 for x in X) * sum((y - mean_y) ** 2 for y in Y)
    ) ** 0.5

    return numerator / denominator


print("Correlation:", correlation(t_r, i_r))
