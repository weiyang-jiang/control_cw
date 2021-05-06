import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

data_inital = pd.read_csv(f"./Eplus-env-IW-right-time-v3-res1/Eplus-env-sub_run1/output/eplusout.csv")
data = data_inital.iloc[:, 1:]
data.index = data_inital["Date/Time"]

x_label = data_inital.columns[0]
# x_ticks = [data.iloc[2200 * (i + 1), 0] for i in range(3)]

# x_ticks_range = [2200 * (i + 1) for i in range(len(x_ticks))]
if not os.path.exists("./Eplus-env-IW-right-time-v3-res1/Eplus-env-sub_run1/img_detail"):
    os.mkdir("./Eplus-env-IW-right-time-v3-res1/Eplus-env-sub_run1/img_detail")

for i in range(data.shape[1]):
    y_label = data.columns[i]
    plt.figure(i + 1, dpi=100)
    y = data.loc[" 01/23  00:05:00":" 01/30  00:05:00", data.columns[i]]
    x = range(y.shape[0])
    plt.plot(x, y)
    # plt.xticks(x_ticks_range, x_ticks)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    y_label = re.search("(.*):(.*)\[(.*)", y_label).group(2)
    y_label = re.sub(" ", "_", y_label)[:-1]
    plt.savefig(f"./Eplus-env-IW-right-time-v3-res1/Eplus-env-sub_run1/img_detail/{y_label}_detail")
    plt.show()