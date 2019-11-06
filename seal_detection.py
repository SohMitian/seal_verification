import numpy as np
import cv2

# 印鑑検出関数
# 引数: 画像パス str
# 戻り値: 円の座標(x, y, r) int
def seal_detection(imgpath: str) -> int:
    image = cv2.imread(imgpath) # ファイル読み込み

    # HSVでの色抽出
    hsv_upper = np.array([0, 255, 255])    # 抽出する色の上限
    hsv_lower = np.array([0, 100, 100])    # 抽出する色の下限
    hsv_result = hsvExtraction(image, hsv_lower, hsv_upper)
    h, s, v1 = cv2.split(hsv_result)

    cimg = v1

    circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=100)

    circles = np.uint16(np.around(circles))
    circles = circles[0]

    # x, y, rの値をリストに入れる
    coordinate = [circles[0], circles[1], circles[2]]
    #for i in circles[0,:]:
        # draw the outer circle
        #cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)

    return coordinate


# HSVで特定の色を抽出する関数
def hsvExtraction(image, hsvLower, hsvUpper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # 画像をHSVに変換
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)    # HSVからマスクを作成
    result = cv2.bitwise_and(image, image, mask=hsv_mask) # 元画像とマスクを合成
    return result

if __name__ == '__main__':
    seal_detection('C:/Users/owner/Pictures/img/sample.png')