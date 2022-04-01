'''添砖加瓦-练习三'''

#导入myreverse模块
import myreverse

#调用myreverse模块中的两个函数
msg = input('请输入字符串：')
print('递归算法：', myreverse.reverse_str1(msg))
print('迭代算法：', myreverse.reverse_str2(msg))
