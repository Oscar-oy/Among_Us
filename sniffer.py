import socket
import struct
import textwrap
#It doesn´t allow us to do it

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW)

    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))

# Unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

'''
https://docs.python.org/3/library/struct.html

Struct function
The struct module in Python is used to convert native Python data types such as 
strings and numbers into a string of bytes and vice versa.
 What this means is that users can parse binary files of data stored in C structs in Python.

It is used mostly for handling binary data stored in files or from network connections, among other sources.

Struct Functions
-> struct.pack()
is the function that converts a given list of values into their corresponding string representation.
 It requires the user to specify the format and order of the values that need to be converted.

These format strings are made up of format characters. Some common ones are:
c - character
s - char[]
i - integer
f - float

i.e.
import struct

packed = struct.pack('i 4s f', 10, b'John', 2500)
print(packed)

-> struct.unpack()
This function converts the strings of binary representations to their original form according to the specified format.
The return type of struct.unpack() is always a tuple.

i.e.
import struct

packed = b'\n\x00\x00\x00John\x00@\x1cE'
unpacked = struct.unpack('i 4s f', packed)
print(unpacked)


-> struct.calcsize()
This function calculates the size of the String representation of struct with a given format string.

i.e.
import struct

size = struct.calcsize('i 4s f')
print("Size in bytes: {}".format(size))
'''
'''
https://docs.python.org/3/library/socket.html

Socket

socket.ntohs(x)
Convert 16-bit positive integers from network to host byte order. 
On machines where the host byte order is the same as network byte order, 
this is a no-op; otherwise, it performs a 2-byte swap operation.

Creating sockets
The following functions all create socket objects.

class socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)

socket.AF_PACKET¶
socket.PF_PACKET
PACKET_*
Many constants of these forms, documented in the Linux documentation, are also defined in the socket module.

Raw socket significa que puede determinar cada sección del paquete, ya sea encabezado o carga útil. 
Tenga en cuenta que el socket sin procesar es una palabra general. Clasifico el socket sin procesar en: 
Network Socket yd Data-Link Socket (o alternativamente L3 Socket y L2 Socket)

'''

#Return properly formatted MAC address (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()



main()

