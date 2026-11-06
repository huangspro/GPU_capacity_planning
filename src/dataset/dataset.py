import pandas as pd


class Dataset:
    def __init__(self, path: str):
        self.path = path
        self.data = None
        self.load()

    def load(self):
        self.data = pd.read_csv(self.path)

    # 获取某一列，返回 list
    def get_column(self, field_name: str) -> list:
        return self.data[field_name].tolist()

    # 获取每一行，返回二维 list
    def get_rows(self) -> list:
        return self.data.values.tolist()

    # 获取符合某个 period 的某一列字段，返回 list
    def get_period(self, period, field_name: str) -> list:
        result = self.data.loc[self.data["period"] == period, field_name].tolist()

        return result

    # 获取符合某个 period 的某一列字段，返回 list
    def get_request_type(self, request_type, field_name: str) -> list:
        result = self.data.loc[
            self.data["request_type"] == request_type, field_name
        ].tolist()

        return result

    def get_col_by_other_head(self, conditions: dict, field_name: str) -> list:
        mask = pd.Series(True, index=self.data.index)

        for head_name, value in conditions.items():
            mask &= self.data[head_name] == value

        result = self.data.loc[mask, field_name].tolist()

        return result

    def get_time_range(self, start_time: str, end_time: str, field_name: str) -> list:
        timestamps = pd.to_datetime(self.data["timestamp"])

        mask = (timestamps.dt.strftime("%H:%M") >= start_time) & (
            timestamps.dt.strftime("%H:%M") <= end_time
        )

        return self.data.loc[mask, field_name].tolist()
