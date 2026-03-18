from RiddleCore import Voldemort
import json
import time
import random
from utils import swapcase, word_break , Chi_to_Rom
import Levenshtein # 计算距离用
def main():
    with open('config.json','r') as d: # r是只读
        config = json.load(d) #对 json中的映射字典进行转换

    v = Voldemort(config['break_dict'])
    s = '奥斯瓦尔德W'
    print(f'原码为{s}')
    if input('是否选择汉语切换（请输入0(不使用）或1（使用），其他输入默认为不使用）：').strip() == '1':
        s = Chi_to_Rom(s)
        print('汉语切换后汉语字符转为小写英文，因此不推荐大小写切换')
    if input('是否选择大小写切换（1为使用，其他输入默认为不使用）（Do you want swapcase?1 for yes, other for no):').strip() == '1':
        s = swapcase(s)  # swapcase函数已经被移动到utils当中
    if input('是否选择我的自定义映射，如m映射为nn，(1为使用，其他输入默认为不使用)(（Do you want my Customized Mapping?1 for yes, other for no):').strip() == '1':
        s = word_break(s, v.break_dict)
    if input('是否选择字符映射为数字(1为使用，其他输入默认为不使用)(Do you want some character to words?):').strip() == '1':
        print(f"目前码长为{len(s)}")
        num = input("请输入转化字符数目（前n个将被转化为数字）(numbers of characters transferred )，请输入一个大于0但小于原码长度的正整数，其他输入将跳过该功能:")
        s = v.word_to_num(s, num)

    leng = len(s)
    if input('是否加入随机字母盐值(Do you want adding salt?(1为使用，其他输入默认为不使用):').strip() == '1':
        s += v.make_salt()
        leng += 1
    result_list = {}
    time.sleep(random.uniform(1, 2))  # uniform生成均匀分布浮点数。请原谅 我想通过sleep避免水军盗刷（水军应该不会用我这么粗劣的代码生成假ID吧)
    for result_num in range(5): #这里我更新了逻辑
        new_v = v.disrupt_spell(s,leng)
        result_list[result_num] = {new_v: Levenshtein.distance(new_v,s)}
    print('我们看到了一个字典输出，其中生成了5个结果及其与原码的各自levenshtein距离（即前者到达后者所需做的变换次数）')
    print(result_list)

if __name__== "__main__":
    main()