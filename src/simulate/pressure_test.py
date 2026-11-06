from math import sqrt

from pyarrow import duration

from src.dataset.dataset import Dataset
import numpy as np

new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/request_count.csv"
)

gpu_number = 9
gpu_capacity = gpu_number * 48
expe_time = 500000

text_ave_count = 45.45133928571428
image_ave_count = 3.638938492063492
text_count_deviation = 961.1112359
image_count_deviation = 11.21283594


text_ave_time = 0.762147
image_ave_time = 7.476124
text_time_deviation = 0.628502
image_time_deviation = 6.247750

text_data = new_dataset.get_column("text_requests")
image_data = new_dataset.get_column("image_requests")

test_failed_count = 0


for i in range(expe_time):
    text = (
        np.random.normal(text_ave_count, sqrt(text_count_deviation), 1)[0]
        * np.random.normal(text_ave_time, sqrt(text_time_deviation), 1)[0]
    )
    image = (
        np.random.normal(image_ave_count, sqrt(image_count_deviation), 1)[0]
        * np.random.normal(image_ave_count, sqrt(image_time_deviation), 1)[0]
    )
    duration = text + image

    if i % 100 == 0:
        print(text, image, duration)

    if duration > gpu_capacity:
        test_failed_count += 1

print(test_failed_count)
print(test_failed_count / expe_time)
