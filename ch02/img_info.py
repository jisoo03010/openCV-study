import sys
import cv2


# 영상 불러오기   
img1 = cv2.imread('./cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)


print(type(img1))
print(img1.shape) # img 크기 가져옴 2차원 배열
print(img2.shape) # img 크기 가져옴 3차원 배열

print(img1.dtype) 
print(img2.dtype) 

if img1.ndim == 2: # 2면 grayscale 임
    print('img2 is a grayscale image')

#위의 결과와 같은 값을 출력함 
if len(img1.shape) == 2: # 2면 grayscale 임
    print('img2 is a grayscale image')

h, w = img1.shape
print('w x h = {} x {}'.format(w, h))

#특정 위치의 색상 뽑아내는 방법
x = 20
y = 20

p = img1[x , y]
print(p)
p = img2[x , y]
print(p)

img1[x , y] = 0 # 해당 위치에 색상 지정하는 방법



for y in range(h):
    for x in range(w):
        img1[y, x] = 0
        img2[y, x] = [0, 255, 255]

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

cv2.waitKey()
# if img1 is None or img2 is None:
#     print('Image load failed!')
#     sys.exit()


# # 영상의 속성 참조
# print('type(img1):', type(img1))
# print('img1.shape:', img1.shape)
# print('img2.shape:', img2.shape)
# print('img1.dtype:', img1.dtype)

# # 영상의 크기 참조
# h, w = img2.shape[:2]
# print('img2 size: {} x {}'.format(w, h))

# if len(img1.shape) == 2:
#     print('img1 is a grayscale image')
# elif len(img1.shape) == 3:
#     print('img1 is a truecolor image')

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.waitKey()

# # 영상의 픽셀 값 참조
# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 255
#         img2[y, x] = (0, 0, 255)        

# # img1[:,:] = 255
# # img2[:,:] = (0, 0, 255)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.waitKey()

# cv2.destroyAllWindows()
