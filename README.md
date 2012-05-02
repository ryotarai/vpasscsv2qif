# VpassCSV2QIF
## 概要
vpass（三井住友VISAカード）の明細データをCSVからQIF形式に変換するスクリプト。
## 使用例
``$ python converter.py hogehoge.csv
``

output.qifが出力される。
## 読み込み
iComptaでの読み込みを確認済み。
iComptaで読みこむ際は、

* Date Format: YYYY/MM/dd
* Encoding: UTF-8

にする必要がある。
