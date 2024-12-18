# webiopiを最新のラズパイで利用するためのパッチ(全ラズパイ対応版)


WebIOPiのオリジナルは既に開発が停止しているため、最新のRaspberry Piに対応していません。
有志によっていくつかのパッチが登場していますが、GPIOのALT機能に対応していないものが多く、利用するためにはいくつかの制限がありました。
そこで、もともと提供されているWebIOPiの機能が利用できるようにパッチを作成しました。
また、今後登場するラズパイにも対応できるようにPythonモジュールへのパッチも作成しwebiopiモジュールも少しだけ拡張しています。

導入手順はいかのとおりです。ご利用する場合には自己の判断にてご利用をお願いいたします。

【手順】
ラズベリーパイにWebIOPiをインストールする

* WebIOPiをダウンロードします。  
`$ wget http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz`

* 解凍します。  
`$ tar xvzf WebIOPi-0.7.1.tar.gz`

* パッチをダウンロードします。  
`$ git clone https://github.com/pochiken/pn-webiopi.git`

* WebIOPiのディレクトリに移動します。  
`$ cd WebIOPi-0.7.1`

* パッチを実行します。  
`$ patch -p1 < ../pn-webiopi/WebIOPi-RPiALL.patch`

* Raspberry Pi 5/500でwebiopiを利用する場合はRaspi5用のパッチを追加で適用します。(注：Raspi5/500以外に適用すると動きません)

  `$ patch -p1 < ../pn-webiopi/Webiopi_RPi5.patch`

* セットアップを実行します。  
`$ sudo ./setup.sh`  

「Do you want to access WebIOPi over Internet ? [y/n]」が表示されたら「n」を入力してから「Enter」キーを押します。 
  
  
  
# pythonモジュールwebiopiについて

## RPI_INFO()を追加しています。
RPI_INFO()を利用することで実行中のRaspberry Piの情報を取得することが可能です。
webiopi.GPIO.RPI_INFOを実行することでJSON形式のデータが取得できます。
取得できる情報は以下の通りです（以下はRaspberry Pi 5にて実行したときの情報です）

{'P1_REVISION': 3, 'REVISION': 'c04170', 'TYPE': 'Raspberry Pi 5 Model B', 'MANUFACTURER': 'Sony UK', 'PROCESSOR': 'BCM2712', 'BREV': '1.0', 'RAM': '4G'}

# REST APIについて
## rpi_infoで情報を取得できます。
`GET /rpi_info`  
{"P1_REVISION": 3, "REVISION": "a020d3", "TYPE": "Raspberry Pi 3 Model B+", "MANUFACTURER": "Sony UK", "PROCESSOR": "BCM2837", "RAM": "1G"}

# WebIOPi Main Menuに実行中のラズパイ情報が表示されます  
![webiopi_rp5_top](https://github.com/user-attachments/assets/57177ced-7ae8-4707-b7d8-111af6fc177e)
# I2C/SPI/UART/1wireなど設定することで表示変わります（UART/1wireは再起動が必要）  
![webiopi_rp5](https://github.com/user-attachments/assets/16f56f98-139c-4fbb-abc2-826460b656ba)


