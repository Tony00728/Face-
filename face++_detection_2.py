import numpy as np
from glob import glob
import os
import requests
from json import JSONDecoder
import cv2
import time
import re
from tqdm import tqdm

t1=time.time()
http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
key ="dFzKyjLueDIsR-SuzJqTeTht6JJAW2WB"
secret ="rdiulbTwWNL5ZiBaJOzaSDRpBm9792iU"


faceId1= []
dataset1_name='F:/Lan/FS-D2AAE/WM/train1/test4/'
f_names1 = glob(os.path.join('F:/Lan/FS-D2AAE/WM/train1/test4/', dataset1_name, '*.png'))
label0=[]
label1=[]
label2=[]
label3=[]
label4=[]
label5=[]
for i in range(0,len(f_names1)):
    #print(f_names1[i])
    label=os.path.splitext(os.path.basename(f_names1[i]))[0].split('_')[-1]
    #print(label)
    if label=='0':
        label0.append(f_names1[i])
    elif label=='1':
        label1.append(f_names1[i])
    elif label=='2':
        label2.append(f_names1[i])
    elif label=='3':
        label3.append(f_names1[i])
    elif label == '4':
        label4.append(f_names1[i])
    elif label == '5':
        label5.append(f_names1[i])

lab0=label0
lab1=label1
lab2=label2
lab3=label3
lab4=label4
lab5=label5
#print(len(lab0),len(lab1),len(lab2),len(lab3),len(lab4),len(lab5))
lab=[lab0,lab1,lab2,lab3,lab4,lab5]
#print(lab)
print(len(lab))
#print(f_names1)

#filepath = "50.png"
#list=['qiyi.jpg','chenduling.jpg','fan.jpg']
#frame=cv2.imread('50.png')

#file_names = glob.glob('D:/Lan/cropAsian2/*')

arr=[]
arr2=[]
for j in range(0,len(lab)):
    #print(lab[j])
    print('lab',j,':')
    for i in tqdm(range(0,len(lab[j]))):
        f1 = os.path.basename(lab[j][i])
        #print('files',files)
        #print('lab[j][i]', lab[j][i])
        files=lab[j][i]
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
        for age in req_dict['faces']:
            if 'attributes' in age.keys():
                attributes.append(age['attributes'])
        #print(attributes)
        for i in attributes:
            age=i['age']
        #    cv2.rectangle(age)
            #print(age)
            age2= age['value']
            print(age2)

            arr2.append(age2)


    if j==0:
        if 11<= age2 <=20:
            a=1
        else:
            a=0
        arr.append(a)
    elif j==1:
        if 21<= age2 <=30:
            a=1
        else:
            a=0
        arr.append(a)
    elif j==2:
        if 31<= age2 <=40:
            a=1
        else:
            a=0
        arr.append(a)
    elif j==3:
        if 41<= age2 <=50:
            a=1
        else:
            a=0
        arr.append(a)
    elif j==4:
        if 51<= age2 <=60:
            a=1
        else:
            a=0
        arr.append(a)
    elif j==5:
        if 61<= age2 <=70:
            a=1
        else:
            a=0
        arr.append(a)

    a=arr
    print(a)
    age2=arr2
    print(age2)
    #print(a)
    #print(age2)
    mean1=np.mean(a)
    mean2=np.mean(age2)
    std=np.std(age2)

    print([j],'accuracy:',mean1)
    print([j],'age_mean:',mean2)
    print([j],'age_std:',std)




        #print(re.findall(r'\d+',age))

    # print('运行时间是{}'.format(time.time()-t1))
    #cv2.imshow('tuxiang',frame)
    #cv2.waitKey(1)

    #time.sleep(10)
