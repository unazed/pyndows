import ctypes


CreateToolhelp32Snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot
CreateToolhelp32Snapshot.argtypes = (
  ctypes.c_uint32,  # dwFlags
  ctypes.c_uint32   # th32ProcessID
)
CreateToolhelp32Snapshot.restype = ctypes.c_uint32  # HANDLE

def create_toolhelp32_snapshot(flags, pid):
  return CreateToolhelp32Snapshot(flags, pid)

