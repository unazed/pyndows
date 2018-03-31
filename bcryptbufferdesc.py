from bcryptbuffer import BCryptBuffer
import ctypes


class BCryptBufferDesc(ctypes.Structure):
  _fields_ = [
    ("ulVersion", ctypes.c_ulong),
    ("cBuffers", ctypes.c_ulong),
    ("pBuffers", ctypes.POINTER(BCryptBuffer))
  ]

