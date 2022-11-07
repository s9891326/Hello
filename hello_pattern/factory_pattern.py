# The Factory Pattern（工廠模式： 解決物件建立問題）
# 先來看三種創建模式中的第一種工廠模式。
# 解釋：處理對象創建，用戶端可以申請一個物件而不用知道對象被哪個class創建。
# 可以方便地解耦物件的使用和創建。
# 有兩種實現，工廠方法和抽象工廠.

# 適合使用在多個對象據有不同的屬性，但執行同樣的Methods時；可以先設計一個基礎的Class，
# 新的對象再去繼承這個Base class，擴充其屬性，並在執行時調用同樣的Methods
# 使用情境的範例是一間工廠會製造多個不同的產品，產品有不同的規格，但有類似的製造流程時，可以使用類似這樣的設計模式

import json
import xml.etree.ElementTree as etree


class JsonConnector:
    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(file_path):
    """ 工厂方法 """
    if file_path.endswith('json'):
        connector = JsonConnector
    elif file_path.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(file_path))
    return connector(file_path)

# d = {"a": 123, "b": 456}
# with open("test.json", "w+", encoding="utf-8") as f:
#     f.write(json.dumps(d, ensure_ascii=False))

if __name__ == '__main__':
    file_path = "test.json"
    print(connection_factory(file_path).parsed_data)

