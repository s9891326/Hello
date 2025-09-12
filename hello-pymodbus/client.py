import logging
from pymodbus.client import ModbusTcpClient

# 設定 logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def run_client():
    # 建立 TCP Client，連線到 localhost:5020
    client = ModbusTcpClient('localhost', port=5020)
    
    print("正在連線到伺服器...")
    if not client.connect():
        print("連線失敗！")
        return
    print("連線成功！")

    # 讀取 Holding Registers
    # 讀取地址 0 開始的 4 個暫存器
    print("\n[讀取] Holding Registers (地址 0-3)...")
    result = client.read_holding_registers(0, 4)
    if result.isError():
        print(f"讀取失敗：{result}")
    else:
        print(f"讀取到的資料：{result.registers}")

    # 寫入單一 Coil
    # 將地址 0 的 Coil 設為 True (開)
    print("\n[寫入] Coil (地址 0) 為 True...")
    result = client.write_coil(0, True)
    if result.isError():
        print(f"寫入失敗：{result}")
    else:
        print("寫入成功！")

    # 再次讀取 Coils 來驗證寫入
    print("\n[讀取] Coils (地址 0-3) 來驗證...")
    result = client.read_coils(0, 4)
    if result.isError():
        print(f"讀取失敗：{result}")
    else:
        print(f"讀取到的資料：{result.bits}")
        
    client.close()

if __name__ == "__main__":
    run_client()
