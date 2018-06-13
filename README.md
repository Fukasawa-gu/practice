# annotation_from_trimmed_img.py
SSD_Kerasやdarkflowを使用して物体検出する際に必要となるアノテーションファイルを、すでにトリミングされた画像（一つの画像につき一つの物体がある画像）から、自動でアノテーションファイル(xml)を作成するプログラム。

# coin (1).xml
annotation_from_trimmed_img.pyを使う際に元データとして必要

# object_detection_cv2.py
閾値処理を利用した物体検出のプログラム。
検出した物をdetected(n).jpgで保存する。
背景が出来るだけ統一されている必要がある。

# coins (454).jpg
object_detection_cv2.pyでこの画像に実行すると上手くできてるはず。

# rakuma_get_data.py
旧ラクマに出品している商品のデータ（タイトル、詳細、価格）をExcelにまとめ、画像を保存する。

# rakuma_syuppin_new.py
merukari_get_data.py で保存した（タイトル、詳細、価格、商品の状態、保存した画像名）のExcelと画像を読み取り、ラクマに自動で出品する。
merukari_get_data.pyを利用しなくてもExcelの形式と画像名があっていれば自動で出品可能。

# merukari_to_rakuma.py
merukari_get_data.pyとrakuma_syuppin_new.pyを合わせたもの。

# merukari_get_data.py
メルカリに出品している商品のデータ（タイトル、詳細、価格、商品の状態、保存した画像名）をExcelにまとめ、画像を保存する。

# yahuoku_watchlist.py
ヤフオクの複数アカウントに対して出品している商品全てをウォッチリスト登録を行う。

