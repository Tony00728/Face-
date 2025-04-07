import requests
from json import JSONDecoder
import cv2
from glob import glob
from pandas.core.frame import DataFrame

import os
import numpy as np
import time

start = time.perf_counter()


compare_url = "https://api-us.faceplusplus.com/facepp/v3/compare"
key ="xxTPFUxNwfHYaMTIJykGFUPcEMZCzQlS"
secret ="QAaaLge6Ik97qOBTqv_pMxGRIUAeBJWv"


#原圖
faceId1= []
dataset1_name='/home/tony/FFHQ_testing_white_males/40-49/new_image'
f_names1 = glob(os.path.join('/home/tony/FFHQ_testing_white_males/40-49/new_image', dataset1_name, '*.jpg'))
#print(f_names1)



#test
faceId2=[]
dataset2_name='/home/tony/exp/exp_sam/WM/40-49/inference_results/45'
f_names2 = glob(os.path.join('/home/tony/exp/exp_sam/WM/40-49/inference_results/45', dataset2_name, '*.jpg'))  #PNG jpg
writepath = "/home/tony/exp/exp_sam/WM/40-49/inference_results/45_identity.xlsx"  # .csv



#print(f_names2)
# fa1 = os.path.basename(f_names1)
# print(fa1)

arr=[]
arr2=[]
result = []

for i,faceId1 in enumerate(f_names1):
    f1_1= os.path.basename(f_names1[i])
    f1=os.path.splitext(f1_1)[0]
    #print(f1)
    #print(faceId1)

    for i,faceId2 in enumerate(f_names2):
        #f2 = os.path.basename(f_names2[i])
        f2_2 = os.path.basename(f_names2[i])
        f2 = os.path.splitext(f2_2)[0]
        #print(f2)
        #print(faceId2)
        if f1 == f2:
            data = {"api_key": key, "api_secret": secret}
            files = {"image_file1": open(faceId1, "rb"), "image_file2": open(faceId2, "rb")}
            print("files",files)

            # 检查是否有一个文件夹中不存在的图片，然后跳过当前迭代
            if not (os.path.exists(faceId1) and os.path.exists(faceId2)):
                print("One of the folders is missing the image. Skipping...")
                continue


            response = requests.post(compare_url, data=data, files=files, timeout=1000)
            req_con = response.content.decode('utf-8')
            req_dict = JSONDecoder().decode(req_con)
            #print(f1,f2)
            #print(req_dict)

            if 'confidence' not in req_dict:
                print("No confidence key in response. Skipping..")
                continue

            confindence = req_dict['confidence']


            print(confindence)

            if confindence >= 65:
                acc=1
                #print('是同一个人')
            else:
                acc=0
                print("no same",f1)
                #print('不是同一个人')
            arr.append(confindence)
            arr2.append(acc)
            result.append([files, confindence, acc])



confindence=arr
#print(confindence)
mean=np.mean(confindence)
print('mean :',mean)
std=np.std(confindence)
print('std : ',std)
acc_acc=arr2
#print(acc_acc)
acc_mean=np.mean(acc_acc)
print('acc mean : ',acc_mean)
result.append([None, None,  None, mean, std, acc_mean])
DataFrame(result).to_excel(writepath,header=['files', 'confindence', 'acc', 'confindence_mean',  'confindence_std', 'acc_mean'])


end = time.perf_counter()
print('運行時間：{} 秒'.format(end-start))
