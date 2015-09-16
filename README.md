# novelspider
### 用Scrapy和MongoDB来实现爬虫功能
#### Scrapy是Python开发的一个快速、高层次的屏幕抓取和web抓取框架,用于抓取Web站点并从页面中提取结构化的数据.它最吸引人的地方在于任何人都可以根据需求方便的修改。
#### MongoDB是现下非常流行的开源的非关系型数据库（NoSql），它是以“key-value”的形式存储数据的，在大数据量、高并发、弱事务方面都有很大的优势。

###其中用到的部分命令
	安装Scrapy : `pip install scrapy`
	创建Scrapy项目: `scrapy startproject novelspider`
	启动MongoDB命令: ` mongod --dbpath d:\MongoDB\Server\3.0\bin\data`
	启动Scrapy项目:  `scrapy crawl novspider`