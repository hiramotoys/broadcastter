broadcastter
============
登録した人全員に同じ内容のMentionを送ることができるスクリプト.

必要なもの
----------
python  
PyYAML  
tweepy  
Macportsでインストールできる
	sudo port install py26-yaml
	sudo port install py26-tweepy

Consumer key/secret. access key/secret
--------------------------------------
appdetail.yamlを書く.
	consumer_key : < consumer key >
	consumer_secret : < consumer secret >
	access_key : < access key >
	access_secret : < access_secret >

namelist.csv
------------
mentionを送る相手をnamelist.csvに書く
	hiramotoys, <なんとかさん>, <なんとかさん>
	<なんとかさん>