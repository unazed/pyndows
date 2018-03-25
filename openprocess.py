import ctypes


OpenProcess = ctypes.windll.kernel32.OpenProcess
OpenProcess.argtypes = (
  ctypes.c_ulong,  # dwDesiredAccess
  ctypes.c_uint,  # bInheritHandle
  ctypes.c_ulong,  # dwProcessID
)
OpenProcess.restype = ctypes.c_void_p # HANDLE

def open_process(desired_access, inherit_handle, process_id):
  return OpenProcess(desired_access, inherit_handle, process_id)

