#-------1 调用函数--------略
#--------2 定义函数-------格式：函数头 def name（）：+函数体：想要实现的功能
# def say_my_name():
#     print("储浩楠")#此为函数内的
# # print("chn")#不属于上面的函数，属于外部代码
# say_my_name()#调用成功，必须放在函数之后调用
# def make_friend():
#     say_my_name()#我们可以在函数中使用我们已经定义好的函数，就像使用print函数一样
#     print('good')
# make_friend()


#--------------3 函数的参数---------def name(a ,b ,c,d):
# def line(width,a):
#     '''width代表你想要线的宽度  
#     a代表你想要线的种类'''#通过‘’‘可以对所定义的函数添加说明，太简单了
#     print(width*a)
# line(5,"$")
# line(17,"储")
# line(5,6)


#-------------4函数的返回值--------return ：1将函数执行后的值返回到调用函数的地方，2结束函数的运行，一个函数可以有多个返回值，一个返回值可以返回多个数据。
# def get_max(a,b):
#     max_=b
#     if a>b:
#         max_=a
#     return max_#返回函数值，并且终止语句
#     print("666")#这句不会被执行，因为他在return的后面
# i=get_max(55,57)
# print(i)

#return可以在一个函数中配合条件语句多次使用
# def age_fun(age):
#     if age<=0:
#         return None
#     if type(age)!= int:
#         return #return 与return none一个效果，都是返回空值
#     print(age)
# age_fun(5)
# age_fun(-1)
# age_fun(16.6) 

#return可以返回多个值，此时要调用时就要有足够的参数与其对应，要么就只给一个参数，系统会自动生成元组touple
# def func(a,b):
#     return a+b, a-b,a*b
# i,j,k=func(5,6)
# print(f"i={i},j={j},k={k}")#此处的print（f）与format函数类似，不加的话，打印不出来值
# z=func(5,6)
# print(z)#只给一个输出端口的话，就会显示一个元组，不是列表


#practice----------5.练习-----编写一个日历————————------计算星期几的公式：（d+2*m+3*(m+1)//5+y+y//4-y//100+y//400）%7+1        ://表示取整，若月份为1，2则年份减一，月份变为13 或14
# def y_m_d_to_week(y,m,d):

#  '''跟据年月日给出星期几 '''
#  y-=1 if m==1 or m==2 else y#常用的结构：表达式1  if 判断语句   else 表达式2
#  m=13 if m==1 else(14 if m==2 else m)#if的多层嵌套，非常滴高端大气
#  w=(d+2*m+3*(m+1)//5+y+y//4-y//100+y//400)%7+1
#  return w
# def is_leap_year(y):
#     '''判断一个年份是否是闰年'''
#     if y%400==0 or (y%4==0 and y %100!=0):#判断条件：如果一个数可以被四百整除，或者可以被4整除，但是不能被100整除，那么这个年份就是闰年
#            return 29 
#     return 28
# def get_days_from_month(m,y):
#     '''计算某一个月内有多少天'''
#     if m in [1,3,5,7,8,10,12]:
#         return 31
#     elif m in[4,6,9,11]:
#         return 30
#     else:
#         return is_leap_year(y)
# '''用户输入年月'''  
# # year=int(input("请输入年份:"))
# # month=int(input("请输入月份:"))
# year,month=2022,11
# days= get_days_from_month(month,year)
# print("一 二 三 四 五 六 日")
# print("--------------------")
# for i in range(1,days+1):
#     w= y_m_d_to_week(year,month,i)
#     if i==1:
#         print(f"{''*(w-1)*3}",end="")#重新定义一号打印的位置
#     else:
#             if w ==1:#判断如果这一天是周一
#                 print("")#是周一则换行
#     print(f"{i:2d}",end=" ")#将end设置为空，打印时不自动换行，用f"{i:2d}"保证打印的i所占为2，不然1和16这种占的地方不一样
# print("")#保证在for循环结束的时候换行

#---------------6 变量的作用域-----------全局（global）与局部（local）
#全局变量在函数内可以使用但是不能修改，如果想在函数内修改变量的值，则需要使用global关键字
# i= 5
# def func():
#     '''这是一个注释'''
#     global i
#     i=0
# func()
# print(i)#此处我们成功修改了函数的值
# print(func.__name__)#打印函数的名字
# print(func.__doc__)#打印函数的注释


#-----------------7参数扩展---------1关键词参数  2 默认值参数   3   形参和实参     
# def information(name,age=0):#age=0,为默认值参数，当我们输入时他就为我们的输入，当我们没有输入时，系统默认为0 ，且默认值只能设置在最后一个参数上
#     print(f"名字={name},年龄={age}")
# information("小明",18)
# information("小红")
# information("xiaohao")

# def f(a,b=4,c=9):
#     print(a,b,c)
# f(a=1,b=2,c=3)#这里直接按照名称传递参数，叫做关键词参数，如果中间某个变量使用了关键词参数，则后面的也需要使用关键值变量来赋值
# f(12,4,5)
# f(12,c=8)#记住了，默认值参数不能时最后一个，但是可以有多个，关键词参数可以跳跃式赋值

#形参（parameter）与实参（argument）  定义参数时，参数a叫做形式参数  
# def f(a):#这里a为形式参数
#     print(a)
# f(12)#a =12 传递参数时会用实际参数给形式参数赋值。

#--------------08可变参数---------可以传递任意数目的参数   *name   得到的是元组
#如：
# def get_sum(a,b,c):
#     return a+b+c
# t = get_sum(1,2,3)
# print(t)
#如果想用以上函数求解四个数，甚至更多说的和，那么我们还得修改我们的函数，此时我们可以引入可变参数*name来解决这个问题
# def get_sum1(*args):#同一个函数最多只能定义一个可变参数。但是可以与普通的参数一起定义a，*args
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# t1=get_sum1(1,2,3,4,5,6,6,78,)#可变参数变得不仅仅可以是数据的数目，也可以是类型
# print(t1)
#t2=get_sum1(a=1,b=2)#可变参数之前的参数不允许进行关键词赋值，会报错，但是可变参数之后的可以使用关键词赋值
# def f(a,b,*c,d,e):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
# f(1,2,3,4,5,6,d=7,e=8)#a,b依次获得1，2，在可变参数之后使用关键词赋值，分别赋给d，e为7，8即可变参数之前只能顺序赋值，之后只能关键词赋值




#--------------9 可变关键词参数------------**name   只能通过关键词进行赋值，得到的是字典   使用时要确保出现在定义的最后面
# def f(**a):
#     print(a)
# f(name='cxh',shengao=185,tizhong=140)#结果是一个字典，三个对
# def f(a,*b,**c):
#     print(a)
#     print(b)
#     for m ,n in c.items():#调用字典与调用元组不一样，需要加.items()表示键值对，  .key()表示仅对键    .value（）表示仅对值
#         print(f'{m}:{n}')
# f(1,2,3,4,name='cxh',shengao=185,apperance='handsome')


#---------------10.元组的解包---------很多类型都能解包，比较简单，不再赘述了
#将元组中的元素拆开的过程称为元组解包
# a,b,*c,d=(1,2,3,4,5,6,7,8,9)#只能有一个带*的参数
# print(a)
# print(b)
# print(c)#    *c代表可以存在多个元素
# print(d)#最后一个给d

# def f(a,b,c):
#     print(a,b,c,sep='--')
# l=[1,2,3]
# f(*l)#快速对数组进行解包，使用*的前提是元素数要相同，若将def f（*a）则对l中的数据多少就无要求了




#--------------------11.函数类型的参数----------------一个函数也可以作为另外一个函数的参数来使用
# import datetime   #导入一个定时数据包
# def time(t,start, finished):
#     t1=datetime.datetime.now()
#     if start!=None:#这里判断start非空也可以写成 if start（）
#         start()
#     while True:
#         t2=datetime.datetime.now()
#         delta_t=t2-t1
#         if delta_t.seconds >=t:
#             break
#     if finished:
#         finished()
# def f():
#     i= int(input('请输入数字:'))
#     print(i)
# def s():
#     print('请稍等')
# time(2,s,f)



#------------12高阶函数-------------函数的特殊使用方式,嵌套，作为参数来使用，作为返回值来使用----
# def f():
#     def fn():#创建fn函数，打印fn
#         print('fn')
#     return fn#在函数内部定义了一个新函数，此处加return用于返回外界  
# a=f()#迭代一次函数
# a()

#实现一个计数器：
# count=5
# def f():
#     global count
#     count-=1
#     if count<0:
#         return
#     return count
# print(f())
# print(f())
# print(f())


#------------12.函数递归-------------
#函数内部可以调用其他函数，如果一个函数在内部调用自身本身，这个函数就是递归函数
#-----递归实现阶乘
# def  fun_(n):
#     if n == 1:
#         return 1 
#     return n*fun_(n-1)
# i = fun_(1000)#递归1000时，栈溢出：maximum recursion depth exceeded
# print(i)


