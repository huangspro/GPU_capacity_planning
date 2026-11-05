from math import exp, log

from scipy.stats import chi2
from scipy.special import gammaln

from src.dataset.dataset import Dataset


new_dataset = Dataset(
    "/home/hhy/hhy-data/Python/GPU_capacity_planning/data/request_count.csv"
)

t_r = new_dataset.get_column("text_requests")
i_r = new_dataset.get_column("image_requests")

ave_t_r = sum(t_r) / len(t_r)
ave_i_r = sum(i_r) / len(i_r)


# 统计实际频数
t_dict = {}
i_dict = {}

for x in t_r:
    t_dict[x] = t_dict.get(x, 0) + 1

for x in i_r:
    i_dict[x] = i_dict.get(x, 0) + 1


# 计算泊松分布拟合优度检验
def poisson_test(data, frequency, lam, name):

    n = len(data)

    theoretical_frequency = {}

    max_k = max(max(data), 0)

    # 计算理论频数（使用对数形式，避免数值溢出）
    for k in range(max_k + 1):

        if lam == 0:
            p = 1.0 if k == 0 else 0.0

        else:
            # log(P(X=k)) = -lambda + k*log(lambda) - log(k!)
            log_p = -lam + k * log(lam) - gammaln(k + 1)

            # 恢复概率
            p = exp(log_p)

        theoretical_frequency[k] = n * p

    # 合并理论频数小于5的相邻组
    groups = []

    current_o = 0
    current_e = 0

    for k in range(max_k + 1):

        current_o += frequency.get(k, 0)
        current_e += theoretical_frequency[k]

        if current_e >= 5:
            groups.append((current_o, current_e))

            current_o = 0
            current_e = 0

    # 将最后剩余的频数合并到上一组
    if current_e > 0:

        if groups:
            old_o, old_e = groups[-1]
            groups[-1] = (
                old_o + current_o,
                old_e + current_e
            )

        else:
            groups.append((current_o, current_e))

    # 计算卡方统计量
    chi_square = 0

    for observed, expected in groups:

        if expected > 0:
            chi_square += (observed - expected) ** 2 / expected

    # 估计了一个参数 lambda，自由度为组数减2
    df = len(groups) - 2

    p_value = chi2.sf(chi_square, df) if df > 0 else float("nan")

    # 输出检验结果
    print("\n", name)
    print("lambda = ", lam)
    # print("Observed frequency = ", frequency)
    # print("Theoretical frequency = ", theoretical_frequency)
    # print("Merged groups = ", groups)
    print("Chi-square statistic = ", chi_square)
    # print("Degree of freedom = ", df)
    # print("p-value = ", p_value)

    if p_value < 0.05:
        print("Reject H0: The data does not follow a Poisson distribution.")

    else:
        print("Cannot reject H0: The data may follow a Poisson distribution.")


# 对 NT 进行泊松拟合优度检验
poisson_test(
    t_r,
    t_dict,
    ave_t_r,
    "NT (Text Requests)"
)

# 对 NI 进行泊松拟合优度检验
poisson_test(
    i_r,
    i_dict,
    ave_i_r,
    "NI (Image Requests)"
)