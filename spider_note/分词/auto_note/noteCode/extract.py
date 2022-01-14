# _*_ coding=utf-8 _*_
from ltp import LTP

ltp = LTP()
ltp.init_dict('..\\word\\dic.txt')


def cut_file_sentences(file_name):
    file = open("..\\case\\" + file_name, "r", encoding="gb18030", errors="ignore")
    case = file.read()

    # 使用 ltp 对案例进行分句
    sentences = ltp.sent_split([case])
    return sentences
