# _*_ coding=utf-8 _*_
"""
针对case目录下的案例
若是.doc则进行转换成.txt
返回 file的列表
"""

import win32com.client
import os
import re
import json

# 文书的目录
dir_name = "D:\\study\\DataScienceFoundation\\spider_note\\分词\\auto_note\\case"


# 将目录下的文件放进文件列表中返回
def files_in_dir():
    my_files = []
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if re.match(".*\.txt", file) is not None:
                my_files.append(file)
            else:
                new_file = file[:-4] + ".txt"
                change_word_to_txt(dir_name + "\\" + file, dir_name + "\\" + new_file)
                os.remove(dir_name + "\\" + file)
                my_files.append(new_file)
    return my_files


# 将.doc转换成.txt
def change_word_to_txt(word_path, save_path):
    word = win32com.client.Dispatch('Word.Application')  # 调用word应用
    doc = word.Documents.Open(word_path)
    doc.SaveAs(save_path, 4)
    doc.Close()
    word.Quit()


def dic_convert_json(dic, filename):
    with open('result\\' + filename, 'a') as f:
        f.write(json.dumps(dic, ensure_ascii=False, indent=2))

# if __name__ == '__main__':
#     for file in files_in_dir('case'):
#         print(file)
# try:
#     readPath = r'D:\download\Documents\Code\Python\test1\24\B\1.docx'  # 要读取的word文件路径
#     savePath = r'D:\download\Documents\Code\Python\test1\25\A\2.txt'  # 保存的绝对路径
#     change_word_to_txt(readPath, savePath)
#     print('保存成功！')
# except Exception as e:
#     print(e)
