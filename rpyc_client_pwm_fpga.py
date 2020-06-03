import rpyc


try:

    print('Connecting to Server')
    HOSTNAME    = '10.34.75.80'
    PORT        = 18861
    connection  = rpyc.connect(HOSTNAME, PORT)
    print('Connected to Server')

    #Expose Remote Modules
    nifpga   = connection.root.nifpga
    Session  = connection.root.Session

    #import nifpga
    with Session(bitfile="pwmmeasurement_FPGATarget2_PWMMeasurement_6s5r+omzCq8.lvbitx", resource="RIO0") as session:
        session.reset()
        session.run()
        low_period = session.registers['Low Period (Ticks)']
        high_period = session.registers['High Period (Ticks)']
        while True:
            low_data = low_period.read()
            high_data = high_period.read()
            print(low_data, high_data)

except Exception as e:
    print('Error in the code :', e)
