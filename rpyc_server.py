import rpyc
import subprocess
import nidaqmx
from nidaqmx.types import CtrTime
from nixnet_custom import nixnet

class MyService(rpyc.Service):
   exposed_nidaqmx   = nidaqmx
   exposed_CtrTime   = CtrTime
   exposed_nixnet    = nixnet
if __name__ == "__main__":
   try:
      from rpyc.utils.server import ThreadedServer
      t = ThreadedServer(MyService, port = 18861, protocol_config = {"allow_public_attrs" : True, "allow_all_attrs" : True})
      print("Starting the RPC Service")
      t.start()
   except Exception as e:
      print('Error Starting Rpyc Server : ', e)