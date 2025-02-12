'''
 * @Author       : bpf
 * @Date         : 2020-10-14 22:39:44
 * @Description  : 读取json文件
 * @LastEditTime : 2020-10-14 23:17:48
'''

import json
from pprint import pprint


json_file = "D:/xu/Python/PDF_Data_Layout/config.json"
db_name = "DEFAULT"

with open(json_file, encoding="UTF-8") as f:
    cfg = json.load(f)[db_name]


pprint(cfg)
