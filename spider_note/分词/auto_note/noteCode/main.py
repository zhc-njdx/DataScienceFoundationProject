# _*_ coding=utf-8 _*_
from noteCode import caseInfoNote, convert, extract, visualization, wordSortNote
import json


# 得到case目录下的文书，支持一个或多个
# 返回文书列表 .txt文件列表
def get_file():
    return convert.files_in_dir()


# 接收一个.txt文件
# 进行相应的分词服务
def note_service(file):
    sentences = extract.cut_file_sentences(file)
    wordSortNote.word_sort_note(sentences)
    caseInfoNote.info_extract(sentences)


def visual():
    visualization.statistics(caseInfoNote.person_statistics)


def convert_json(filename):
    case_in_json = {"案件背景": caseInfoNote.case_background, "案件人物": caseInfoNote.case_person,
                    "案件经由": caseInfoNote.case_story, "名词": wordSortNote.noun_dic, "动词": wordSortNote.verb_dic,
                    "形容词": wordSortNote.adj_dic}
    with open(filename, 'a') as f:
        f.write(json.dumps(case_in_json, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    file_list = get_file()
    # for file in file_list:
    #     note_service(file)
    file = file_list[9]
    note_service(file)
    filename = "..\\result\\" + file[:-4] + ".json"
    convert_json(filename)
