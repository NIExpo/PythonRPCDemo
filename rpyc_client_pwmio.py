import rpyc


try:

    print('Connecting to Server')
    HOSTNAME    = '10.34.75.80'
    PORT        = 18861
    connection  = rpyc.connect(HOSTNAME, PORT)
    print('Connected to Server')

    #Expose Remote Modules
    nidaqmx            = connection.root.nidaqmx
    AcquisitionType    = connection.root.AcquisitionType

    #configure and start ci task for pwm
    with nidaqmx.Task() as citask, nidaqmx.Task() as cotask:
        citask.ci_channels.add_ci_pulse_chan_freq("Mod8/ctr2")
        cotask.co_channels.add_co_pulse_chan_freq("Mod7/ctr1", freq=100.0, duty_cycle=0.5)

        cotask.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
        cotask.start()

        data    = citask.read(timeout=30)
        print("1 Channel 1 Sample Read: ", data)
        data    = citask.read(number_of_samples_per_channel=8,timeout=30)
        print("1 Channel N Samples Read: ", data)


except Exception as e:
    print('Error in the code :', e)
