import ctypes


GetProcessId = ctypes.windll.kernel32.GetProcessId
GetProcessId.argtypes = (
  ctypes.c_void_p,  # HANDLE        
)
GetProcessId.restype = ctypes.c_ulong  # DWORD

def get_process_id(handle):
    return GetProcessId(handle)

