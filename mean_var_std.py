import numpy as np


def calculate(list):
    if len(list) == 9:
        list = np.array(list).reshape(3, 3)

        mean_col = (list.mean(axis=0)).tolist()
        mean_row = (list.mean(axis=1)).tolist()
        mean_list = [mean_col, mean_row, list.mean()]

        var_col = (list.var(axis=0)).tolist()
        var_row = (list.var(axis=1)).tolist()
        var_list = [var_col, var_row, list.var()]

        std_col = (list.std(axis=0)).tolist()
        std_row = (list.std(axis=1)).tolist()
        std_list = [std_col, std_row, list.std()]

        max_col = (list.max(axis=0)).tolist()
        max_row = (list.max(axis=1)).tolist()
        max_list = [max_col, max_row, list.max()]

        min_col = (list.min(axis=0)).tolist()
        min_row = (list.min(axis=1)).tolist()
        min_list = [min_col, min_row, list.min()]

        sum_col = (list.sum(axis=0)).tolist()
        sum_row = (list.sum(axis=1)).tolist()
        sum_list = [sum_col, sum_row, list.sum()]

        calculations = {"mean": mean_list, "variance": var_list, "standard deviation": std_list,
                        "max": max_list, "min": min_list, "sum": sum_list}
    else:
        raise ValueError("List must contain nine numbers.")

    return calculations