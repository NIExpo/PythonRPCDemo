import rpyc


try:

    print('Connecting to Server')
    HOSTNAME    = '10.34.75.80'
    PORT        = 18861
    connection  = rpyc.connect(HOSTNAME, PORT)
    print('Connected to Server')

    #Expose Remote Modules
    nidaqmx                = connection.root.nidaqmx
    AcquisitionType        = connection.root.AcquisitionType
    TerminalConfiguration  = connection.root.TerminalConfiguration


    #import nidaqmx
    with nidaqmx.Task() as aitask:
        aitask.ai_channels.add_ai_voltage_chan("Mod6/ai0", terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0)
        aitask.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=10000)
        aitask.start()
        i=1
        while i==1:
            voltage = aitask.read(number_of_samples_per_channel=1000, timeout=30.0)
            print(voltage)

except Exception as e:
    print('Error in the code :', e)
