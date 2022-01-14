# _*_ coding=utf-8 _*_

import jieba
from ltp import LTP
import jieba.posseg as poss
import doctotxt
import re

# jieba.enable_paddle()

'''
相对于ltp来说，jieba分词似乎是一个更好的选择，在载入词典放方面
jieba 和 ltp 结合版
jieba 对词典更加敏感
ltp 对名字更加敏感

分词思路如下：
1、实现对于案例中主要人物的信息抽取
    extract_person_info方法
    1) 主要当事人的详细信息: 出生日期、出生地、性别、民族等
    2) 其他人员的名字和一些信息
    
2、实现对于案件信息的抽取，以刑事案件为主，民事和赔偿等案例过于杂乱
    extract_story方法
    1) 案由
    2) 审判结果
    3) 根据时间来抽取一些事件
    

3、实现对于案件审理背景的抽取，比如法院，审查人员，审查时间等
    extract_background方法
    1) 提取文书类型和机构
    2) 提取文书时间
    3) 如果有审判人员，提取出审判人员
    4) 提取出相关法院
    
'''

# 载入词典
jieba.load_userdict("word\\dic.txt")

ltp = LTP()
ltp.init_dict("word\\dic.txt")

case_background = {}
case_person = {}
person_statistics = {}
case_story = {}


def print_dic(dic):
    for key, value in dic.items():
        print(str(key) + ": ")
        if isinstance(value,list):
            for item in value:
                print(item)
        else:
            print(str(value))


# 得到文件列表
def get_file_list():
    return doctotxt.files_in_dir('case')


# 将案例文本分句
def cut_file_sentences(file_name):
    file = open("case\\" + file_name, "r", encoding="gb18030", errors="ignore")
    case = file.read()

    # 使用 ltp 对案例进行分句
    sentences = ltp.sent_split([case])
    return sentences


def extract_background(sentences):
    # 头两行就是总的信息类型
    case_background["文书机构"] = sentences[0]
    case_background["文书类型"] = sentences[1]
    # 时间
    case_background["时间"] = "无"
    for i in range(0, len(sentences)):
        if re.match(".*年.*月.*日", sentences[i]) is not None:
            case_background["时间"] = sentences[i]

    # 如果有审判人员 抽取出来
    case_background["审判长"] = "无"
    case_background["审判员"] = "无"
    case_background["书记员"] = "无"
    case_background["法官助理"] = "无"
    for i in range(0, len(sentences)):
        if re.match("审.*判.*长|审.*判.*员|书.*记.*员|法.*官.*助.*理", sentences[i]) is not None:
            str = sentences[i]
            for m in range(0, len(sentences[i])):
                if '\u4e00' > sentences[i][m] or sentences[i][m] > '\u9fa5':
                    str = str.replace(sentences[i][m], '')
            sentences[i] = str
            # print(sentences[i])

            # sentences[i].replace(' ','')
            # print(sentences[i])
            name = ""
            seg_list = list(jieba.cut(sentences[i]))
            for j in range(len(seg_list[0]), len(sentences[i])):
                # c = sentences[i][j]
                # if '\u4e00' <= c <= '\u9fa5':
                #     if c == '审' or c == '判' or c == '长' or c != '员' or \
                #             c == '书' or c == '记':
                #         continue
                name += sentences[i][j]

            # seg_list = list(jieba.cut(sentences[i]))
            case_background[seg_list[0]] = name
            case_person[name] ={"身份": seg_list[0]}

    # 相关法院
    case_background["相关法院"] = []
    cnt = 0
    for i in range(0, len(sentences)):
        words = list(poss.cut(sentences[i]))
        # 分词后在词中分析
        for j in range(0, len(words)):
            # 如果可以匹配上 人民法院
            if re.match(".*人民法院|.*人民检察院", words[j].word) is not None:
                court = words[j].word
                # print(court)
                # 追溯地名
                k = j - 1
                while (re.match(".*区", words[k].word) is not None) or (words[k].flag == 'ns'):
                    court = words[k].word + court
                    k -= 1
                    if k == -1:
                        break
                # print(court)
                # 前面要有地名前缀 不然不用加入字典中
                if k != j - 1 and court not in case_background["相关法院"]:
                    case_background["相关法院"].append(court)
                    cnt += 1


# words 是分词后的 词列表
# index 是 人名第一次出现的位置
# 处理人物信息
def deal_person_info_ltp(seg, pos, index):
    person = {}

    # 人物在案件中的身份
    i = index - 1
    person["身份"] = ""
    while i != -1:
        if pos[i] == 'n' or pos[i] == 'b':
            person["身份"] = seg[i] + person["身份"]
        elif pos[i] != 'wp':
            break
        i -= 1
    if len(person["身份"]) == 0:
        person["身份"] = "未知"

    # 人物出生地等详细信息
    j = index + 1
    # person["性别"] = "未知"
    # person["民族"] = "未知"
    # person["出生日期"] = "未知"
    birthday = ""
    cnt_birth = 0
    # person["出生地"] = "未知"
    birthplace = ""
    first = 0
    no_birthplace = False
    while j != len(pos):
        if re.match("男|女", seg[j]) is not None:
            person["性别"] = seg[j]

        elif re.match(".*族", seg[j]) is not None:
            person["民族"] = seg[j]

        elif pos[j] == 'nt':
            cnt_birth += 1
            if re.match(".*年|.*月|.*日", seg[j]) is not None:
                birthday += seg[j]
            # 判断日期后面是否为  '出生'
            if cnt_birth == 3:
                if j != len(pos) - 1 and re.match("出生.*", seg[j + 1]) is None:
                    birthday = ""

        elif pos[j] == 'ns':
            # 判断地址前面是否为 '出生于' 或 '住'
            if first == 0:
                first = 1
                if re.match(".*住.*|.*出生.*", seg[j - 1]) is None:
                    no_birthplace = True
            birthplace += seg[j]
        j += 1

    if birthday != "":
        person["出生日期"] = birthday
    if (not no_birthplace) and (birthplace != ""):
        person["出生地"] = birthplace

    case_person[seg[index]] = person

# 使用jieba对人物信息进行提取

def deal_person_info_jieba(sentence, name):
    # print(list(jieba.cut(name)))
    jieba.add_word(name, 3, 'nr')
    words = list(poss.cut(sentence))
    # print(words)
    index = 0
    for i in range(0, len(words)):
        if words[i].word == name:
            index = i
            break

    person = {}

    # 人物在案件中的身份
    i = index - 1
    person["身份"] = ""
    while i != -1:
        if words[i].flag == 'n' or words[i].flag == 'j':
            person["身份"] = words[i].word + person["身份"]
        elif words[i].flag != 'x':
            break
        i -= 1
    if len(person["身份"]) == 0:
        person["身份"] = "未知"

    # 人物出生地等详细信息
    j = index + 1
    # person["性别"] = "未知"
    # person["民族"] = "未知"
    # person["出生日期"] = "未知"
    birthday = ""
    last_m = 0
    # person["出生地"] = "未知"
    birthplace = ""
    first = 0
    no_birthplace = False
    while j != len(words):
        if re.match("男|女", words[j].word) is not None:
            person["性别"] = words[j].word

        elif re.match(".*族", words[j].word) is not None:
            person["民族"] = words[j].word

        elif words[j].flag == 'm':
            last_m = j
            birthday += words[j].word

        elif words[j].flag == 'ns':
            # 判断地址前面是否为 '出生于' 或 '住'
            if first == 0:
                first = 1
                if re.match(".*住.*|.*出生.*", words[j - 1].word) is None:
                    no_birthplace = True
            birthplace += words[j].word
        j += 1

    # 判断日期后面是否为  '出生'
    if last_m != 0:
        if last_m != len(words) - 1 and re.match("出生.*", words[last_m + 1].word) is None:
            birthday = ""
    if re.match(".*年.*月.*日",birthday) is None:
        birthday = ""

    if birthday != "":
        person["出生日期"] = birthday
    if (not no_birthplace) and (birthplace != ""):
        person["出生地"] = birthplace

    case_person[name] = person


def extract_person_info(sentences):
    for i in range(0, len(sentences)):
        # words = list(poss.cut(sentences[i]))
        seg, hidden = ltp.seg([sentences[i]])
        pos = ltp.pos(hidden)
        for j in range(0, len(pos[0])):
            if pos[0][j] == 'nh':
                name = seg[0][j]
                name = name.replace('\u3000', '')
                name = name.replace(' ', '')
                # print(words[j].word)
                if name in case_person.keys():
                    person_statistics[name] += 1
                # 人名第一次出现，加入字典并进行处理
                else:
                    # 对第一次出现人名做进一步处理 防止分词错误
                    isFalse = False
                    for n in list(person_statistics.keys()):
                        if re.match(n + ".*", name) is not None:
                            person_statistics[n] += 1
                            isFalse = True
                    if not isFalse:
                        # deal_person_info_ltp(seg[0], pos[0], j)
                        deal_person_info_jieba(sentences[i], name)
                        person_statistics[name] = 1


def extract_story(sentences):
    #针对刑事案件有如下
    begin = 0
    end = 0
    for i in range(0,len(sentences)):
        # print(sentences[i])
        if re.match("经复核确认.*",sentences[i]) is not None:
            begin = i
        if re.match("上述事实.*",sentences[i]) is not None:
            end = i
    story = []
    for i in range(begin,end):
        story.append(sentences[i])
    case_story['案由'] = story
    # print(str(begin)+" " + str(end))


'''可视化 将不同词的频率以图表形式呈现出来'''
import matplotlib.pyplot as plt

def statistics(dic):
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    keys = list(dic.keys())
    values = list(dic.values())

    plt.bar(keys, values)
    plt.title('人物出现频次')

    plt.show()


if __name__ == '__main__':
    file = get_file_list()[9]
    extract_story(cut_file_sentences(file))
    extract_person_info(cut_file_sentences(file))
    extract_background(cut_file_sentences(file))
    print_dic(case_background)
    print_dic(person_statistics)
    print_dic(case_person)
    print_dic(case_story)
    statistics(person_statistics)
