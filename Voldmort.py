import random
import json
import typing
import time
from pypinyin import lazy_pinyin# 大饼：将来加入中文转拼音逻辑（已实现）
import Levenshtein # 计算两个ID的距离
import re
from  Pinyin2Hanzi import simplify_pinyin ,viterbi,dag ,DefaultHmmParams
class Voldemort(object):

    def __init__(self):

        self.word_dict = {chr(ord('a')+x): x for x in range(0, 26)} # 生成26个字母字典的代码。大饼：未来可用作映射数字（已经理论实现）

        self.reverse_dict = {b: a for a, b in self.word_dict.items()}
        self.break_dict = {"m": "nn","o": "0","0": "o","l": "1","w": "uu","M": "MM","W": "UU"}
    def read_config(self,name='config.json'): # v 1.0.2:可以在config中自定义更改配置
        with open(name, 'r') as d:
            config = json.load(d)
            return config
    def save(self,r,s):
        try:
            with open ('result.txt','w',encoding='utf-8') as f:
                f.write("这是处理结果：\n")
                f.write(f"原ID为：{s}\n")
                for idx,data in r.items():
                    f.write(f"ID:{data}\n")
                print("成功录入result.txt！")
        except Exception as e:
            print(f"录入不成功:{e}")


    def make_salt(self):
        """
        制作加入字符串的盐
        :return:
        """
        return self.reverse_dict.get(random.randint(0 , 25)) # 生成一个随机int数,得到一个随机字符.目前加盐还只从字符中选取。今后可能扩大范围或者加入多个盐

    def Chi_to_Eng(self,s):
        Eng_list = lazy_pinyin(s)
        return "".join(Eng_list)

    def word_to_num(self, s, n):
        """
        n为一个正整数，将字符串中的前n个字符转为数字
        :param n:
        :return:
        """
        try:
            n = int(float(n))
        except:
            print('输入无效，不进行数字映射，进入下一步')
            return s
        temp_leng = len(s)
        temp = list(s)
        if n <= 0 or n > temp_leng :
            return s
        i = 0
        while i < n :
            if temp [i] in self.word_dict:
               temp[i] = str(self.word_dict.get(temp[i])) # 数字也需要以字符格式写入临时数组
               i += 1
            else:
                i += 1
        return "".join(temp)
    def swapcase(self, s):
        """
        切换大小写
        :param s:
        :return:
        """
        return s.swapcase()

    def word_break(self, s):
        """进行一个自定义映射
        """
        words = list(s)
        i = 0
        while i < len(s) :
            if words[i] in self.break_dict:
                words[i] = self.break_dict.get(words[i])
            i += 1
        return "".join(words)
    def construct_dictionary(self):

        """
        返回正向词典：词（小写）对值（0-25），反向字典，值对词
        :return:
        """
        return self.word_dict, self.reverse_dict

    def Chi_Homophony(self,s):
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
        result = viterbi(hmm_params=hmmparams, observations= safe_list, path_num=300)
        if not result:
            print("原字符串中无中文，谐音是无效的")
            return s
        hom_part = "".join(result[min(len(result)-1,300)].path)  # 原库中结果对象有两类：score/path
        refreshed_s = hom_part + remains
        return refreshed_s
    def disrupt_spell(self, s):
        """
        s:str,原ID号
        :return:
        """
        copy_s = s # 字符串不可变，制作副本简单
        config = self.read_config()
        result_count = config.get('result_count', 5)
        print( f'原码为{s}')
        Chi_choice = input('是否选择汉语切换（请输入0(不使用）、1（转换为拼音）、2（转为谐音）），其他输入默认为不使用）：').strip()
        if Chi_choice == '1':
            s = self.Chi_to_Eng(s)
            print('汉语切换后汉语字符转为小写英文，因此不推荐大小写切换')
        if Chi_choice == '2':
            s = self.Chi_Homophony(s)
        swapcase_choice = input('是否选择大小写切换（请输入0(不使用）或1（使用），其他输入默认为不使用）：').strip() # strip用于删除空格
        if swapcase_choice == '1': # 其他输入则均不使用
            s = self.swapcase(s)
        swapcase_choice = input('是否选择我采用的自定义映射，如将m映射为n（请输入0(不使用）或1（使用），其他输入默认为不使用）：').strip()
        if swapcase_choice == '1':
            s = self.word_break(s)
        tonum_choice = input('是否选择字符映射为数字，（请输入0(不使用）或1（使用），其他输入默认为不使用）：').strip()
        if tonum_choice == '1':
            print(f"码长为{len(s)}")
            n = input("请输入要转为数字的字符数目（前n个将被转化为数字），请输入一个大于0但小于原码长度的正整数，其他输入将跳过该功能：")
            s = self.word_to_num(s,n)
        temp_list = list(s)
        leng = len(s)
        print(f"现在码长为{leng}")
        salt_choice = input('是否加入盐值（请输入0(不使用）或1（使用），其他输入默认为不使用）：').strip()

        if salt_choice == '1':  # 其他输入则均不使用
            temp_list.append(self.make_salt())  # 加一个字符到末尾，之后会打乱
            leng += 1
        save_choice = input('是否将结果保存到txt文件（请输入0或1）：').strip()
        # time.sleep(random.uniform(1, 2))  # uniform生成均匀分布浮点数。请原谅，注释掉的这里 我想通过sleep避免水军盗刷（水军应该不会用我这么粗劣的代码吧？）
        # 使用shuffle即可，但我想写出逻辑
        copy = temp_list[:] # 制作一个副本，避免第二个结果是第一个结果基础上继续打乱的。
        result_num = 0
        result_list = {}
        while result_num < result_count:
            temp_list = copy[:]
        # 随机选一个元素，与未交换元素进行对调，直至全部调换位置
            for i in range (leng-1, 0, -1):
               j = random.randint(0, i)
               temp_list[i], temp_list[j] = temp_list[j], temp_list[i]

            result = "".join(temp_list)
            distance = Levenshtein.distance(result,s)
            result_list[result_num] = {result:distance}
            result_num += 1
        if save_choice == '1' :
            self.save(result_list,copy_s)
        print(f'我们看到了一个字典输出，其中生成了{result_count}个结果及其与原码的各自levenshtein距离（即前者到达后者所需做的变换次数）')

        return result_list

v = Voldemort()
s = 'IamTomRiddle'
print(v.disrupt_spell(s))