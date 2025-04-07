import requests
from json import JSONDecoder
import cv2
from glob import glob
import os
import numpy as np
from tqdm import tqdm
import time
compare_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
key ="dFzKyjLueDIsR-SuzJqTeTht6JJAW2WB"
secret ="rdiulbTwWNL5ZiBaJOzaSDRpBm9792iU"


faceId1= []
# dataset1_name='F:/Lan/face_aging_with_CycleGan-master/WF/11-20to61-70/testFGNET/'
# f_names1 = glob(os.path.join('F:/Lan/face_aging_with_CycleGan-master/WF/11-20to61-70/testFGNET/', dataset1_name, '*.jpg'))

dataset1_name='F:/Lan/FGNET_test/test/41-50/'
f_names1 = glob(os.path.join('F:/Lan/FGNET_test/test/41-50/', dataset1_name, '*.png'))






faceId2=[]
dataset2_name='F:/Lan/FGNET_test/crop/F/41-50/'
f_names2 = glob(os.path.join('F:/Lan/FGNET_test/crop/F/41-50/', dataset2_name, '*.jpg'))
#print(f_names2)
# fa1 = os.path.basename(f_names1)
# print(fa1)
arr=[]
arr2=[]

for i in tqdm(range(0,len(f_names1))):    #enumerate(f_names1):
    #print('faceId1',faceId1)
    faceId1=f_names1[i]
    f1_1= os.path.basename(f_names1[i])
    # print('f1_1',f1_1)
    f1=f1_1.split('A')[0]
    # int(str(os.path.splitext(sample_files[i].split('\\')[-1].split('F')[-1])[0]))
    # print(f1)
    # print(faceId1)

    for i,faceId2 in enumerate(f_names2):
        #f2 = os.path.basename(f_names2[i])
        f2_2 = os.path.basename(f_names2[i])
        f2 = f2_2.split('A')[0]
        # print(f2)
        # label = (os.path.splitext(os.path.basename(f_names2[i]))[0])[-1]
        # #print(label)
        # if label=='5':
        #     f3=f2[:-2]
        # else:
        #     continue
        # #print(f3)
        # #print(f2)
        # #print(faceId2)
        if f1==f2:
            print(f1_1,',',f2_2)
            data = {"api_key": key, "api_secret": secret}
            files = {"image_file1": open(faceId1, "rb"), "image_file2": open(faceId2, "rb")}
            #print("files",files)
            response = requests.post(compare_url, data=data, files=files)

            req_con = response.content.decode('utf-8')
            req_dict = JSONDecoder().decode(req_con)
            #print(f1,f2)
            #print(req_dict)
            try:
                confindence = req_dict['confidence']
                #print(confindence)
            except:
                continue


            arr.append(confindence)
            time.sleep(1)

confindence=arr
print(confindence)
mean=np.mean(confindence)
print('mean',mean)
std=np.std(confindence)
print('std',std)





# faceId2=[]
# dataset2_name='D:/Lan/CAAEtest/facetest2/'
#
#
# faceId1 = "chenduling.jpg"
# faceId2="chendulingrea.jpg"
# data = {"api_key": key, "api_secret": secret}
# files = {"image_file1": open(faceId1, "rb"), "image_file2": open(faceId2, "rb")}
# #files = {"image_file1": open(glob(os.path.join('D:/Lan/cropAsian/', dataset_name, '*.jpg')), "rb"), "image_file2": open(faceId2, "rb")}
#
# response = requests.post(compare_url, data=data, files=files)
#
# req_con = response.content.decode('utf-8')
# req_dict = JSONDecoder().decode(req_con)
# print(req_dict)
# confindence = req_dict['confidence']
# print(confindence)
# if confindence>=65:
#     print('是同一个人')
# else:
#     print('不是同一个人')
