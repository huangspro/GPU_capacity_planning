from src.dataset.dataset import Dataset


new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/request_count.csv"
)

t_r = new_dataset.get_column("text_requests")
i_r = new_dataset.get_column("image_requests")

print("lambda_t = ", sum(t_r)/len(t_r))
print("lambda_i = ", sum(i_r)/len(i_r))