'''添砖加瓦-练习四-在myreverse模块中添加新函数'''

# 递归法反向输出字符串
def reverse_str(s):
    if s == '':
        return ''
    else:
        return reverse_str(s[1:])+s[0]

# 迭代法反向输出字符串
def reverse_str2(s):
    n=''
    if s == '':
        return ''
    else:
        for i in s:
            n=i+n
        return n
