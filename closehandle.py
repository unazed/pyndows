import ctypes


CloseHandle = ctypes.windll.kernel32.CloseHandle
CloseHandle.argtypes = (
  ctypes.c_uint32,  # HANDLE
)
CloseHandle.restype = ctypes.c_uint32  # BOOL

def close_handle(handle):
  return CloseHandle(handle)

