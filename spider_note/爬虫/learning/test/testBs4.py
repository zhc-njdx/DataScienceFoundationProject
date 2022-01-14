'''
- Tag
- NavigableString
- BeautifulSoup
- Comment
'''

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")  # 树形结构

# print(type(bs.title))

# 1. Tag 标签及其内容: 默认拿到它找到的第一个内容

# print(type(bs.title.string))

# 2.NavigableString 标签里的内容（字符串）

# print(type(bs))

# 3.BeautifulSoup 表示整个文档

# 4.Comment 是一个特殊的NavigableString 输出内容不包含注释符号

# print(type(bs.a.string))

# -------------------------------------------------------


# 文档的遍历

# 获取特定标签的内容
# print(bs.head.contents)
# print(bs.head.contents[1])

# 更多例子，搜索文档


# 文档的搜索

# 1.find_all
# 字符串过滤: 会查找与字符串完全相同的内容
# t_list = bs.find_all("a")

import re
# 正则表达式搜索: 使用 search() 方法来匹配内容
# 匹配一个标签来找，找到一整个标签

# t_list = bs.find_all(re.compile("a"))


# 方法: 传入一个函数(方法)，根据函数的要求来搜索

# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)

# 2.kwargs  参数

# t_list = bs.find_all(class_=True)

# for item in t_list:
#     print(item)

# 3. text参数

# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])

# t_list = bs.find_all(text=re.compile("\d"))  # 应用正则表达式来查找包含特定文本的内容 （标签里的字符串）

# 4.limit 参数

# t_list = bs.find_all("a",limit=3)
#
# print(t_list)


# 5.css 选择器

# print(bs.select('title'))    # 通过标签来寻找

# print(bs.select(".mnav"))  # 通过类名来查找

# print(bs.select("#u1"))  # 通过id来查找


# print(bs.select("a[class='bri']"))   # 通过属性来查找

# print(bs.select("head > title"))  # 通过子标签来查找

print(bs.select(".mnav ~ .bri")[0].get_text())  # 通过兄弟标签来查找
