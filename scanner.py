import socket 
import ipaddress
import time
from concurrent.futures import ThreadPoolExecutor


# IP input validation

while True: 
    target = input("Enter target IP: ")

    try:
        ipaddress.IPv4Address(target)
        break
    
    except ValueError:
        print("Invalid IP address. Enter a valid IPv4 address.")

# Port input validation

while True: 
    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if 1 <= start_port <= end_port <= 65535:
            break

        else:
            print("Invalid port range. Enter a valid port range between 1 and 65535")

    except ValueError:
        print("Invalid input. Numbers only.")

# Scanner


print("PYTHON SCANNER")

print(f"Target: {target}")
print(f"\nscanning ports...\n")

open_ports = 0

start_time = time.perf_counter()

for port in range(start_port, end_port + 1):
        scanner = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )

        scanner.settimeout(0.5)

        result = scanner.connect_ex((target, port))

        if result == 0:
            open_ports += 1

            #Service detection

            try: 
                service = socket.getservbyport(port, "tcp")
                print(f"[+] Port {port} OPEN - Service: {service}")

            except OSError:
                print(f"[+] Port {port} OPEN - Service: Unknown")               

        else:
            print(f"[-] Port {port} CLOSED")
        
        
        scanner.close()

total_ports = end_port - start_port + 1

end_time = time.perf_counter()
elapsed_time = end_time - start_time

#Results
print("\nScan completed")
print(f"Total ports scanned: {total_ports}")
print(f"Total open ports: {open_ports}")
print( f"Ports scanned in: {elapsed_time:.2f} seconds")