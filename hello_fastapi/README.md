# Hello FastAPI

## FastAPI with websocket
- [教學](https://fastapi.tiangolo.com/advanced/websockets/)


## 運行方式
- [uvicorn](https://pypi.org/project/uvicorn/)


## 遇到的BUG
1. ImportError: cannot import name dataclass_transform
    - run ```viucorn hello-fastapi.main:app --host 0.0.0.0 --port 8087``` 的時候噴的錯誤 
    - 解決方案: 更新版本 ```pip install --upgrade typing_extensions>=4.1.0```
