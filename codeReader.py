#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

def code_reader_by_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        height, width = frame.shape[:2]
        img = cv2.resize(frame,(int(width),int(height)))
        corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)
        if isinstance(ids, numpy.ndarray) == True:
            print(ids[0][0])
        else:
            print(ids)
        # 二次元コードに描画する
        #aruco.drawDetectedMarkers(img, corners, ids, (0,255,0))
        #cv2.imshow('drawDetectedMarkers', img)
        cv2.waitKey(0)

    cap.release()
    #cv2.destroyAllWindows()

code_reader_by_camera()