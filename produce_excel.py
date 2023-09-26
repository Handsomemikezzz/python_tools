import os 
import json
import pandas as pd

#------遍历文件夹，获取文件夹下的所有以json后缀结尾的文件------并将其值存在一个excel中
#创建文件夹
result_df = pd.DateFrame(columns = ['name1','age','date'])
folder = 'your_fold_path'

#读取子文件夹
subfolders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder,f)) ]

for fold in subfolders:
    fold_path = os.path.join(folder,fold)
    json_files = [f for f in os.listdir(fold_path) if f.endswith('.json')]

    for json_file in json_files:
        json_file_path = os.path.join(fold_path,json_file)
        with open(json_file_path,'r',encoding = 'uff-8') as file:
            json_str = file.read()
            json_content = json.loads(json_str)
            
            for item in json_content:
                value1 = item['name']
                value2 = item['age']
                value3 = item['date']
            #将数据存为df形式
                result_df = result_df.append({'文件名':fold,'name':value1,'age':value2,'date':value3})
#将df转为excel
result_excel_file = r'希望保存的路径'
result_df.to_excel(result_excel_file,index=False)