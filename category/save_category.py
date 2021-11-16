
from category_classifier import *
import sys
import time



text_datas = str(sys.argv[1])[7:]
name = str(sys.argv[2])[6:]

# text_datas = text_datas.replace('  ', '')

category_data = push_this_button(text_datas)[0]['subclass']
# [0]['subclass'].encode(encoding='ISO-8859-1',errors='strict').decode(encoding='UTF-8',errors='strict')

with open(f'category/temp/{name}.txt', "w") as f:
    f.write(category_data)