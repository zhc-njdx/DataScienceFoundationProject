# _*_ coding:utf-8 _*_

from ltp import LTP
import jieba
ltp = LTP()

ltp.init_dict("word/word.txt",max_window=4)

# file = open("case.txt","r",encoding='gb18030',errors='ignore')
file = open("case/case.txt", "r", encoding='utf-8')

case = file.read()

# 分句，以句号分句
sents = ltp.sent_split([case])

print(sents[0])

file_write = open("analysis/analysis.txt","w",encoding='utf-8')

people_name = {}

for sent in sents:
    # print(sent+'\n')

    # file_write.write(sent+"\n")

    seg,hidden = ltp.seg([sent])
    pos = ltp.pos(hidden)
    # print(seg)
    # print(pos)

    i = 0
    for p in pos[0]:
        if p == 'nh':
            name = seg[0][i]
            if name in people_name.keys():
                people_name[name] += 1
            else:
                people_name[name] = 1
        i += 1

    # file_write.write(str(seg)+"\n")
    # file_write.write(str(pos)+"\n")

# for key,value in people_name:
#     print(key + " " + value)
print(people_name)