import rpyc


try:

    print('Connecting to Server')
    HOSTNAME    = '10.34.75.80'
    PORT        = 18861
    connection  = rpyc.connect(HOSTNAME, PORT)
    print('Connected to Server')

    #Expose Remote Modules
    nidaqmx            = connection.root.nidaqmx

    #import nidaqmx
    with nidaqmx.Task() as aitask:
        aitask.ai_channels.add_ai_voltage_chan("Mod2/ai0")
        voltage = aitask.read()
        print("Voltage :", voltage)

except Exception as e:
    print('Error in the code :', e)
