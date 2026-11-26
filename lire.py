from pymodbus.client import ModbusTcpClient

with ModbusTcpClient("127.0.0.1", port=502) as client:
    print("HR 0-2 =", client.read_holding_registers(address=0, count=3).registers)