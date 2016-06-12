#!/usr/bin/env python
#coding:utf-8
__author__ = '李晓波'
import re

def compute_mul_div(arg): #用于过滤内容中的乘除部分并计算。
    val = arg[0]
    #mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', val)
    mch = re.search('\d+\.?\d*[\*\/][\+\-]?\d+\.?\d*', val) #匹配第一个数字和*或/和数字,内容格式类似 7.9*29
    if not mch: #匹配不到内容退出函数
        arg[0]
        return
    content = re.search('\d+\.?\d*[\*\/][\+\-]?\d+\.?\d*', val).group()
    #if len(content.split('*'))>1:
    if '*' in content: #如果匹配的内容含有*
        n1, n2 = content.split('*') #用*分割字符串，结果为两部分
        value = float(n1) * float(n2)
    else:
        n1, n2 = content.split('/')
        value = float(n1) / float(n2)
    before, after = re.split('\d+\.?\d*[\*\/][\+\-]?\d+\.?\d*', val, 1) #以匹配内容为分隔符分割一次
    new_str = "%s%s%s" % (before,value,after) #组合新的字符串
    arg[0] = new_str #将新字符串放到原来的列表位置
    compute_mul_div(arg)

def compute_add_sub(arg): #用于计算过滤内容的加建部分并计算。
    while True:
        if arg[0].__contains__('+-') or arg[0].__contains__("++") or arg[0].__contains__('-+') or arg[0].__contains__("--"):#如果arg[0]包含指定字符串
            arg[0] = arg[0].replace('+-','-')
            arg[0] = arg[0].replace('++','+')
            arg[0] = arg[0].replace('-+','-')
            arg[0] = arg[0].replace('--','+')
        else:
            break
    val = arg[0]
    mch = re.search('[\+\-]?\d+\.?\d*[\+\-]\d+\.*\d*', val)
    if not mch:
        return
    content = re.search('[\+\-]?\d+\.?\d*[\+\-]\d+\.*\d*', val).group() #匹配出第一个含有运算符或没有运算符的数字和有运算符数字
    content_sign=re.search('[\+\-]?\d+\.?\d*([\+\-])\d+\.*\d*', val).group(1) #主要是提取出类似-2+3中的第二个运算符
    if '+' == content_sign: #如果第二个运算符为+
        n1, n2 = content.split('+')
        value = float(n1) + float(n2)
    else:
        n1, n2 = content.split('-')
        value = float(n1) - float(n2)

    before, after = re.split('[\+\-]?\d+\.?\d*[\+\-]\d+\.*\d*', val, 1)
    new_str = "%s%s%s" % (before,value,after)
    arg[0] = new_str
    compute_add_sub(arg)

def compute(expression):#操作乘除加减总函数
    inp = [expression]#将表达式放入列表
    compute_mul_div(inp) #计算乘除
    compute_add_sub(inp) #计算加减
    result = float(inp[0]) #将结果转换成浮点型
    return result

def exec_bracket(expression): #用于过滤表达式，并调用计算函数
    # 如果表达式中已经没有括号，则直接调用负责计算的函数，将表达式结果返回
    #if not re.search('\(([\+\-\*\/]*\d+\.?\d*){2,}\)', expression):
    if not re.search('\(([\+\-\*\/]*\d+\.?\d*){1,}\)', expression): #匹配第一个包含开头和结尾是括号，括号中内容为运算符和数字
        final = compute(expression)
        return final
    content = re.search('\(([\+\-\*\/]*\d+\.?\d*){1,}\)', expression).group()# 过滤第一个只含有操作符和数字/小数的括号
    before, nothing, after = re.split('\(([\+\-\*\/]*\d+\.?\d*){1,}\)', expression, 1)# 分割表达式,分割更三部分
    print 'before：',expression
    content = content[1:len(content)-1] #将过滤出的结果去除括号
    ret = compute(content) #计算过滤内容的结果
    print '%s=%s' %(content, ret)
    expression = "%s%s%s" %(before, ret, after) #拼接字符串
    print 'after：',expression
    print "="*10,'上一次计算结束',"="*10
    # 循环继续下次括号处理操作，本次携带者的是已被处理后的表达式，即：
    return exec_bracket(expression)
inpp='1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
inpp = re.sub('\s*','',inpp) #去除表达式中的空字符
print exec_bracket(inpp)


