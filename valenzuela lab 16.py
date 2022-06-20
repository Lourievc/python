import socket
from time import sleep

target_host = input("Please enter the target IP: ")

results = []

def tcp_scan():

    for port in range(7995,8005):
        socket.setdefaulttimeout(0.1)
        print("Scanning port " + str(port) + " on " + target_host)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = client.connect_ex((target_host,port))
        if result == 0:
            results.append("\nOpen connection found on TCP port " + str(port))
        client.close()
    return results

def udp_scan():

    for port in range(7995,8005):
        print("Scanning port " + str(port) + " on " + target_host)
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket.setdefaulttimeout(0.1)
        result = client.connect_ex((target_host,port))
        if result == 0:
            results.append("\nOpen connection found on UDP port " + str(port))
    client.close()
    return results

print("\nStarting TCP scan\n")
sleep(1)
tcp_scan()
print("\nStarting UDP scan\n")
sleep(1)
udp_scan()

for line in tcp_scan():
    print(line)


input_file = input('Enter the name of the file you want to write the scans to: ')
f = open(input_file, "a")
f.write(line)
#f.write(line1)
f.close()


