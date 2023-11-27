import os
import csv
import json

'''常用的文件格式转换基本都有成熟的库
此处写一些不常用到的，可能是我思想愚笨
'''

def file_process(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension.lower() =='csv':
        a=1
        #进一步拓展

def csv_to_json(file_path):
    csv.field_size_limit(2147483647)#设定容量上限，不然会报错此处为2GB
    data = []
    with open(file_path,'r',encoding='utf-8') as f:
        csv_res = csv.DictReader(f)
        for row in csv_res:
            data.append(row)

    #保存为多行json
    save_json_file_path =r''
    with open(save_json_file_path ,'w',encoding='utf-8') as jsonf:
        json.dump(data,jsonf,indent=4,ensure_ascii=False) #防止中文乱码


    #保存为单行字典json：需要有多行字典文件
    merge_list=[]
    with open(save_json_file_path,'r',encoding='utf-8') as f:
        dict_list = json.load(f)#load保存下来就是字典格式
        for dict in dict_list:
            merge = ','.join([f'{key}:{value}' for key ,value in dict])#将字典连接
            merge_list.append(merge)
        a=merge_list

    oneline_json_path = r''
    with open(oneline_json_path,'w',encoding='utf-8')as onef:
        json.dump(a,onef,indent=4,ensure_ascii=False)
    return oneline_json_path









