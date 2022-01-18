# _*_ coding=utf-8 _*_
from ltp import LTP

ltp = LTP()
ltp.init_dict('D:\\study\\DataScienceFoundation\\spider_note\\分词\\auto_note\\word\\dic.txt')


def cut_file_sentences(file_name):
    file = open("D:\\study\\DataScienceFoundation\\spider_note\\分词\\auto_note\\case\\" + file_name, "r", encoding="gb18030", errors="ignore")
    case = file.read()

    # 使用 ltp 对案例进行分句
    sentences = ltp.sent_split([case])
    return sentences
