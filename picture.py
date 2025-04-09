import cv2

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame=cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break