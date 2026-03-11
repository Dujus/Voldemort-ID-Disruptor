import random


class Voldemort(object):

    def __init__(self,break_dict):

        self.word_dict = {chr(ord('a')+x): x for x in range(0, 26)}

        self.reverse_dict = {b: a for a, b in self.word_dict.items()}
        self.break_dict = break_dict  # {'m':'nn','o':'0','0':'o','l':'1','w':'uu'}，读取json后就不需要在这里硬编码了，可以到config.json里头改

    def make_salt(self):
        """
        制作加入字符串的盐
        :return:
        """
        return self.reverse_dict.get(random.randint(0 , 25)) # 生成一个随机int数,得到一个随机字符.目前加盐还只从字符中选取。今后可能扩大范围或者加入多个盐

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

    def construct_dictionary(self):

        """
        返回正向词典：词（小写）对值（0-25），反向字典，值对词
        :return:
        """
        return self.word_dict, self.reverse_dict

    def disrupt_spell(self, s,leng):
        """
        s:str,原ID号
        :return:
        """
        # shuffle可以实现，但我想写出逻辑
        temp_list = list(s)
        copy = temp_list[:]
        # 随机选一个元素，与未交换元素进行对调，直至全部调换位置
        for i in range (leng-1, 0, -1):

            j = random.randint(0, i)
            copy[i], copy[j] = copy[j], copy[i]

        result = "".join(copy)
        return result


