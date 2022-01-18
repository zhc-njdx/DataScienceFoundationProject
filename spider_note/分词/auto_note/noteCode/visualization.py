# _*_ coding=utf-8 _*_
"""
可视化 将不同词的频率以图表形式呈现出来
"""
import matplotlib.pyplot as plt


def statistics(dic, table_type):
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    keys = list(dic.keys())
    values = list(dic.values())

    plt.bar(keys, values)
    plt.title(table_type)

    plt.show()