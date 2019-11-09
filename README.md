# seal_verification
## 印鑑照合ロジック
## Flow
1. 印鑑検出
2. 印鑑照合
### テスト用画像
![sample](https://user-images.githubusercontent.com/13077132/68528896-ce75c580-033b-11ea-8a0f-a8c74c683916.png)
## 印鑑検出
1. 画像から赤色部分を抽出
2. 抽出した画像に対して円検出
3. 検出した円のバウンディングボックスを設定
### 検出結果画像
![result_img](https://user-images.githubusercontent.com/13077132/68528878-a7b78f00-033b-11ea-817f-204e42a6ac25.png)

## 印鑑照合
1. 検出した印鑑の画像に対してテンプレートマッチング
2. マッチング率で照合

### ToDo
- マッチング率の閾値をどうするか
- かすれや回転の対応