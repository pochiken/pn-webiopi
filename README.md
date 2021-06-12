# webiopiを最新のラズパイで利用するためのパッチ
#（全ラズパイに対応のはず）


WebIOPiのオリジナルは既に開発が停止しているため、最新のRaspberry Piに対応していません。
有志によっていくつかのパッチが登場していますが、GPIOのALT機能に対応していないものが多く、利用するためにはいくつかの制限がありました。
そこで、もともと提供されているWebIOPiの機能が利用できるようにパッチを作成しました。
また、今後登場するラズパイにも対応できるようにPythonモジュールへのパッチも作成しwebiopiモジュールも少しだけ拡張しています。

導入手順はいかのとおりです。ご利用する場合には自己の判断にてご利用をお願いいたします。

【手順】
ラズベリーパイにWebIOPiをインストールする

WebIOPiをダウンロードします。

$ wget http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz

解凍します。

$ tar xvzf WebIOPi-0.7.1.tar.gz

WebIOPiのディレクトリに移動します。

$ cd WebIOPi-0.7.1

パッチをダウンロードします。

$ wget https://github.com/pochiken/pn-webiopi/blob/main/WebIOPi-RPiALL.patch

パッチを実行します。

$ patch -p1 -i WebIOPi-RPiALL.patch

セットアップを実行します

$ sudo ./setup.sh

「Do you want to access WebIOPi over Internet ? [y/n]」が表示されたら「n」を入力してから「Enter」キーを押します。 



pythonモジュールwebiopiについて

RPI_INFO()を追加しています。
RPI_INFO()を利用することで実行中のRaspberry Piの情報を取得することが可能です。
webiopi.GPIO.RPI_INFOを実行することでJSON形式のデータが取得できます。
取得できる情報は以下の通りです（以下はRaspberry Pi A+にて実行したときの情報です）

{'P1_REVISION': 3, 'REVISION': '900021', 'TYPE': 'Model A+', 'MANUFACTURER': 'Sony UK', 'PROCESSOR': 'BCM2835', 'RAM': '512M'}

![webiopi_menu](https://user-images.githubusercontent.com/24805847/121764068-f82c4980-cb7b-11eb-8d02-b995199b45ce.png)

![webiopi](https://user-images.githubusercontent.com/24805847/121349278-49fa8700-c964-11eb-971c-88f845703fb5.png)

