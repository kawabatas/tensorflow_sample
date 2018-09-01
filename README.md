# tensorflow_sample
学習モデルを一から作る
[参考](https://book.mynavi.jp/manatee/detail/id=87654)

## 起動
```
docker-compose up
```
コンテナの中に入る
```
docker-compose exec app bash
```

## 画像ダウンロード
```
root@fad36960dc3d:/home/app# python3 download_images.py
```

## モデル学習
```
root@fad36960dc3d:/home/app# python3 train.py
```

## 認識
- recognizer フォルダに使用する学習モデル `model.rb` を置く
- recognizer フォルダにターゲットの画像 `target.jpg` を置く
- `root@fad36960dc3d:/home/app# python3 recognizer/app.py` を実行する
