import rpyc
import subprocess
import nidaqmx
import nifpga
from nixnet_custom import nixnet
from nidaqmx import stream_writers
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration
from rpyc.utils.server import ThreadedServer
from nifpga import Session

class MyService(rpyc.Service):
   exposed_nidaqmx                                     = nidaqmx
   exposed_nixnet                                      = nixnet
   exposed_nifpga                                      = nifpga
   exposed_AcquisitionType                             = AcquisitionType
   exposed_TerminalConfiguration                       = TerminalConfiguration
   exposed_stream_writers                              = stream_writers
   exposed_Session                                     = Session

if __name__ == "__main__":
   try:
      t = ThreadedServer(MyService, port = 18861, protocol_config = {"allow_public_attrs" : True, "allow_all_attrs" : True})
      print("Starting the RPC Service")
      t.start()
   except Exception as e:
      print('Error Starting Rpyc Server : ', e)
