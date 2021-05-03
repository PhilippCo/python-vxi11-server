import pyvisa
rm = pyvisa.ResourceManager('@py')
inst = rm.open_resource("TCPIP::192.168.2.88::gpib0,22::INSTR")
inst.write("END ALWAYS")
print(inst.query("ID?"))
inst.close()
