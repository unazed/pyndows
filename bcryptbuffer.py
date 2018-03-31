import ctypes


class BCryptBuffer(ctypes.Structure):
  _fields_ = [
    ("cbBuffer", ctypes.c_ulong),
    ("BufferType", ctypes.c_ulong),
    ("pvBuffer", ctypes.c_void_p)
  ]

