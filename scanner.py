import socket
target = input("Enter target IP or domain: ")
ports = range(20,1025)
print(f"\nscanning {target}...\n")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"[OPEN] port {port}")
    s.close()
