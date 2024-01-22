import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret, frame = webcam.read()
    cv.imshow('frame', frame)
    tecla = cv.waitKey(1)
    if tecla == ord('q'):
        cv.imshow('ret', frame)
    elif tecla == ord('w'):
        frameBlur = cv.filter2D(frame, -1,  (1, 1))
        frameSub = cv.subtract(frameBlur, frame)
        res = cv.add(frame, frameSub)
        cv.imshow('res', res)
    elif tecla == ord('e'):
        frameBlur = cv.filter2D(frame, -1,  (2, 2))
        frameSub = cv.subtract(frameBlur, frame)
        res = cv.add(frame, frameSub)
        cv.imshow('res', res)
    elif tecla == ord('r'):
        frameBlur = cv.filter2D(frame, -1, (3, 3))
        frameSub = cv.subtract(frameBlur, frame)
        res = cv.add(frame, frameSub)
        cv.imshow('res', res)
    elif tecla == ord('s'):
        break




