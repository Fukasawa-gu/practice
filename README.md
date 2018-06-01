# annotation_from_trimmed_img.py
SSD_Kerasやdarkflowを使用して物体検出する際に必要となるアノテーションファイルを、すでにトリミングされた画像（一つの画像につき一つの物体がある画像）から、自動でアノテーションファイル(xml)を作成するプログラム。

# object_detection_cv2.py
閾値処理を利用した物体検出のプログラム。
背景が出来るだけ統一されている必要がある。

# rakuma_get_data.py
ラクマに出品している商品のデータ（タイトル、詳細、価格）をExcelにまとめ、画像を保存する。

# yahuoku_watchlist.py
ヤフオクの複数アカウントに対して出品している商品全てをウォッチリスト登録を行う。
