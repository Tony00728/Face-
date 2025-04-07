import numpy as np
from glob import glob
import os
import requests
from json import JSONDecoder
import cv2
import time
import re
import scipy.io
from glob import glob
from tqdm import tqdm
from PIL import Image
t1=time.time()
http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
key ="dFzKyjLueDIsR-SuzJqTeTht6JJAW2WB"
secret ="rdiulbTwWNL5ZiBaJOzaSDRpBm9792iU"


faceId= []
dataset_name='F:/Lan/dataset/BM/train/61-70/'
f_names = glob(os.path.join('F:/Lan/dataset/BM/train/61-70/', dataset_name, '*.jpg'))
#file_names= f_names1
size_data1 = len(f_names)
print('1:',size_data1)

faceId2= []
dataset2_name='F:/Lan/dataset/BM/train/71+/'
f_names2 = glob(os.path.join('F:/Lan/dataset/BM/train/71+/', dataset2_name, '*.jpg'))
#file_names= f_names1
size_data2 = len(f_names2)
print('2:',size_data2)

f_names1=f_names+f_names2
size_data = len(f_names1)
print('All:',size_data)

name=[]

arr=[]
arr2=[]
for i in tqdm(range(0,len(f_names1))):#enumerate(f_names1):
    f1 = os.path.basename(f_names1[i])
    files = f_names1[i]
    #print(f1)
    #image = cv2.imread(files)
    #print(image)

    data = {"api_key": key, "api_secret": secret, "return_attributes":"age"}
    files = {"image_file": open(files, "rb")}
    response = requests.post(http_url, data=data, files=files)

    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)

    #print(req_dict)
    face_rectangles=[]
    #print(req_dict['faces'][0]['face_rectangle'])
    attributes=[]
    #print(req_dict['faces'][0]['attributes'])


    try :
        for age in req_dict['faces']:

            if 'attributes' in age.keys():
                attributes.append(age['attributes'])
        #print(attributes)
    except KeyError:
        print('continue')
        continue
    for i in attributes:
        age=i['age']
    #    cv2.rectangle(age)
        #print(age)
        age2= age['value']
        #print(age2)
#
        arr2.append(age2)

    time.sleep(0.3)

age2=arr2
#print(a)
print(age2)

mean2=np.mean(age2)
std=np.std(age2)

print('age_mean:',mean2)
print('age_std:',std)



