# pn-webiopi

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
