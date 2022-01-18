# _*_ coding=utf-8 _*_
"""
此模块用于将文书中的不同词性的词分出来
名词
动词
形容词
"""

import jieba
from ltp import LTP

# 词性列表
noun_dic = []
verb_dic = []
adj_dic = []

# 用于可视化统计
noun_statistics = {}
verb_statistics = {}
adj_statistics = {}

ltp = LTP()
jieba.load_userdict('D:\\study\\DataScienceFoundation\\spider_note\\分词\\auto_note\\word\\dic.txt')
ltp.init_dict('D:\\study\\DataScienceFoundation\\spider_note\\分词\\auto_note\\word\\dic.txt')


def word_sort_note(sentences):
    for sentence in sentences:
        verb_note(sentence)
        noun_note(sentence)
        adj_note(sentence)


def verb_note(sentence):
    seg, hidden = ltp.seg([sentence])
    pos = ltp.pos(hidden)
    for i in range(0, len(pos[0])):
        if pos[0][i] == 'v':
            if seg[0][i] in verb_dic:
                verb_statistics[seg[0][i]] += 1
            else:
                verb_dic.append(seg[0][i])
                verb_statistics[seg[0][i]] = 1


def noun_note(sentence):
    seg, hidden = ltp.seg([sentence])
    pos = ltp.pos(hidden)
    for i in range(0, len(pos[0])):
        if pos[0][i] == 'n':
            if seg[0][i] in noun_dic:
                noun_statistics[seg[0][i]] += 1
            else:
                noun_dic.append(seg[0][i])
                noun_statistics[seg[0][i]] = 1


def adj_note(sentence):
    seg, hidden = ltp.seg([sentence])
    pos = ltp.pos(hidden)
    for i in range(0, len(pos[0])):
        if pos[0][i] == 'a':
            if seg[0][i] in adj_dic:
                adj_statistics[seg[0][i]] += 1
            else:
                adj_dic.append(seg[0][i])
                adj_statistics[seg[0][i]] = 1
