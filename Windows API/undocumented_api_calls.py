from ctypes import *
from ctypes import wintypes

# Setup of kernel32
kernel32 = windll.kernel32
# This is just stetically
SIZE_T = c_size_t

# Creating the function

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID # POinter to void object

# Parameters to the function

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40 # Protection


# We can now call the function

ptr = VirtualAlloc(None, 1024 * 4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

# Check for errors
error = GetLastError()

if error:
    print(error)
    print(WinError(error))

# Print wher we allocated the memory
print("VirtualAlloc: ", hex(ptr))

###

# Declaring the NTDLL version of Virtual Alloc
nt = windll.ntdll
# For the sake of simplicity
NTSTATUS = wintypes.DWORD
# Function definition 
NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = (wintypes.HANDLE, POINTER(wintypes.LPVOID),
                                    wintypes.ULONG, POINTER(wintypes.ULONG),
                                    wintypes.ULONG, wintypes.ULONG)
                            
NtAllocateVirtualMemory.restype = NTSTATUS


###

# Now that is defined we will interface with it
# We will use the CurrentProcess function defined as a special constant

handle = 0xffffffffffffffff # Pseudo handle (we dont need to call the function)
base_address = wintypes.LPVOID(0x0) 
# Parameters
zero_bits = wintypes.ULONG(0)
# Pointer to a variable that will receive the size
size = wintypes.ULONG(1024 * 12) # Large so we can see it in ProcessHacker 
PAGE_EXECUTE_READWRITE = 0x40 # Protection

# Calling the function
ptr2 = NtAllocateVirtualMemory(handle, byref(base_address), zero_bits, byref(size),
                                MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

# Verify if it succeeded
if ptr2 != 0:
    print("Error")
    print(ptr2)

# If there are not errors
print("NtAllocateVirtualMemory: ", hex(base_address.value))


input()

