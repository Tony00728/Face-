from tqdm import tqdm
import time
from skimage.measure import compare_ssim, compare_psnr, compare_mse
import requests
from json import JSONDecoder
import cv2
from glob import glob
import os
import numpy as np
faceId1= []
dataset1_name='F:/Lan/classification/test_dataset_class2/BM/'
f_names1 = glob(os.path.join('F:/Lan/classification/test_dataset_class2/BM/', dataset1_name, '*.jpg'))
#print(f_names1)


faceId2=[]
dataset2_name='F:/Lan/FS-D2AAE/BM/train_yesD2_noloss/test_all/'
f_names2 = glob(os.path.join('F:/Lan/FS-D2AAE/BM/train_yesD2_noloss/test_all/', dataset2_name, '*.png'))
# print(f_names2)
# fa1 = os.path.basename(f_names1)
# print(fa1)
arr=[]
arr2=[]
arr3=[]

for i in tqdm(range(0,len(f_names1))):
    f1_1 = os.path.basename(f_names1[i])
    f1 = os.path.splitext(f1_1)[0]
    #print('f1', f1)
    #print('f1__', f_names1[i].split('\\')[-1])
    try:
        if 'F' in f_names1[i].split('\\')[-1] and not 'chip' in f_names1[i].split('\\')[-1]:  # for Black and White

            label_age = int(str(os.path.splitext(f_names1[i].split('\\')[-1].split('F')[-1])[0]))

        elif 'M' in f_names1[i].split('\\')[-1] and not 'chip' in f_names1[i].split('\\')[-1]:

            label_age = int(str(os.path.splitext(f_names1[i].split('\\')[-1].split('M')[-1])[0]))
        elif 'M' and 'chip' in f_names1[i].split('\\')[-1] and not 'F' in f_names1[i].split('\\')[-1]:

            label_age = int(os.path.split(f_names1[i].split('\\')[-1])[-1].split('M')[-1][0:2])
        elif 'F' and 'chip' in f_names1[i].split('\\')[-1] and not 'M' in f_names1[i].split('\\')[-1]:

            label_age = int(os.path.split(f_names1[i].split('\\')[-1])[-1].split('F')[-1][0:2])

        elif 'chip' in f_names1[i].split('\\')[-1] and not 'M' in f_names1[i].split('\\')[-1] and not 'F' in \
                f_names1[i].split('\\')[-1]:

            label_age = int(os.path.split(f_names1[i].split('\\')[-1])[-1].split('_')[0])
        elif f_names1[i].split('\\')[-1][0:2]=='0_'or f_names1[i].split('\\')[-1]=='1_':
            label_age = int(os.path.split(f_names1[i].split('\\')[-1])[-1].split('_')[2])
            #print('age',label_age)


        #print(label_age)

        if 11 <= label_age <= 20:
            label = 0
        elif 21 <= label_age <= 30:
            label = 1
        elif 31 <= label_age <= 40:
            label = 2
        elif 41 <= label_age <= 50:
            label = 3
        elif 51 <= label_age <= 60:
            label = 4
        elif 61 <= label_age <= 70:
            label = 5

        #print('label', label)

        f4=f1+'_'+str(label)
        #print('f4', f4)
        img1 = cv2.imread(f_names1[i])
        for i in range(0,len(f_names2)):
            f2_2 = os.path.basename(f_names2[i])
            f2 = os.path.splitext(f2_2)[0]
            #print('f2', f2)
            if f4==f2:
                f3=f2[:-2]
                print('true',f1,f4)
            else:
                continue
            img2 = cv2.imread(f_names2[i])
            f = "{}/{}".format("F:/Lan/FS-D2AAE/BM/train_yesD2_noloss/", "test_all_same")
            # print("f",f)
            path = os.path.splitext(f4)
            print(path)
            cv2.imwrite("{}/{}.jpg".format(f, path[0]), img2)


    except ValueError:
        continue

