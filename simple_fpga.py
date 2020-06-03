from nifpga import Session
import time

with Session(bitfile="PWM.lvbitx", resource="RIO0") as session:
    #session.reset()
    session.download()
    session.run()
    low_period = session.registers['Low Period (Ticks)']
    high_period = session.registers['High Period (Ticks)']
    iteration = session.registers['Iteration']
    while True:
        low_data = low_period.read()
        high_data = high_period.read()
        iteration_number = iteration.read()
        print(low_data, high_data, iteration_number)
        time.sleep(0.01)
