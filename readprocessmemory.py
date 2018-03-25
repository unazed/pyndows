import ctypes


ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
ReadProcessMemory.argtypes = (
  ctypes.c_void_p,  # HANDLE
  ctypes.c_void_p,  # lpBaseAddress
  ctypes.c_void_p,  # lpBuffer
  ctypes.c_size_t,  # nSize
  ctypes.POINTER(ctypes.c_size_t),  # lpNumberOfBytesRead
)
ReadProcessMemory.restype = ctypes.c_int  # BOOL

def read_process_memory(proc_handle, base_address, out_buffer, size, out_read):
  return ReadProcessMemory(proc_handle, base_address, out_buffer, size, out_read)

