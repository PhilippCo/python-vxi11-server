import time
import vxi11_server as Vxi11
import pyvisa

class VxiGW(Vxi11.InstrumentDevice):
    def __init__(self, device_name):
        super().__init__(device_name)
        self.rm = pyvisa.ResourceManager('@py')

        if device_name == "korad1":
            self.device = self.rm.open_resource('ASRL/dev/ttyACM0::INSTR')

        elif device_name == "korad2":
            self.device = self.rm.open_resource('ASRL/dev/ttyACM1::INSTR')

        elif device_name == "sdg1025":
            self.device = self.rm.open_resource('USB0::62701::60986::SDG00004131329::0::INSTR')

        elif device_name[:4] == "gpib":
            gpib = int(device_name.split(",")[1])
            visastr = "GPIB0::{0:d}::INSTR".format(gpib)
            print(visastr)
            self.device = self.rm.open_resource(visastr)

        else:
            print("no match!!")

    def device_read(self):
        '''respond to the device_read rpc: refer to section (B.6.4)
           of the VXI-11 TCP/IP Instrument Protocol Specification'''
        error = Vxi11.Error.NO_ERROR

        result = self.device.read()
		# In this case, our result is an ascii string. 
		# encode and return the result as binary (opaque) data for transfer to host
        return error, result.encode('ascii')

    def device_write(self, opaque_data):
        self.device.write(opaque_data.strip().decode("ascii"))
        return Vxi11.Error.NO_ERROR

if __name__ == '__main__':
    # create a server, attach a device, and start a thread to listen for requests
    instr_server = Vxi11.InstrumentServer()
    instr_server.add_device_handler(VxiGW, 'korad1')
    instr_server.add_device_handler(VxiGW, 'korad2')
    instr_server.add_device_handler(VxiGW, 'sdg1025')

    for gpibno in range(1, 30):
        instr_server.add_device_handler(VxiGW, "gpib0,{0:d}".format(gpibno))

    instr_server.listen()

    # sleep (or do foreground work) while the Instrument threads do their job
    while True:
   	    time.sleep(1)
