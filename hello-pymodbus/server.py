import logging
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore.context import ModbusSlaveContext, ModbusServerContext # <--- Updated lines here
from pymodbus.server.async_io import ModbusDeviceIdentification
from pymodbus.server import ModbusTcpServer

# Configure logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def run_server():
    # Initialize data store
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17, 17, 17, 17]),
        co=ModbusSequentialDataBlock(0, [17, 17, 17, 17]),
        hr=ModbusSequentialDataBlock(0, [17, 17, 17, 17]),
        ir=ModbusSequentialDataBlock(0, [17, 17, 17, 17]))
    
    context = ModbusServerContext(slaves=store, single=True)
    
    # Configure server identity
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'PyModbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'PyModbus Server'
    identity.ModelName = 'PyModbus'
    identity.MajorMinorRevision = '3.11.2'

    # Start the TCP server
    StartTcpServer(context=context, identity=identity, address=("localhost", 5020))

if __name__ == "__main__":
    run_server()

