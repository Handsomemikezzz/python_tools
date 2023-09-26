import pandas as pd

file_path = r'文件一'
file_path1 = r'文件二'

df = pd.read_excel(file_path)
df1 = pd.read_excel(file_path1)

column_A='name'
column_B = 'age'
column_C = 'date'
column_D = '文件名'

#首先判断文件是否都被读取,采用集合set很方便

set_file_name = set(df[column_D])
set_file_name1 = set(df1[column_D])

#多读取的文件：
added_file_name = set_file_name1 - set_file_name

#没读到的文件
miss_file_name = set_file_name - set_file_name1

#正确读取的文件
correct_file_name = set_file_name&set_file_name1

#打印这些
for add in added_file_name:
    print('多读的文件：',add)
for miss in miss_file_name:
    print('漏读的文件：',miss)


#当文件都被正确读取时，再去比较文件中的其他属性是否正确
error_date=[]
error_name=[]
error_age = []

for idx ,filename in enumerate(df[column_D]):
    for idx1,filename1 in enumerate(df[column_D]):
        if filename == filename1:
            if df[column_B].loc[idx]!= df1[column_B].loc[idx1]:
                print('读取到错误年龄：',str(filename)+':'+str(df1[column_B].loc[idx1]))
            if df[column_C].loc[idx]!= df1[column_C].loc[idx1]:
                print('读取到错误日期：',str(filename)+':'+str(df1[column_C].loc[idx1]))
            if df[column_A].loc[idx]!= df1[column_A].loc[idx1]:
                print('读取到错误名称：',str(filename)+':'+str(df1[column_A].loc[idx1]))

print('比较完毕')
            
            
            