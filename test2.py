import cv2


def main() :
    cap=cv2.VideoCapture()
    if cap.isOpened() :
        ret, frame=cap.read()
        print(ret)
        print(frame)
    else:
if __name__ == "__main__" :
    main()
