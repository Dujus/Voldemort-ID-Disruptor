Voldemort ID Disruptor 
<details> 
”他轻声说：“伏地魔……是我的过去、现在和未来，哈利·波特……”
他举起哈利的魔杖，在空中挥了一下，那些字母重新排列，变成了：我是伏地魔（I AM LORD VOLDEMORT）。”
</details> 
在社交媒体高度发达的今天，专家劝我们不要在不同的社交媒体平台使用相似的ID。受《哈利波特》系列的启发，Voldemort ID Disruptor 是一个轻量级的 简单ID 混淆与生成工具。它旨在通过多种字符处理逻辑（包括大小写切换、自定义映射（m-nn)、数字转化及盐值添加），为字符串生成具有高随机性的变体。特别适用于简单混淆对象字符及进行兴趣教学场景。目前，它适配中英文ID。

基于python 实现，依赖库如下：
pip install -r requirements.txt
使用时，您可以在‘config.json'中自定义您的映射，在main.py中，s的值即为您所希望混淆的ID。它将以字符串格式输入。result_count为生成结果数目。运行 python main.py ，按照屏幕提示输入是否应用特定功能后，得到要求个数相应打乱后ID。 
结构为：VoldemortProject/
├── main.py        # 入口文件

├── RiddleCore.py        # 核心模块，包含 Voldemort 类及算法

├── utils.py             # 工具模块，含简单辅助函数

├── config.json          # 配置文件：存储我自定义的映射规则

├── requirements.txt     # 依赖列表

└── README.md            
若采用了保存功能，产生result.txt文件

Voldmort.py则是我最初创建该项目未进行拆分时的脚本文件，它也可以单独运行。

一次执行案例如下：
原码为IamLordVoldemort

是否选择大小写切换（1为使用，其他输入默认为不使用）:1

是否选择我的自定义映射，如m映射为nn，(1为使用，其他输入默认为不使用):1

是否选择字符映射为数字(1为使用，其他输入默认为不使用):1

目前码长为16

请输入转化字符数目（前n个将被转化为数字），请输入一个大于0但小于原码长度的正整数，其他输入将跳过该功能：:1

是否加入随机字母盐值(1为使用，其他输入默认为不使用):2

是否将结果保存到txt文件（请输入0或1）：1

成功录入result.txt！

我们看到了一个字典输出，其中生成了5个结果及其与原码的各自levenshtein距离（即前者到达后者所需做的变换次数）

{0: {'DLOTOR18vMOERDAM': 13}, 1: {'1LORMDREOvMAOTD8': 14}, 2: {'DLTRMEOA1R8vMOOD': 14}, 3: {'OR8DAvLMRDE1TOOM': 13}, 4: {'1RMOM8TOLAOEDvRD': 11}}


<details> 
原码为IamTomRiddle
是否选择汉语切换（请输入0(不使用）或1（使用），其他输入默认为不使用）：
是否选择大小写切换（请输入0(不使用）或1（使用），其他输入默认为不使用）：
是否选择我采用的自定义映射，如将m映射为n（请输入0(不使用）或1（使用），其他输入默认为不使用）：
是否选择字符映射为数字，（请输入0(不使用）或1（使用），其他输入默认为不使用）：
现在码长为12
是否加入盐值（请输入0(不使用）或1（使用），其他输入默认为不使用）：
是否将结果保存到txt文件（请输入0或1）：1
成功录入result.txt！
我们看到了一个字典输出，其中生成了6个结果及其与原码的各自levenshtein距离（即前者到达后者所需做的变换次数）
{0: {'edlodmRimaTI': 9}, 1: {'edoRimIalmTd': 11}, 2: {'TddemomIaRil': 10}, 3: {'RTemdIolmaid': 10}, 4: {'edImamdoiTlR': 9}, 5: {'loTmemddaIRi': 10}}
</details> 

Disclaimer:
本项目仅供学术研究、兴趣爱好、个人学习及简单的安全测试使用。

严禁滥用：严禁将本项目用于任何形式的自动化注册、批量生成虚假 ID、垃圾邮件制造、网络暴力、网络攻击或其他违反目标平台服务条款及相关法律法规的行为！！！

责任归属：采用 GNU General Public License v3.0协议。使用者应对使用本项目产生的任何后果承担全部责任，开发者不对因滥用本项目而导致的任何法律诉讼、经济损失或服务违规负责。本代码的混淆效果简单，不适合应用于严肃的、工业化的、真正的’加密‘场景。且请注意，该项目的‘原ID到结果ID’是单向的，用后不依赖统计工具仅凭肉眼难以还原，在破坏前最好记住原ID。

本代码是我作为python菜鸟上传的第一个兴趣项目，经验不足，一定还有很多疏漏、粗糙、不足之处，恳请各位大佬多多批评指正。若有不当，请轻喷。
最近clones增多，似乎是爬虫的功劳。若您是受益于项目的人且感兴趣它未来进展，请点一个watch或star吧，这对我很重要！😙
未来’大饼‘计划：适配中文（映射为拼音,已实现）、自动化项目（如移除input交互）、用户自定义自由度提升（如自己定义生成几个ID，已实现）、更精细函数功能等等，敬请期待……
非常欢迎各位开发者提交 Issue 或 Pull Request，共同完善项目。您的建议是我进步的动力！

Voldemort ID Disruptor 

"He said softly, 'Voldemort... is my past, present, and future, Harry Potter...'"
He waved Harry's wand in the air, and the letters rearranged themselves into: ‘I AM LORD VOLDEMORT’.

In today's highly connected digital world, experts advise against using similar IDs across different social media platforms. Inspired by the *Harry Potter* series, the 'Voldemort ID Disruptor' is a lightweight ID obfuscation and generation tool. 

It generates high-randomness variants of strings using various character manipulation logic, including case swapping, custom mapping (e.g., 'm' to 'nn'), numeric conversion, and salt addition. This project is intended for simple character obfuscation and educational purposes. 

Hint: Currently optimized for English IDs. Chinese ID support is experimental and under development.*

 Getting Started

 Prerequisites
You need Python installed on your system. Install the required dependencies:

```bash
pip install -r requirements.txt

Customize your mapping rules in config.json.

Run the program:

Bash
python main.py
's' in the main.py is the ID you hope to input it.It is a string. 
Follow the on-screen prompts to apply specific transformation functions（input number '1' means applying the function.While all other inputs means not applying it). The tool will output 5 distinct, obfuscated variants along with their Levenshtein distance relative to the original ID.
VoldemortProject/
├── main.py              # Entry point
├── RiddleCore.py        # Core module containing the Voldemort class and algorithms
├── utils.py             # Utility module with helper functions
├── config.json          # Configuration file for custom mapping rules
├── requirements.txt     # Dependency list
└── README.md
While Voldemort.py is the original monolithic script created before refactoring. It remains functional and can be run independently.(the same result as the project)

Disclaimer
Usage Policy: This project is intended for academic research, personal interest, and basic security testing.
I use GNU General Public License v3.0 for this project.
Prohibited Use: Any form of automated registration, mass generation of fake IDs, spam creation, cyber-bullying, cyber-attacks, or any other use that violates platform terms of service or applicable laws is strictly prohibited.

Liability: The user assumes all responsibility for any consequences arising from the use of this project. The developer is not liable for any legal action, economic loss, or service violations resulting from the misuse of this project. This code provides simple obfuscation and is not suitable for serious, industrial-grade, or professional cryptographic applications.

About
This is my first hobby project as a Python learner. There are certainly areas for improvement, and I welcome all constructive criticism and feedback.
Future Roadmap(perhaps):

Support for Chinese character mapping (Pinyin)(finished).

Automation (e.g., removing input() interactions,(finished)).

Advanced user-defined configurations.

Code refactoring and function optimization.
Contributions are highly welcome! Feel free to submit an Issue or a Pull Request. 
Recently, there has been an increase in clones, which seems to be attributed to crawlers. If you are someone who benefits from my early project and is interested in its future progress, please click on a watch or star, it is important to me! 😙
