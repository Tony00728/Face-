# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import time
from pandas.core.frame import DataFrame
import os
import numpy as np
import time

start = time.perf_counter()

result = []
ages = []


http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key ="JLso2LyWzev1zEaDkzbpfRi0I9Ah8DCq"
secret ="FYP0OdDAexPTkZM-QzclML15jZLNCal7"

#/home/tony/exp/exp_fading_shapeloss_white_males/70+/inference_results/80

filedir= r"/home/tony/exp/exp_fading_shapeloss_white_males/70+/inference_results/80"
writepath = "/home/tony/exp/exp_fading_shapeloss_white_males/70+/inference_results/80.xlsx"  # .csv


filelist = os.listdir(filedir)
for filename in filelist:
    filepath = os.path.join(filedir, filename)
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr = open(filepath, 'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_landmark')
    data.append('1')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'return_attributes')
    data.append(
        "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus")
    data.append('--%s--\r\n' % boundary)

    for i, d in enumerate(data):
        if isinstance(d, str):
            data[i] = d.encode('utf-8')

    http_body = b'\r\n'.join(data)

    # build http request
    req = urllib.request.Request(url=http_url, data=http_body)

    # header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)

    try:
        # post data to server
        resp = urllib.request.urlopen(req, timeout=1000)  #
        # get response
        qrcont = resp.read()
        # if you want to load as json, you should decode first,
        # for example: json.loads(qrount.decode('utf-8'))
        #print(qrcont.decode('utf-8'))
        dict = eval(qrcont)
        faces = dict['faces']
        for i in range(len(faces)):
            attribute = faces[i]['attributes']
            # gender = attribute['gender']['value']
            age = attribute['age']['value']
            print(age)
            ages.append(age)
            #print(ages)
            # face_rectangle = faces[i]['face_rectangle']
            # width = face_rectangle['width']
            # top = face_rectangle['top']
            # left = face_rectangle['left']
            # height = face_rectangle['height']
            result.append([filepath, age])

    except urllib.error.HTTPError as e:
        print(e.read().decode('utf-8'))

if ages:
    age_mean = np.mean(ages)
    age_sd = np.std(ages)
    max_age = np.max(ages)
    min_age = np.min(ages)
    print("Average Age:", age_mean)
    print("Age Standard Deviation:", age_sd)
    result.append([None, None, age_mean, age_sd, max_age , min_age])

DataFrame(result).to_excel(writepath,header=['filepath', 'age', 'age_mean', 'age_sd',  'max_age', 'min_age'])
#DataFrame(result).to_csv(writepath,header=['filepath', 'age', 'age_mean', 'age_sd',  'max_age', 'min_age'])

end = time.perf_counter()
print('運行時間：{} 秒'.format(end-start))