import serial


def list_devices_and_select():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    print("Available serial ports:")
    ports_list = [(i, port.device) for i, port in enumerate(ports)]
    for port in ports_list:
        print(f"{port[0]}: {port[1]}")
    dev_num = None
    while not dev_num in [str(p[0]) for p in ports_list]:
        dev_num = input("Enter the port number: ")
    return ports_list[int(dev_num)][1]


def echo_server(port, baud_rate=300):
    # Open the serial connection
    ser = serial.Serial(port, baud_rate)
    print(f"Opened serial port {port} at {baud_rate} baud.")
    try:
        while True:
            # Wait for a line to be received
            line = ser.readline()
            # Print the received line
            print(f"Received: {line.decode('utf-8').strip()}")
            # Echo the line back
            ser.write(line)
    except KeyboardInterrupt:
        pass
    finally:
        # Close the serial connection
        ser.close()
        print("Closed serial port.")


if __name__ == "__main__":
    dev_name = list_devices_and_select()
    echo_server(dev_name, baud_rate=300)