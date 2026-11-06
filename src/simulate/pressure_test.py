from math import sqrt

from pyarrow import duration

from src.dataset.dataset import Dataset
import numpy as np

new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/request_count.csv"
)

gpu_number = 2
gpu_capacity = gpu_number * 48
expe_time = 5000000

text_ave_count = 45.45133928571428
image_ave_count = 3.638938492063492
text_count_deviation = 961.1112359
image_count_deviation = 11.21283594


text_ave_time = 0.762147
image_ave_time = 7.476124
text_time_deviation = 0.628502
image_time_deviation = 6.247750

E_W = text_ave_count * text_ave_time + image_ave_count * image_ave_time
D_W = text_ave_count * text_time_deviation + image_ave_count * image_time_deviation

test_failed_count = 0


tem = 0
for i in range(expe_time):
    duration = np.random.normal(E_W, sqrt(D_W), 1)[0]
    tem += duration
    if i % 800000 == 0:
        print(duration)

    if duration > gpu_capacity:
        test_failed_count += 1

print(test_failed_count)
print(test_failed_count / expe_time)
print(tem / expe_time)
