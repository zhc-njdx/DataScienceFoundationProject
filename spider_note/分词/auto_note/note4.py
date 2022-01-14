from ltp import LTP

ltp = LTP()

# segment, _ = ltp.seg(["他叫汤姆去拿外衣。"])
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]

# 对于已经分词的数据
# segment, hidden = ltp.seg(["他/叫/汤姆/去/拿/外衣/。".split('/')], is_preseged=True)


# seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
# pos = ltp.pos(hidden)

# print(seg)
# print(pos)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]
# [['r', 'v', 'nh', 'v', 'v', 'n', 'wp']]

seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
print(seg)
ner = ltp.ner(hidden)
print(ner)
# [['他', '叫', '汤姆', '去', '拿', '外衣', '。']]
# [[('Nh', 2, 2)]]

tag, start, end = ner[0][0]
print(tag,":", "".join(seg[0][start:end + 1]))
# Nh : 汤姆

seg,hidden = ltp.seg(["越秀区人民检察院指控被告人刘永寿、刘水养、杨杰犯非法买卖枪支罪一案"])
pos = ltp.pos(hidden)
print(seg[0])
print(pos[0])

c = "1 2 3 4 5 6"
c = c.replace(' ','')
print(c)

