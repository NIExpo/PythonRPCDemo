import rpyc
import subprocess
import nidaqmx
from nixnet_custom import nixnet
from nidaqmx.constants import FuncGenType
from nidaqmx.constants import AcquisitionType
from nidaqmx.constants import TerminalConfiguration

class MyService(rpyc.Service):
   exposed_nidaqmx                 = nidaqmx
   exposed_nixnet                  = nixnet
   exposed_AcquisitionType         = AcquisitionType
   exposed_TerminalConfiguration   = TerminalConfiguration
   exposed_FuncGenType             = FuncGenType

if __name__ == "__main__":
   try:
      from rpyc.utils.server import ThreadedServer
      t = ThreadedServer(MyService, port = 18861, protocol_config = {"allow_public_attrs" : True, "allow_all_attrs" : True})
      print("Starting the RPC Service")
      t.start()
   except Exception as e:
      print('Error Starting Rpyc Server : ', e)
