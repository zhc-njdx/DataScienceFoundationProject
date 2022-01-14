# _*_ coding=utf-8 _*_

from ltp import LTP

ltp = LTP()

ltp.init_dict("word\\word.txt")

seg, hidden = ltp.seg(["他叫汤姆和杰克去中国人民法院拿外衣。"])
ner = ltp.ner(hidden)
pos = ltp.pos(hidden)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]
# [[('Nh', 2, 2)]]

print(pos)
print(ner)
# tag, start, end = ner[0][0]
# print(tag,":", "".join(seg[0][start:end + 1]))
for tag, start, end in ner[0]:
    print(tag,":", "".join(seg[0][start:end + 1]))
# Nh : 汤姆
srl = ltp.srl(hidden)
print(srl)

seg,hidden = ltp.seg(["王小明系湖南省娄底市人，在中国人民法院工作。"])
print(seg)