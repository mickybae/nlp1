import os
import numpy
import json
from pandas import DataFrame
from matplotlib import pyplot

path = "./data/raw"
file_list = os.listdir(path)
arr_file_list = (file_list)
write_file = open(path+"/"+"001_train.txt",'a',encoding="utf-8")
intG = 0
intN = 0
intB = 0
# read files
for file_name in arr_file_list:
    obj_file = open(path+"/"+file_name,'r',encoding="utf-8")
    obj_json = json.loads(obj_file.read())
    for checkdata in obj_json:
        checkdata['review'].replace(",","")
        if int(checkdata['rating']) > 6:
            str_obj = checkdata['review_id'] + "," + checkdata['review'] + "," + "1" + "\n"
            intG = intG + 1
        elif int(checkdata['rating']) > 3:
            str_obj = checkdata['review_id'] + "," + checkdata['review'] + "," + "0" + "\n"
            intN = intN + 1
        else:
            str_obj = checkdata['review_id'] + "," + checkdata['review'] + "," + "-1" + "\n"
            intB = intB + 1
        
        write_file.write(str_obj)
        print("%d,%d,%d"%(intG, intN, intB))


