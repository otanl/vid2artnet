#  vid2artnet

OpenCVとstupidArtnetライブラリを使用して、ビデオファイルからフレームを読み取り、それらをArt-Netデータとして送信します。（monitor.pyは確認用です）

## 機能

- ビデオファイル（HAP形式が推奨）からフレームを読み取ります。
- フレームのピクセルデータを抽出し、Art-Netデータとして送信します。
- ビデオの各行に対して、StupidArtnetインスタンスが作成されます。(動画の解像度は、"最大ch数"*"ユニバース数"になるようにしてください。)

## 必要なライブラリ

- OpenCV
- stupidArtnet

```bash
$ pip install stupidartnet opencv-python
```

## 使用方法

1. `TARGET_IP`変数を、Art-Netデータを送信する対象のIPアドレスに設定します。
2. `cap = cv2.VideoCapture('test.mov')`の`test.mov`を、使用するビデオファイルのパスに変更します。
3. コードを実行します。
