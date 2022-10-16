import uvicorn
from typing import Optional, List

from fastapi import FastAPI, WebSocket

from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect

app = FastAPI()  # 建立一個 Fast API application


# @app.get("/")  # 指定 api 路徑 (get方法)
# def read_root():
#     return {"Hello": "World"}


@app.get("/users/{user_id}")  # 指定 api 路徑 (get方法)
def read_user(user_id: int, q: Optional[int] = None):
    return {"user_id": user_id, "q": q}


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


# 處理和廣播訊息到多個 WebSocket 連線
class ConnectManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: str) -> None:
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(client_id: str, websocket: WebSocket):
    # 1、客戶端、服務端建立 ws 連線
    await manager.connect(websocket)
    
    # 2、廣播某個客戶端進入聊天室
    await manager.broadcast(f"{client_id} 進入了聊天室")
    
    try:
        while True:
            # 3、服務端接收客戶端傳送的內容
            data = await websocket.receive_text()
            
            # 4、廣播某個客戶端傳送的訊息
            await manager.broadcast(f"{client_id} 傳送訊息：{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{client_id} 離開了聊天室")


if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True, host="127.0.0.1", port=8000)

# viucorn hello-fastapi.main:app --host 0.0.0.0 --port 8087
