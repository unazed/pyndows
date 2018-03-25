import ctypes


GetProcessImageFileNameW = ctypes.windll.psapi.GetProcessImageFileNameW
GetProcessImageFileNameA = ctypes.windll.psapi.GetProcessImageFileNameA
GetProcessImageFileNameW.argtypes = (
  ctypes.c_void_p,  # HANDLE
  ctypes.c_wchar*260,  # lpImageFileName
  ctypes.c_long  # nSize
)
GetProcessImageFileNameA.argtypes = (
  ctypes.c_void_p,  # HANDLE
  ctypes.c_char*260,  # lpImageFileName
  ctypes.c_long  # nSize
)
GetProcessImageFileNameW.restype = ctypes.c_long  # DWORD
GetProcessImageFileNameA.restype = ctypes.c_long  # DWORD

def get_process_image_filename_ansi(handle, out, size):
    return GetProcessImageFileNameA(handle, out, size)
def get_process_image_filename_unicode(handle, out, size):
    return GetProcessImageFileNameW(handle, out, size)

