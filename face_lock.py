import requests
from json import JSONDecoder
import datetime
import cv2
import os
#'faceset_token': '5309ce72084fe8430a6ca31b4a700bc4'
#'face_token': '8b7fa9baf07b6bb1b4e7a22aec64e22d'
key ="Lw7WQXJMIfpF--CE05dnko3nhWzjpe9c"
secret ="a0Aw1jXqhwYWnnR_e_O23GD0-R87E4En"
def jiance():#摄像头实时分析
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"
    filepath1 ="E:/opencv_pictures/face++/image/my_face.jpg"
    # 需要发送的数据
    data = {"api_key":key, "api_secret": secret,"return_attributes":"age,emotion", }  # 多个返回值用“,”隔开
    files = {"image_file": open(filepath1, "rb")}
    cap = cv2.VideoCapture(0)
    while   True:
        ret, frame = cap.read()
        # cv2.resize(frame,frame,320,240,0)
        # show a frame
        cv2.imshow("capture", frame)
        cv2.imwrite("E:/opencv_pictures/face++/image/my_face.jpg", frame)
        # 打开文件的地址
        files = {"image_file": open(filepath1, "rb")}
        starttime = datetime.datetime.now()
        # post上传
        response = requests.post(http_url, data=data, files=files)
        test = response.json().get('faces')
        """
        endtime = datetime.datetime.now()
        print((endtime - starttime).seconds)
        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)
        print(req_dict)
        """
        print(response.json())
        print(test)
        cv2.waitKey(10)
def shangchuan():#上传人脸数据
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    # 需要发送的数据
    data = {"api_key": key, "api_secret": secret, "return_attributes": "age,emotion", }  # 多个返回值用“,”隔开
    filepath1 = "E:/opencv_pictures/face++/image/my_face.jpg"
    files = {"image_file": open(filepath1, "rb")}
    response = requests.post(http_url, data=data, files=files)
    test = response.json().get('faces')
    print(response.json())
    print(test)
def Compare(): # 人脸对比
    url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
    # 需要发送的数据
    data = {"api_key": key, "api_secret": secret, "face_token1": "8b7fa9baf07b6bb1b4e7a22aec64e22d","face_token2":"1b14251fdc701551e025b152dc272f33" }  # 多个返回值用“,”隔开
    image_file2 = "E:/opencv_pictures/face++/image/my_face.jpg"
    image_file2 = {"image_file2": open(image_file2, "rb")}
    response = requests.post(url, data=data,)
    print(response.json())
# 返回值{'confidence': 85.179, 'request_id': '1521508784,c368e44a-e430-4675-858a-f8ce3bb44d50', 'time_used': 547, 'thresholds': {'1e-3': 62.327, '1e-5': 73.975, '1e-4': 69.101}}
def FaceSet_Create():  # 建立人脸识别库
    url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"
    data = {"api_key": key, "api_secret": secret,}  #
    # post上传
    response = requests.post(url, data=data)
    test = response.json()
    print(test)
def Search():# 在库中搜索人脸数据
    url = "https://api-cn.faceplusplus.com/facepp/v3/search"
def FaceSet_AddFace(): #添加人脸到库中
    url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
    data = {"api_key": key, "api_secret": secret,"faceset_token": "5309ce72084fe8430a6ca31b4a700bc4","face_tokens": "8b7fa9baf07b6bb1b4e7a22aec64e22d",}
    response = requests.post(url, data=data)
    test = response.json()
    print(test)
def camera_compare():#摄像头实时比对
    url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
    filepath1 = "E:/opencv_pictures/face++/image/my_face.jpg"
    # 需要发送的数据
    data = {"api_key": key, "api_secret": secret,"face_token1": "8b7fa9baf07b6bb1b4e7a22aec64e22d" }  # 多个返回值用“,”隔开
    files = {"image_file": open(filepath1, "rb")}
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # cv2.resize(frame,frame,320,240,0)
        # show a frame
        cv2.imshow("capture", frame)
        cv2.imwrite("E:/opencv_pictures/face++/image/my_face.jpg", frame)
        # 打开文件的地址
        files = {"image_file2": open(filepath1, "rb")}
        starttime = datetime.datetime.now()
        # post上传
        response = requests.post(url, data=data, files=files)
        # 返回比较结果
        print(response.json())
        cv2.waitKey(10)
#FaceSet_Create()
#shangchuan()
#FaceSet_AddFace()
#FaceSet_Create()
#Compare()
#jiance()
camera_compare()
# 网址：http://blog.csdn.net/qq_34475777/article/details/78446731