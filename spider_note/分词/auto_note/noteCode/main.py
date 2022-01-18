# _*_ coding=utf-8 _*_
import sys
sys.path.append('..')
sys.path.append('D:\\study\\DataScienceFoundation\\spider_note\\分词\\auto_note')
import json
from noteCode import caseInfoNote, convert, extract, visualization, wordSortNote

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
    visualization.statistics(caseInfoNote.person_statistics, "人物分布")
    visualization.statistics(wordSortNote.verb_statistics, "动词分布")
    visualization.statistics(wordSortNote.noun_statistics, "名词分布")
    visualization.statistics(wordSortNote.adj_statistics, "形容词分布")


def convert_json(filename):
    case_in_json = {"审判信息": caseInfoNote.case_background,
                    "案件主要人物": caseInfoNote.case_main_person,
                    "案件其他人物": caseInfoNote.case_other_person,
                    "案件经由": caseInfoNote.case_story,
                    "名词": wordSortNote.noun_dic,
                    "动词": wordSortNote.verb_dic,
                    "形容词": wordSortNote.adj_dic}
    file_create = open(filename, 'w')
    file_create.close()
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(case_in_json, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    file_list = get_file()
    # for file in file_list:
    #     note_service(file)
    file = file_list[9]
    note_service(file)
    filename = "D:\\study\\DataScienceFoundation\\myweb\\web\\jsonResult\\result.json"
    convert_json(filename)
