import windows_types
import ctypes


class _UNICODE_STRING(ctypes.Structure):
  _fields_ = [
    ("Length", windows_types.USHORT),
    ("MaximumLength", windows_types.USHORT),
    ("Buffer", windows_types.PWSTR)
  ]
UNICODE_STRING = _UNICODE_STRING
PUNICODE_STRING = ctypes.POINTER(UNICODE_STRING)
PCUNICODE_STRING = ctypes.POINTER(UNICODE_STRING)

