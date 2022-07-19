import cv2


def nothing(emp):
    pass


video = 'E:\\毕设\\video\\fire_1.mp4'
cv2.namedWindow('video')
cap = cv2.VideoCapture(video)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
loop_flag = 0
pos = 0
cv2.createTrackbar('time', 'video', 0, frames, nothing)

while 1:
    if loop_flag == pos:
        loop_flag = loop_flag + 1
        cv2.setTrackbarPos('time', 'video', loop_flag)
    else:
        pos = cv2.getTrackbarPos('time', 'video')
        loop_flag = pos
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
    ret, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & loop_flag == frames:
        break