from ctypes import *
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL

# We first need to find where this function is
MessageBoxA = windll.user32.MessageBoxA

# Define the argument types for the function
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)

# Define the Return Type also specified on the page
MessageBoxA.restype = INT

print(MessageBoxA)

# Now to scpecify the parameters
lpText = LPCSTR(b"Hello")
lpCaption = LPCSTR(b"Alex")
#Our type (copied from the page)
MB_OK = 0x00000000
# We can add other button
MB_OKCANCEL = 0x00000001

# The none is to specify the box has no owner
MessageBoxA(None, lpCaption, lpText, MB_OKCANCEL)

####

# Declaring our return function
GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = INT

# Specify the size of the buffer

buffer_size = DWORD(5) # DWORD is a 32 bit unsigned integer
buffer= create_string_buffer(buffer_size.value) # The buffer is th size of buffer_size
GetUserNameA(buffer, byref(buffer_size))
# This will print out our username
print(buffer.value)

# If there is an error we can use this API call for debugging

error = GetLastError()
if error:
    print(hex(error))
    # To print the full error message
    print(WinError(error))

## Now moving to structures

class RECT(Structure):
    _fields_ = [("left", c_long), 
                ("top", c_long,),
                ("right", c_long),
                ("bottom", c_long)]

# Now that the scrutcture is defined we can use it

rect = RECT()
print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)

# Modify a value in the group
rect.left = 1
print("Rect left is {}".format(rect.left))

# Now to define the GetWindowRect function

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HANDLE, POINTER(RECT))
# Return type
GetWindowRect.restype = BOOL

# To setup a handle so wecan use the function

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))

# Now we print the dimensions of the window

print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)