import ctypes


WriteProcessMemory = ctypes.windll.kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = (
  ctypes.c_void_p,  # HANDLE
  ctypes.c_void_p,  # lpBaseAddress
  ctypes.c_void_p,  # lpBuffer
  ctypes.c_size_t,  # nSize
  ctypes.POINTER(ctypes.c_size_t)  # lpNumberOfBytesWritten
)
WriteProcessMemory.restype = ctypes.c_int  # BOOL

def write_process_memory(proc_handle, base_address, out_buffer, size, out_read):
  return WriteProcessMemory(proc_handle, base_address, out_buffer, size, out_read)

