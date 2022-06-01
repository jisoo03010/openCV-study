import cv2
import sys
print("hello, opencv", cv2.__version__)

# cv2.IMREAD_GRAYSCALE => 흑백 사진 , 영상으로 가져옴
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)



if img is None:  #만약 이미지를 불러오지 못하는 아래를 출력하라 
    print("Image load failde!")
    sys.exit()

#불러온 img 파일을 png로 바꿔서 작성함
cv2.imwrite('cat_gray.png', img)

# , width와 height를 사용해서 크기를 변경하려면  normal을 정의해 줘야함 
# cv2.WINDOW_NORMAL => 창의 크기 조정가능 하게 하는 기능
# cv2.WINDOW_AUTOSIZE => 기본 값 (생략 가능)
cv2.namedWindow("image" ) #창생성 ("창의 이름")
cv2.imshow("image", img)    #창에다 이미지 보여주는 
key = cv2.waitKey() # 키보드 입력을 기다리고, 영상이 실제도 보여주는 기능
print(key) # => 이미지를 클릭후 키보드의 키를 누르면 해당키의 아스키 코드를 보여줌
# cv2.waitKey(3000) => 3초동안만 켜짐

#특정 키를 눌렀을때 이 프로그램을 실행하고 싶다면 아래와 같이 해야함
while True:
    if cv2.waitKey() == ord('q'): # 27 => esc키
        break



#창의 크기 변경
# cv2.resizeWindow("image",  100, 100) # cv2.IMREAD_GRAYSCAL로 정의해야지만 사용가능
#창의 위치 변경
# cv2.moveWindow("image", 100, 50)

cv2.imshow("image", img)
cv2.destroyWindow("image") # 창의 이름을 적어줘야함 
# cv2.destroyAllWindows() # 기존에 화면에 나타나있는 모든 창을 닫아라 