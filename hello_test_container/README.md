# Test Container(Python + SqlAlchemy + Postgres)

## 遇到的問題
當我們使用TDD的方式來開發時，時常會把資料庫相關的地方都直接Mock掉，來假設跟DB之間的交流是符合邏輯的。但往往會發生不如預期的事情，假如某張table要增加一個欄位，但某些地方卻沒修改到，導致服務整個爆炸，就GG了

## 解決方式
因為會有上面的問題，所以就有了`Test Container`，來支援撰寫測試案例的時候，可以幫忙起個容器(Container)，並架設指定的資料庫(Postgres、MySQL...)等等可以放在Docker上面的images

## 實作分享
1. 安裝套件
```
pip install testcontainers==3.4.2
pip install SQLAlchemy==1.4.45
pip install psycopg2-binary==2.9
```
2. 定義model(DB table)
3. 撰寫db_mask


## 總結



## 參考
1. https://nijialin.com/2021/11/25/python-testcontainer-fasstapi-database/

