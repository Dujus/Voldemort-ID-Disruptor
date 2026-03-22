from pypinyin import lazy_pinyin# 大饼：加入中文转拼音逻辑（已实现）
import re
from  Pinyin2Hanzi import simplify_pinyin ,viterbi,dag ,DefaultHmmParams
def swapcase(s):
    """
    切换大小写
    :param s:
    :return:
    """
    return s.swapcase()

def word_break(s, break_dict):
    """

    :param s: 字符串
    :param break_dict: 我自定义的映射
    :return:
    """
    words = list(s)
    i = 0
    while i < len(words):
        if words[i] in break_dict:
            words[i] = break_dict.get(words[i])
        i += 1
    return "".join(words)

def Chi_to_Rom(s):

  Eng_list = lazy_pinyin(s)

  return "".join(Eng_list)


def Chi_Homophony(s):
    hmmparams = DefaultHmmParams()
    # re.split 函数，运用unicode码，找出所有中文字符 findall(string[, pos[, endpos]])
    chinese_list = re.findall(r'[\u4e00-\u9fa5]', s)
    remain_part = re.split(r'[\u4e00-\u9fa5]', s)
    remains = "".join(remain_part)

    Eng_list = lazy_pinyin(chinese_list)
    if not Eng_list:
        print("原字符串中无中文，谐音是无效的")
        return s
    safe_list = []
    for py in Eng_list:
        safe_list.append(simplify_pinyin(py))
    result = viterbi(hmm_params=hmmparams, observations=safe_list, path_num=300)
    if not result:
        print("原字符串中无中文，谐音是无效的")
        return s
    hom_part = "".join(result[min(len(result) - 1, 300)].path)  # 原库中结果对象有两类：score/path
    refreshed_s = hom_part + remains
    return refreshed_s
def save(r, s):
    try:
        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write("这是处理结果：\n")
            f.write(f"原ID为：{s}\n")
            for idx, data in r.items():
                f.write(f"ID:{data}\n")
            print("成功录入result.txt！")
    except Exception as e:
        print(f"录入不成功:{e}")



