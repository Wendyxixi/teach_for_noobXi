'''
Author: CC-TSR
Date: 2021-01-06 21:05:06
LastEditTime: 2021-01-06 22:33:25
LastEditors: xiejiancheng1999@qq.com
Description: 
FilePath: \teach_for_noobXi\cal.py
可以输入预定的版权声明、个性签名、空行等
'''


# 计算器 输入： 需要计算什么， 需要用什么计算
#        输出： 计算结果
def wendyFirstSoft(numbers, method):
    result = 0
    if(method == "+" ):
        for number in numbers:   
            result = result + number

    if(method == "-"):
        result = 0
        for number in numbers:   
            result = result - number
    
    
    if(method == "*" ):
        result = 1 
        for number in numbers:   
            result = result + number

    ''' 
    初始值其实是啥固定的数字都不对
    初始值应该得是第一个输入的数字
    我们怎么判断For 循环的第一次运行 并把数值赋给结果，并跳过运算
     '''
    if(method == "/"):
        result = 1
        计数器 = 0
        for number in numbers: 
            计数器 +=1  
            if(计数器== 1):
                result = number
                continue
            # break 跳出所有
            # continue 跳一次
            result = result / number
             
            print(计数器) 
    return result

if __name__ == '__main__':
   wendyFirstSoft([1,2,45,4], '/')
    
