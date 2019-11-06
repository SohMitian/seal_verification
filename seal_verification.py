import numpy as np
import cv2
import seal_detection as sd

# 印鑑照合関数
def seal_verification(indocuments_path: str) -> float:
    # input document から印鑑を検出　-> 切り出し -> 類似度判定

    # ドキュメントの読み込み
    doc_img = cv2.imread(indocument_path)

    # ドキュメントから印鑑を検出
    seal_img = sd.seal_detection(doc_img)

    

    return null;

if __name__ == '__main__':
    seal_verification('C:/Users/owner/Pictures/img/sample.png')