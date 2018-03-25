import ctypes
from processentry32 import PROCESSENTRY32


Process32Next = ctypes.windll.kernel32.Process32Next
Process32Next.argtypes = (
  ctypes.c_uint32,  # hSnapshot
  ctypes.POINTER(PROCESSENTRY32),  # lppe
)
Process32Next.restype = ctypes.c_uint32  # BOOL

def process32_next(snapshot, lppe):
  return Process32Next(snapshot, lppe)

