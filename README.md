# tensorflow_sample
学習モデルを一から作る
[参考](https://book.mynavi.jp/manatee/detail/id=87654)

## 画像ダウンロード
```
python3 download_images.py
```

## モデル学習
```
python3 train.py
```

## 認識
- recognizer フォルダに使用する学習モデル `model.rb` を置く
- recognizer フォルダにターゲットの画像 `target.jpg` を置く
- `python3 recognizer/app.py` を実行する
