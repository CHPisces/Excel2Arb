# -*- coding: utf-8 -*-

import pandas as pd
import json
import os
import shutil
import sys

# 读取excel文件
if len(sys.argv) < 2:
    print("请传入Excel文件路径")
    sys.exit(1)

excel_path = sys.argv[1]
df = pd.read_excel(excel_path)

# 删除已存在的output文件夹
if os.path.exists("output"):
    shutil.rmtree("output")
    
os.mkdir("output") 

# 将每一列导出为一个json文件
for col in df.columns[1:]:
    result = {"@@locale": col}
    for index, row in df.iterrows():
        key = row[0]
        value = row[col]
        if pd.isna(value):
            value = ""
        result[key] = value
    with open(f'output/{col}.json', 'w') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)  # 导出json文件
    os.rename(f'output/{col}.json', f'output/intl_{col}.arb')
