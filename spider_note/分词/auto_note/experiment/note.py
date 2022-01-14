# _*_ coding=utf-8 _*_

from ltp import LTP
from noteCode import convert

# people_deal 里面进行逻辑处理
layer = {}
criminal = ""
victim = []
people = {}

# cate函数里进行词性分析
adj = {}
verb = {}
noun = {}
name = {}

ltp = LTP()

ltp.init_dict(path='../word/word.txt', max_window=4)

# 把 case 目录下的 .doc 文件转化为 .txt 文件
# return case 下的文件名列表
def get_files():
    return convert.files_in_dir('case')

# 将案例按句分开，写进analysis文件
# return 分开的句子的列表
def split_sent(file_name):
    file = open("case\\"+file_name,"r",encoding="gb18030",errors="ignore")
    analysis = open("analysis\\"+"analysis_"+file_name[5:],"w",encoding="gb18030",errors="ignore")
    case = file.read()
    sents = ltp.sent_split([case])
    for sent in sents:
        # print(sent)
        # sent.strip()
        # print(sent)
        analysis.write(sent+'\n')
    return sents

'''将案例中的人名全部统计出来'''
def people_deal(sents):
    for sent in sents:
        seg,hidden = ltp.seg([sent])
        pos = ltp.pos(hidden)

        j = 0  # 帮助打印句子而设置的变量，防止打印多次sent
        for i in range(0,len(pos[0])):
            # 处理人名
            if(pos[0][i] == 'nh'):
                if j == 0:
                    # print(sent)
                    j = 1
                name = seg[0][i]
                # print(name)
                '''假如在人物字典中，次数加一；不在则加入字典，次数为一'''
                if name not in people.keys():
                    # 加入的第一个人肯定是犯罪嫌疑人，其信息都在这句话中
                    # 这个在某些案例中不成立
                    if len(people) == 0:
                        criminal_deal(sent)

                    people[name] = 1
                else:
                    people[name] += 1
        # print(seg)
        # print(pos)
    # print(list(people.keys())
    # 相关审判人员
    # 有些案例中并没有审理人员
    layer["审判长"] = list(people.keys())[-4]
    layer["审理员一"] = list(people.keys())[-3]
    layer["审理员一"] = list(people.keys())[-2]
    layer["书记员"] = list(people.keys())[-1]

'''处理犯罪嫌疑人的信息，包括民族，出生等'''
def criminal_deal(sent):
    seg, hidden = ltp.seg([sent])
    pos = ltp.pos(hidden)
    # print(seg)
    # print(pos)

'''笼统地统计不同词性出现频率'''
def cate(sents):
    for sent in sents:
        seg,hidden = ltp.seg([sent])
        pos = ltp.pos(hidden)
        # print(sent)
        # print(pos)
        for i in range(0,len(pos[0])):
            if pos[0][i] == 'v':
                v = seg[0][i]
                if v not in verb:
                    verb[v] = 1
                else:
                    verb[v] += 1
            elif pos[0][i] == 'a':
                a = seg[0][i]
                if a not in adj:
                    adj[a] = 1
                else:
                    adj[a] += 1
            # elif re.match("n",pos[0][i]) is not None:
            elif pos[0][i] == 'n':
                n = seg[0][i]
                if n not in noun:
                    noun[n] = 1
                else:
                    noun[n] += 1
            elif pos[0][i] == 'nh':
                nh = seg[0][i]
                if nh not in name:
                    name[nh] = 1
                else:
                    name[nh] += 1
    # print(verb)
    # print(adj)
    # print(noun)
    print(name)

'''可视化 将不同词的频率以图表形式呈现出来'''
import matplotlib.pyplot as plt

def statistics(dic):
    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    keys = list(dic.keys())
    values = list(dic.values())
    # waters = ['碳酸饮料', '绿茶', '矿泉水', '果汁', '其他']
    # buy_number = [6, 7, 6, 1, 2]

    plt.bar(keys, values)
    plt.title('词语出现频次')

    plt.show()


# 分析每个人名在案例中的身份和信息
def analysis_people(sents):
    people_name_identity = {}
    for sent in sents:
        # 分词
        seg,hidden = ltp.seg([sent])
        pos = ltp.pos(hidden)
        #处理
        # for i in range(0,len(pos[0])):
        for i in range(0,len(pos[0])):
            if pos[0][i] == 'nh':
                # 第一次出现
                if seg[0][i] not in people_name_identity.keys():
                    print(seg)
                    print(pos)
                    # 往回找其对应的名词应该就是其身份
                    j = i
                    while pos[0][j] != 'n' and pos[0][j] != 'b':
                        j -= 1
                        if j == -1:
                            break
                    # 找到了
                    if j != -1:
                        iden = seg[0][j]
                        if j - 1 != -1:
                            iden = seg[0][j - 1] + iden
                        people_name_identity[seg[0][i]] = iden
                    # 没找到
                    else:
                        people_name_identity[seg[0][i]] = "null"
    print(people_name_identity)








if __name__ == "__main__":
    files = get_files()
    file = files[0]
    sents = split_sent(file)
    analysis_people(sents)
    # 对 case 目录下所有文件的处理
    # for file in files:
    #     sents = split_sent("case\\"+file)

    # cate(sents)
    # statistics(verb)
    # people_deal(sents)
    # print(people)
    # print(list(people.keys()))
    # print(layer)
