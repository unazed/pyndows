import ctypes


class PROCESSENTRY32(ctypes.Structure):
  _fields_ = [
    ("dwSize",              ctypes.c_ulong),
    ("cntUsage",            ctypes.c_ulong),
    ("th32ProcessID",       ctypes.c_ulong),
    ("th32DefaultHeapID",   ctypes.POINTER(ctypes.c_ulong)),
    ("th32ModuleID",        ctypes.c_ulong),
    ("cntThreads",          ctypes.c_ulong),
    ("th32ParentProcessID", ctypes.c_ulong),
    ("pcPriClassBase",      ctypes.c_long),
    ("dwFlags",             ctypes.c_ulong),
    ("szExeFile",           ctypes.c_char * 260)
  ]
