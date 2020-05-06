import rpyc
import nidaqmx
from nidaqmx.types import CtrTime
try:

    #import nidaqmx
    with nidaqmx.Task() as aitask:
        aitask.ai_channels.add_ai_voltage_chan("Mod2/ai0")
        voltage = aitask.read()
        print("Voltage :", voltage)


    with nidaqmx.Task() as citask:
        citask.ci_channels.add_ci_pulse_chan_freq("Mod8/ctr2")
        data    = citask.read(timeout=30)
        print("1 Channel 1 Sample Read: ", data)
        #data    = citask.read(number_of_samples_per_channel=8,timeout=30)
        #print("1 Channel N Samples Read: ", data)

except Exception as e:
    print('Error in the code :', e)
