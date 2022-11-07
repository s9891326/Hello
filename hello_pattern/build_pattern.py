# Builder Pattern（構造模式： 控制複雜物件的構造）
# 當物件需要多個部分組合起來一步步創建，並且創建和表示分離的時候。
# 可以這麼理解，你要買電腦，工廠模式直接返回一個你需要型號的電腦，但是構造模式允許你自定義電腦各種配置類型，組裝完成後給你。
# 這個過程你可以傳入builder從而自定義創建的方式

# 這種設計模式適合使用在單一訊息接收口，要處理不同流程的情境
#
# 分成Director和Builder的角色
#
# 例如當一間餐廳要製作餐點時，由點餐員（Director）接收餐點訂單
#
# 再將這些餐點（如漢堡、飲料、甜點…）發送到不同的餐點製造口（Builder）
#
# 最後再將製作好的餐點彙整起來出餐

# factory pattern
MINI14 = '1.4GHz Mac mini'


class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.memory = 4  # in gigabytes
            self.hdd = 500  # in gigabytes
            self.gpu = 'Intel HD Graphics 5000'
        
        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)
    
    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print("I don't know how to build {}".format(model))


# 使用工厂
afac = AppleFactory()
mac_mini = afac.build_computer(MINI14)
print(mac_mini)


# builder模式
class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None      # in gigabytes
        self.hdd = None         # in gigabytes
        self.gpu = None

    def __str__(self):
        info = ('\nMemory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    @property
    def computer(self):
        return self.builder.computer

# 使用builder，可以创建多个builder类实现不同的组装方式
engineer = HardwareEngineer()
engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
computer = engineer.computer
print(computer)
