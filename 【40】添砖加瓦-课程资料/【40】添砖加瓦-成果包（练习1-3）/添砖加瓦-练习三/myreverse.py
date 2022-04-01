'''添砖加瓦-练习三-在myreverse模块中添加新函数'''

# 递归法反向输出字符串
def reverse_str1(s):
    if s == '':
        return ''
    else:
        return reverse_str1(s[1:])+s[0]

# 迭代法反向输出字符串
def reverse_str2(s):
    for i in range(len(s)-1, -1 , -1):
        s += s[i]
    return s[(len(s)//2):]

