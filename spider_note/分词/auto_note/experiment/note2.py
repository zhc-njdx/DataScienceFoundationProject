# encoding=utf-8
import jieba
import jieba.analyse
import jieba.posseg as pos
import re

# jieba.enable_paddle()# 启动paddle模式。 0.40版之后开始支持，早期版本不支持
# strs=["我来到北京清华大学","乒乓球拍卖完了","中国科学技术大学"]
# for str in strs:
#     seg_list = jieba.cut(str,use_paddle=True) # 使用paddle模式
#     print("Paddle Mode: " + '/'.join(list(seg_list)))

jieba.load_userdict('word\\word.txt')

seg_list = jieba.cut("他叫汤姆和杰克去中国人民法院拿外衣。", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# jieba.suggest_freq('中国人民法院',True)
seg_list = jieba.cut("他叫汤姆和杰克去中国人民法院拿外衣。")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

seg_list = jieba.cut("广西壮族自治区钦州市中级人民法院审理钦州市人民检察院指控原审被告人杨光毅犯强奸罪一案")
print(", ".join(seg_list))
seg = pos.cut("审判长李勇")
print(list(seg))
for word,flag in seg:
    print(word + " " + flag)


n = "王小明"
name = "人民检察院"
if re.match(".*人民法院|.*人民检察院",name) is not None:
    print("Yes")

