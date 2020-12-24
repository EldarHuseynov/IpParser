import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack(
            b'256s',
            bytes(ifname[:15], 'ascii'))
        )[20:24])

print(get_ip_address('lo'))
