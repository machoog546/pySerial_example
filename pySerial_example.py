import serial, time

# This is the name of the port/path to your serial connection (Testing in Windows ATM)
SERIAL_PORT = 'COM3'
SERIAL_RATE = 9600


def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

    cmds = ['term le 0\r', "conf t\r", "exit\r", "show run\r","show inven\r", "\r"] #commands being ran on small Cisco POE switch

    ser.write(b'\r')
    check = ser.readline().decode('utf-8')
    print(check)

    if check == '\r\n':     #if they
        ser.write(b'en\r')
        ser.write(b'cisco')
        check2 = ser.readline().decode('utf-8')
        print(check2)

    output = []
    ser.write(b"\r")
    time.sleep(1)
    for command in cmds:
        ser.write(bytes(command, 'utf-8'))
        while True:
            # using ser.readline() will only kick back a line at a time?
            # Use the loop to keep reading till it find's it match


            reading = ser.readline().decode('utf-8')

            # reading is a string...do whatever you want from here
            print(reading) #Allows us to see what it's returning

            output.append(reading) #Add's it to a list

            if "TestSwitch#" in reading or "end\r" in reading:
                break

    #everything south needs to be fixed...later
    output2 = "".join(output)
    output2 = output2.replace('\r\n', '\r')

    print("The following are the answers: \n")
    print(output)
    print(output2)


if __name__ == "__main__":
    main()
