import addressparser as addr
import jieba

'''对于部分指代不明的可以通过try except语句跳过,
addressparser中用到函数pandas  有可能index报错'''
line = ['蜀山区','颍州区']

df = addr.transform(line)
print(df)
res_list = df.values.tolist()
print(res_list)
