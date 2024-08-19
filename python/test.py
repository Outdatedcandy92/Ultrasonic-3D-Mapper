import serial
import time
import os
import subprocess

ser = serial.Serial('COM4', 9600)
time.sleep(2)
ser.flushInput()
ser.flushOutput()

ser.write(b'runfunc\n')

def read_data():
    storing_data = False
    main_started = False

    try:
        with open('data.txt', 'ab') as file:  
            while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').rstrip()
                    print(f"Received: {line}")  

                    if line == "Mapping Started":
                        storing_data = True
                    elif line == "Mapping Finished":
                        storing_data = False
                        print("Mapping Data Finished")
                    elif storing_data:
                        print(f"New Data: {line}")
                        file.write((line + '\n').encode('utf-8')) 
                        file.flush() 
                        os.fsync(file.fileno())  

                        if not main_started:
                            subprocess.Popen(['python', 'main.py'])
                            main_started = True
    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")
    finally:
        ser.close()  

if __name__ == "__main__":
    read_data()