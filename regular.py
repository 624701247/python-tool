import re

# kone point : 正则的东西看这里


# 两头固定字符，中间不知道啥字符（中间要有字符才能匹配上）
# 替换后的字符串 = (模式字符串, 替换的字符串, 原字符串)
sst = re.sub('(aa).+(bb)', 'xxx', '11aa22bb33')
# print(sst)


# 两头固定字符,中间有一个某字符
sst = re.sub('(aa).(bb)', 'xxx', '00aa1bb00')
# print(sst)


# 两头固定字符,中间有 0个 或 任意n个字符
sst = re.sub('(aa)*(bb)', 'xxx', '00aabb00')
# print(sst)


# 字符 a到z & 0到9 & ! 统统匹配替换
sst = re.sub('[a-z0-9!]', '?', '135agb!')
# print(sst)


# 匹配连续n个某字符
sst = re.sub('(a){2}', '?', 'aabbaaa')
# print(sst)


# re.search 扫描整个字符串并返回第一个成功的匹配。
ssc = re.search('(a).(b)', 'a1ba0000a2b')
# print(ssc)	# 返回的是对象
# print(ssc.group()) # 返回匹配到的字符串


# 尝试从字符串的起始位置匹配一个模式，
# 如果不是起始位置匹配成功的话，match()就返回none。
ssc = re.match('(a).(b)', '000a1ba0000')
# print(ssc)