import os
# import numpy
import json
# from pandas import DataFrame
from konlpy.tag import Okt
from pprint import pprint
# from matplotlib import pyplot

path = "./data"

intG = 0
intN = 0
intB = 0

# 명사, 동사, 형용사, 부사 등 의미있는 단어를 남긴다.
okt = Okt()
def str_filter(review):
    str_result = ""
    for t in okt.pos(review, norm=True, stem=True):
        if (t[1] =="Josa" or t[1] == "Punctuation"):
            str_result = str_result
        else:
            str_result = str_result + " " + t[0] 
    return str_result

# read files
obj_file = open(path+"/"+"ratings_train.txt",'r', encoding="utf-8")
lines = obj_file.readlines()
print (lines[0])

write_file = open(path+"/"+"ratings_josa.txt",'a',encoding="utf-8")
for t in lines:
    checkdata = t.split('\t')
    checkdata[1].replace(",","")
    str_obj = checkdata[0] + "\t" + str_filter(checkdata[1]) + "\t" + checkdata[2]
    write_file.write(str_obj)
