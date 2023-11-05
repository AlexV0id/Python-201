# Defining functions, constants and variables

from ctypes import *
from ctypes import wintypes

# This is just stetically
SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

# Parameters to the function

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40 # Protection

# Specific to x64 ASM
# This is how windows executes syscalls with the use of the 
# WIN 32 API
"""
mov r10, rcx
mov eax, 18h // this is our syscall number
syscall
return
"""

###

# To use the ASM code we will translate it to shellcode
# Then we put it somewhere in memory

# Function to verify if a call succeeded

def verify(x):
    if not x:
        raise WinError()

# Create out buffer containing the testing shellcode
buf = create_string_buffer(b"\xb8,\x05,\x00,\x00,\x00,\xc3")

# Get the address of where it is in memory
buf_addr = addressof(buf)
print("Buffer address:", hex(buf_addr))

# We will use VirtualProtect to change our memory protections

VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.LPDWORD)
VirtualProtect.restype = wintypes.INT

# Changing the memory protection, we can reuse th eone above 
# because it includes execute

old_protection = wintypes.DWORD(0)
protect = VirtualProtect(buf_addr, len(buf), PAGE_EXECUTE_READWRITE, byref(old_protection))
verify(protect)

# Making use of cfunctype to execute our shellcode
asm_type = CFUNCTYPE(c_int) # We are expecting a 5 to be returned
asm_function = asm_type(buf_addr) # Address of the shellcode

'''
r = asm_function()
print("The number is: ", hex(r))
'''

###

# Making our syscall with the method we used before
# It is doing what NtAllocateVirtualMemory does

buf2 = create_string_buffer(b"\x4c,\x8b,\xd1,\xb8,\x18,\x00,\x00,\x00,\x0f,\x05,\xc3")
buf_addr2 = addressof(buf2)
print("Buffer address 2: ", hex(buf_addr2))

# Enable execute memory protection again
old_protection = wintypes.DWORD(0)
protect = VirtualProtect(buf_addr2, len(buf2), PAGE_EXECUTE_READWRITE, byref(old_protection))
verify(protect)

# In the cfunctype we first return NT STATUS
# Then the arguments

syscall_type = CFUNCTYPE(NTSTATUS, wintypes.HANDLE, POINTER(wintypes.LPVOID),
                                    wintypes.ULONG, POINTER(wintypes.ULONG),
                                    wintypes.ULONG, wintypes.ULONG)

# Setting up the function 
syscall_function = syscall_type(buf_addr2)

# The execution is the same as the undocumented API lesson

handle = 0xffffffffffffffff 
base_address = wintypes.LPVOID(0x0) 
zero_bits = wintypes.ULONG(0)
size = wintypes.ULONG(1024 * 12) # How many kilobytes in Process Hacker
PAGE_EXECUTE_READWRITE = 0x40 # Protection

# Calling our new assembly function
ptr2 = syscall_function(handle, byref(base_address), zero_bits, byref(size),
                                MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

if ptr2 != 0:
    print("Error")
    print(ptr2)

# If there are not errors
print("Syscall Allocation: ", hex(base_address.value))


input()