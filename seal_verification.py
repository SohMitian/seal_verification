import cv2
import seal_detection as sd


def seal_verification(indocuments_path: str) -> float:
    # input document から印鑑を検出　-> 切り出し -> 類似度判定

    # ドキュメントの読み込み
    doc_img = cv2.imread(indocuments_path)

    # ドキュメントから印鑑を検出
    seal_coordinate = sd.seal_detection(doc_img)
    x = seal_coordinate[0] - seal_coordinate[2]
    y = seal_coordinate[1] - seal_coordinate[2]
    w_h = seal_coordinate[2]*2

    result_img = cv2.rectangle(
        doc_img, (x, y), (x + w_h, y + w_h), (0, 255, 0), 2)

    cv2.imwrite('test_assets/result_img.png', result_img)


if __name__ == '__main__':
    seal_verification('test_assets/sample.png')
