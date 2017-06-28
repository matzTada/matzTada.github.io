# matzTada.github.io

<https://matztada.github.io>  

<a href="https://matztada.github.io">
	<img src="https://matztada.github.io/images/screenshot.png" alt="" width=50%>
</a>  

## Content handler

* can change ```style``` attribute of ```article``` tag based on the pre-defined sequence
* can "append", "modify", "clear" articles


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
	* 