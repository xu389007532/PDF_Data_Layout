from pandas import read_excel
import os

# 指定文件夹路径
folder_path = r'D:\xu\Python\PDF_Data_Layout\DATA'

# 扫描文件夹
total=0
for filename in os.listdir(folder_path):
    # print(filename)
    xls = read_excel(folder_path+"/"+filename)
    print(xls.shape[0],filename)
    total=total+xls.shape[0]
    # va = xls.values[0][0]

    # for p, v in enumerate(va):
    #     print(p,v)
print(total)