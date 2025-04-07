import requests
from json import JSONDecoder
import cv2
from glob import glob
import os
import numpy as np
from tqdm import tqdm
import time
from skimage.measure import compare_ssim, compare_psnr, compare_mse

faceId1= []
dataset1_name='F:/Lan/classification/test_dataset_class2/BM/'
f_names1 = glob(os.path.join('F:/Lan/classification/test_dataset_class2/BM/', dataset1_name, '*.jpg'))
#print(f_names1)


faceId2=[]
dataset2_name='F:/Lan/FS-D2AAE/BM/train_noD2_noloss/test_valid/'
f_names2 = glob(os.path.join('F:/Lan/FS-D2AAE/BM/train_noD2_noloss/test_valid/', dataset2_name, '*.png'))
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
                print('f3',f1,f2)

                img2 = cv2.imread(f_names2[i])
                img3 = cv2.resize(img2, (200,200))
                psnr = compare_psnr(img1, img3)
                ssim = compare_ssim(img1, img3, multichannel=True)  # 对于多通道图像(RGB、HSV等)关键词multichannel要设置为True
                mse = compare_mse(img1, img3)

                print('PSNR：{}，SSIM：{}，MSE：{}'.format(psnr, ssim, mse))
                arr.append(psnr)
                arr2.append(ssim)
                arr3.append(mse)

            else:
                continue
    except ValueError:
        continue

psnr=arr
print(psnr)
mean1=np.mean(psnr)
print('psne_mean',mean1)
std1=np.std(psnr)
print('psnr_std',std1)
ssim=arr2
print(ssim)
mean2=np.mean(ssim)
print('ssim_mean',mean2)
std2=np.std(ssim)
print('ssim_std',std2)
mse=arr3
print(mse)
mean3=np.mean(mse)
print('mse_mean',mean3)
std3=np.std(mse)
print('mse_std',std3)







# for i in tqdm(range(0,len(f_names1))):    #enumerate(f_names1):
#     #print('faceId1',faceId1)
#     faceId1=f_names1[i]
#     f1_1= os.path.basename(f_names1[i])
#     f1=os.path.splitext(f1_1)[0]
#     #print(f1)
#     #print(faceId1)
#
#     for i,faceId2 in enumerate(f_names2):
#         #f2 = os.path.basename(f_names2[i])
#         f2_2 = os.path.basename(f_names2[i])
#         f2 = os.path.splitext(f2_2)[0]
#         #print(f2)
#         label = (os.path.splitext(os.path.basename(f_names2[i]))[0])[-1]
#         #print(label)
#         if label=='5':
#             f3=f2[:-2]
#         else:
#             continue
#         #print(f3)
#         #print(f2)
#         #print(faceId2)
#         if f1==f3:
#             #print(f1,',',f2,",",f3)
#             data = {"api_key": key, "api_secret": secret}
#             files = {"image_file1": open(faceId1, "rb"), "image_file2": open(faceId2, "rb")}
#             #print("files",files)
#             response = requests.post(compare_url, data=data, files=files)
#
#             req_con = response.content.decode('utf-8')
#             req_dict = JSONDecoder().decode(req_con)
#             #print(f1,f2)
#             #print(req_dict)
#             try:
#                 confindence = req_dict['confidence']
#                 #print(confindence)
#             except:
#                 continue
#
#             time.sleep(0.3)
#             arr.append(confindence)
#
# confindence=arr
# print(confindence)
# mean=np.mean(confindence)
# print('mean',mean)
# std=np.std(confindence)
# print('std',std)



