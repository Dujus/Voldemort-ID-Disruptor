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
    while i < len(words):
        if words[i] in break_dict:
            words[i] = break_dict.get(words[i])
        i += 1
    return "".join(words)

def Chi_to_Rom(s):

  Eng_list = lazy_pinyin(s)

  return "".join(Eng_list)


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



