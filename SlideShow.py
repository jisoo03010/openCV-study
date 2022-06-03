import os
import sys
import glob
import cv2


# 이미지 파일을 모두 img_files 리스트에 추가

# os.listdir() 사용 방법
#file_list = os.listdir('.\\images')
#img_files = [os.path.join('.\\images', file) for file in file_list if file.endswith('.jpg')]

# glob.glob() 사용 방법
img_files = glob.glob('.\\images\\*.jpg')

for f in img_files:
    print(f)