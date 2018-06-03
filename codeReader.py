#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

def code_reader_by_camera():
	# ビデオキャプチャーの開始
	cap = cv2.VideoCapture(0)

	while True:
		# ビデオキャプチャーから画像を取得
		ret, frame = cap.read()
		# sizeを取得
		Height, Width = frame.shape[:2]
		img = cv2.resize(frame,(int(Width),int(Height)))
		# マーカを検出
		corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)
		# 検出したマーカーに描画する
		aruco.drawDetectedMarkers(img, corners, ids, (0,255,0))
		# 番号をターミナルに表示し続ける
		print(ids)
		## ToDo: 番号が配列の配列に収まっているので取り出す。（番号が認識されていないときは、Noneなので、単純に[0][0]で取り出してもエラーがおきるので注意）
		cv2.imshow('drawDetectedMarkers', img)
		# キーボード入力の受付
		cv2.waitKey(1)

	# ビデオキャプチャーのメモリ解放
	cap.release()
	cv2.destroyAllWindows()

code_reader_by_camera()