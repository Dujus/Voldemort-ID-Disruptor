from pypinyin import lazy_pinyin# 大饼：将来加入中文转拼音逻辑（已实现）


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
    while i < len(s):
        if words[i] in break_dict:
            words[i] = break_dict.get(words[i])
        i += 1
    return "".join(words)

def Chi_to_Rom(s):

  Eng_list = lazy_pinyin(s)

  return "".join(Eng_list)



