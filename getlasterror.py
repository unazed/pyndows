import ctypes


GetLastError = ctypes.windll.kernel32.GetLastError
GetLastError.argtypes = ()
GetLastError.restype = ctypes.c_uint32

def get_last_error():
  return GetLastError()

