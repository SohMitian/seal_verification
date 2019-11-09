import numpy as np
import cv2


def seal_detection(imgpath: str):
    """
    画像から赤色の円を抽出する関数

    Args:
      param1 (str): 画像のパス

    Returns:
      circle_coordinate (float): 円の座標と半径

    Errors:
      未定義
    """
    # 画像の読み込み
    img = cv2.imread(imgpath)

    # HSVの色上下限値を設定
    hsv_upper = np.array([0, 255, 255])
    hsv_lower = np.array([0, 100, 100])
    # 特定カラーの抜き出し
    extracted_hsv_img = hsv_extraction(img, hsv_lower, hsv_upper)
    # HSV画像からグレースケール（V）を取得
    gray_img = extracted_hsv_img[:, :, 0]
    # 円の検出
    circles = cv2.HoughCircles(gray_img, cv2.HOUGH_GRADIENT, dp=1,
                               minDist=20, param1=50, param2=30, minRadius=0, maxRadius=100)

    # 検出した円の座標（浮動小数点）を2バイトの符号なし整数にキャスト
    circles = np.uint16(np.around(circles))
    # 最初に見つけた円を抜き出す
    circles = circles[0][0]
    # 円の「中心X」「中心Y」「半径」を取得
    circle_coordinate = [circles[0], circles[1], circles[2]]

    return circle_coordinate


def hsv_extraction(image: str, hsvLower: int, hsvUpper: int) -> np.ndarray:
    """
    特定の色を抽出する関数

    Args:
      param1 (str): 画像のパス
      param2 (int): 8bitカラーを0~255の間で指定
      param3 (int): 8bitカラーを0~255の間で指定

    Returns:
      masked_img (np.ndarray): 特定の色を抜き出した画像

    Errors:
      未定義
    """
    # 画像をHSV形式に変換
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 範囲指定をして二値化
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)
    # 対象の色以外をカット
    masked_img = cv2.bitwise_and(image, image, mask=hsv_mask)

    return masked_img


if __name__ == '__main__':
    seal_detection('/Users/soh92/Downloads/sample.png')
