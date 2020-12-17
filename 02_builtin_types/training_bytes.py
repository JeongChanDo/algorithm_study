"""
byte, bytearray

byte : immutable type
bytearray : mutable type
"""

def print_name(name):
    print("\n### "+name+" ###")


blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print_name("bytes")
print(the_bytes)

the_bytes_array = bytearray(blist)
print_name("bytearray")
print(the_bytes_array)


print_name("immutable type")
try:
    the_bytes[1] = 127
except Exception as e:
    print(e)

the_bytes_array[1] = 127
print_name("mutable type")
print(the_bytes_array)