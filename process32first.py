import ctypes
from processentry32 import PROCESSENTRY32


Process32First = ctypes.windll.kernel32.Process32First
Process32First.argtypes = (
  ctypes.c_uint32,  # hSnapshot
  ctypes.POINTER(PROCESSENTRY32)  # lppe
)
Process32First.restype = ctypes.c_uint32  # BOOL

def process32_first(snapshot, lppe):
  return Process32First(snapshot, lppe)

