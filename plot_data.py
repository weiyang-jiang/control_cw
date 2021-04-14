import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re


class analysis_data(object):
    def __init__(self, PATH):
        self.PATH = PATH
        self.data = pd.read_csv(f"./{PATH}/Eplus-env-sub_run1/output/eplusout.csv")

    def plot_data(self):
        x_label = self.data.columns[0]
        x_ticks = [self.data.iloc[2200*(i+1), 0] for i in range(3)]
        x = range(self.data.shape[0])
        x_ticks_range = [2200 * (i + 1) for i in range(len(x_ticks))]
        img_path = self.__create_path(f"./{self.PATH}/img")
        for i in range(self.data.shape[1] - 1):
            y_label = self.data.columns[i + 1]
            plt.figure(i+1, dpi=100)
            y = self.data.iloc[:, i+1]
            plt.plot(x, y)
            plt.xticks(x_ticks_range, x_ticks)
            plt.ylabel(y_label)
            plt.xlabel(x_label)
            y_label = re.search("(.*):(.*)\[(.*)", y_label).group(2)
            y_label = re.sub(" ", "_", y_label)[:-1]
            plt.savefig(f"./{img_path}/{y_label}.png")

    def save_power(self):
        power_sum = self.data["EMS:IW Calculated Heating Demand [KW](TimeStep)"].sum()
        power_sum = pd.DataFrame(data=power_sum, index=[1], columns=["power_sum"])
        power_path = self.__create_path(f"./{self.PATH}/power")
        power_sum.to_csv(f"./{power_path}/power_1.csv")
        return power_sum

    def __create_path(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        return path