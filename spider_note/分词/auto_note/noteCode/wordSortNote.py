# _*_ coding=utf-8 _*_
"""
此模块用于将文书中的不同词性的词分出来
名词
动词
形容词
"""

import jieba
from ltp import LTP

noun_dic = {}
verb_dic = {}
adj_dic = {}

ltp = LTP()
jieba.load_userdict('..\\word\\dic.txt')
ltp.init_dict('..\\word\\dic.txt')


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
                verb_dic[seg[0][i]] += 1
            else:
                verb_dic[seg[0][i]] = 1


def noun_note(sentence):
    seg, hidden = ltp.seg([sentence])
    pos = ltp.pos(hidden)
    for i in range(0, len(pos[0])):
        if pos[0][i] == 'n':
            if seg[0][i] in noun_dic:
                noun_dic[seg[0][i]] += 1
            else:
                noun_dic[seg[0][i]] = 1


def adj_note(sentence):
    seg, hidden = ltp.seg([sentence])
    pos = ltp.pos(hidden)
    for i in range(0, len(pos[0])):
        if pos[0][i] == 'a':
            if seg[0][i] in adj_dic:
                adj_dic[seg[0][i]] += 1
            else:
                adj_dic[seg[0][i]] = 1
