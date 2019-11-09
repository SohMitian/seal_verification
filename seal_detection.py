import numpy as np
import cv2


def seal_detection(imgpath: str):
    image = cv2.imread(imgpath)

    hsv_upper = np.array([0, 255, 255])
    hsv_lower = np.array([0, 100, 100])
    hsv_result = hsv_extraction(image, hsv_lower, hsv_upper)
    h, s, v1 = cv2.split(hsv_result)

    cimg = v1

    circles = cv2.HoughCircles(cimg, cv2.HOUGH_GRADIENT, dp=1,
                               minDist=20, param1=50, param2=30, minRadius=0, maxRadius=100)

    # 検出した円の座標（浮動小数点）を2バイトの符号なし整数にキャスト
    circles = np.uint16(np.around(circles))
    # 最初に見つけた円を抜き出す
    circles = circles[0][0]

    coordinate = [circles[0], circles[1], circles[2]]

    return coordinate


def hsv_extraction(image: str, hsvLower: int, hsvUpper: int) -> np.ndarray:
    """
    特定の色を抽出する関数

    Args1:
      image str:
        画像のパス

    Args2:
      hsvLower int:
        8bit色の下限値

    Args3:
      hsvUpper int:
        8bit色の上限値

    Returns:
      np.ndarray:
        特定の色を抜き出した画像

    Errors:
      未定義

    """
    # 画像をHSV形式に変換
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 範囲指定をして二値化
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)
    # 対象の色以外をカット
    result = cv2.bitwise_and(image, image, mask=hsv_mask)

    return result


if __name__ == '__main__':
    seal_detection('/Users/soh92/Downloads/sample.png')
