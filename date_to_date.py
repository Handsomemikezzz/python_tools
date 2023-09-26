import xlrd
import re 
import pandas as pd
# xlrd为1.2.0版本时可同时处理xls 与xlsx文件

filepath = 'your file path'
wb = xlrd.open_workbook(filepath)
ws= wb.sheet_by_name('Sheet1')

pattern = r'^[45]\d{4}$'#用于匹配五位整数


#日期到日期序列转换函数：
def data(para):
    delta = pd.Timedelta(str(para)+'days')
    time = pd.to_datetime('1899-12-10')+delta
    return time

#判断转换后的日期是否正常，及对转换后的日期按需求进行处理
def date_parse(cell_value):
    cell_value_date=data(cell_value)
    try:
        date = cell_value_date
        date = date.replace(hour = 0 ,minute = 0 ,second = 0 )# 此处可以不将时分秒置零
        year_last_two = int(date.strftime("%y"))#. %y表示读取年份的后两位，%Y表示读取年份的全部位数
        if year_last_two ==23 or year_last_two ==24:#此处只希望保留23年或24年的日期
            return date.strftime("%Y-%m-%d %H-%m-%s")#返回时间
        else:
            return cell_value
    except ValueError:
        return cell_value

# 遍历单元格，修改符合条件的元素:
for row in range(ws.nrows):
    for col in range(ws.ncols):
        cell = ws.cell(row, col)
        cell_value = cell.value
        ctype = cell.ctype#由于读取的日期为数字，所以此时在表格属性中数字对应的ctype为2
        if type == 2 :
            match =re.search(pattern, str(int(cell_value)) )
            if match:#若其属性为2，表格内的值为一个五位整数，则对其进行日期转换
                cell_value = date_parse(cell_value)
                print(cell_value)




