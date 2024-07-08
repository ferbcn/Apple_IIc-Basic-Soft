import serial
import time

def send_file_over_serial(file_path, port, baud_rate=9600, delay=1):
    # Open the serial connection
    ser = serial.Serial(port, baud_rate)
    print(f"Opened serial port {port} at {baud_rate} baud.")

    try:
        with open(file_path, 'r') as file:
            # Read the file line by line
            for line in file:
                # Strip any newline characters from the line
                line = line.strip()
                # Send the line over the serial connection
                ser.write(line.encode('utf-8'))
                ser.write(b'\r')  # Send newline character
                print(f"Sent: {line}")
                # Wait for a specified delay
                time.sleep(delay)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the serial connection
        ser.close()
        print("Closed serial port.")

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


if __name__ == "__main__":
    # Replace 'textfile.txt' with the path to your text file
    # Replace 'COM3' with your serial port (e.g., '/dev/ttyUSB0' on Linux or 'COM3' on Windows)
    # Select Serial device
    dev_name = list_devices_and_select()
    send_file_over_serial('basic.txt', dev_name, baud_rate=300, delay=0.7)
