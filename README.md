# matzTada.github.io

<https://matztada.github.io>  

<a href="https://matztada.github.io">
	<img src="https://matztada.github.io/images/screenshot.png" alt="" width=50%>
</a>  

## Content handler by Python

* can change ```style``` attribute of ```article``` tag based on the pre-defined sequence
* can ```append```, ```modify```, ```clear``` articles
* create ```index.html``` based on ```index_seed.html```
* 最悪jsがくるっても，htmlそのものをファイルとして読み書きしているという点に利点はあるかも

## Color Changer by JavaScript

* Color set will be selected with Checkbox
* Color set changed when button pushed

## To Do

* sorting
	* 既存のソート
	* 名前順	
* 更新日を引っ張ってこれるようにしたい

## tips
### html handling with Python

* ```pip install beautifulsoup4```
* <http://qiita.com/itkr/items/513318a9b5b92bd56185>
* <http://kondou.com/BS4/>
	* [パースツリーの変更のくだり](http://kondou.com/BS4/#id38)
	* NavigableStringっていうのを使えば，tagに挟まれた文字を置換できる
	* [tag].string.replace_with("[string]")で文字を変えられる
	* ```["attribute"]```で属性
	* ```.string```でタグに挟まれた中身の文字