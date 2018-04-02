import ctypes
import platform


ptr = ctypes.POINTER
x64 = platform.architecture()[0] == '64bit'
x86 = platform.architecture()[0] == '32bit'

if x64:
  ULONG_PTR = ctypes.c_uint64
else:
  ULONG_PTR = ctypes.c_ulong
BOOL = ctypes.c_int
BOOLEAN = ctypes.c_ubyte
BYTE = ctypes.c_ubyte
CCHAR = ctypes.c_char
COLORREF = ctypes.c_ulong
DWORD = ctypes.c_ulong
DWORDLONG = ctypes.c_uint64
DWORD_PTR = ULONG_PTR
DWORD32 = ctypes.c_uint
DWORD64 = ctypes.c_int64
FLOAT = ctypes.c_float
HACCEL = ctypes.c_void_p
if x64:
  HALF_PTR = ctypes.c_int
else:
  HALF_PTR = ctypes.c_short
HANDLE = ctypes.c_void_p
HBITMAP = ctypes.c_void_p
HBRUSH = ctypes.c_void_p
HCOLORSPACE = ctypes.c_void_p
HCONV = ctypes.c_void_p
HCONVLIST = ctypes.c_void_p
HCURSOR = ctypes.c_void_p
HDC = ctypes.c_void_p
HDDEDATA = ctypes.c_void_p
HDESK = ctypes.c_void_p
HDROP = ctypes.c_void_p
HDWP = ctypes.c_void_p
HENHMETAFILE = ctypes.c_void_p
HFILE = ctypes.c_int
HFONT = ctypes.c_void_p
HGDIOBJ = ctypes.c_void_p
HGLOBAL = ctypes.c_void_p
HHOOK = ctypes.c_void_p
HICON = ctypes.c_void_p
HINSTANCE = ctypes.c_void_p
HKEY = ctypes.c_void_p
HKL = ctypes.c_void_p
HLOCAL = ctypes.c_void_p
HMENU = ctypes.c_void_p
HMETAFILE = ctypes.c_void_p
HMODULE = ctypes.c_void_p
HMONITOR = ctypes.c_void_p
HPALETTE = ctypes.c_void_p
HPEN = ctypes.c_void_p
HRESULT = ctypes.c_long
HRGN = ctypes.c_void_p
HRSRC = ctypes.c_void_p
HSZ = ctypes.c_void_p
HWINSTA = ctypes.c_void_p
HWND = ctypes.c_void_p
INT = ctypes.c_int
if x64:
  INT_PTR = ctypes.c_int64
else:
  INT_PTR = ctypes.c_int
INT8 = ctypes.c_char
INT16 = ctypes.c_short
INT32 = ctypes.c_int
INT64 = ctypes.c_int64
LANGID = ctypes.c_ushort
LCID = ctypes.c_ulong
LCTYPE = ctypes.c_ulong
LGRPID = ctypes.c_ulong
LONG = ctypes.c_long
if not x86:
  LONGLONG = ctypes.c_int64
else:
  LONGLONG = ctypes.c_double
if x64:
  LONG_PTR = ctypes.c_int64
else:
  LONG_PTR = ctypes.c_long
LONG32 = ctypes.c_int
LONG64 = ctypes.c_int64
LPARAM = LONG_PTR
LPBOOL = ptr(ctypes.c_int)
LPBYTE = ptr(ctypes.c_ubyte)
LPCOLORREF = ptr(ctypes.c_ulong)
#LPCTSTR =
LPCVOID = ctypes.c_void_p
LPCWSTR = ptr(ctypes.c_wchar)
LPDWORD = ptr(ctypes.c_ulong)
LPHANDLE = ptr(ctypes.c_void_p)
LPINT = ptr(ctypes.c_int)
LPLONG = ptr(ctypes.c_long)
LPSTR = ptr(ctypes.c_char)
#LPTSTR = 
LPVOID = ctypes.c_void_p
LPWORD = ptr(ctypes.c_ushort)
LPWSTR = ptr(ctypes.c_wchar)
LRESULT = ptr(ctypes.c_long)
PBOOL = ptr(ctypes.c_int)
PBOOLEAN = ptr(ctypes.c_ubyte)
PBYTE = ptr(ctypes.c_ubyte)
PCHAR = ptr(ctypes.c_char)
PCSTR = ptr(ctypes.c_char)
#PCTSTR =
PCWSTR = ptr(ctypes.c_wchar)
PDWORD = ptr(ctypes.c_ulong)
PDWORDLONG = ptr(ctypes.c_uint64)
PDWORD_PTR = ptr(DWORD_PTR)
PDWORD32 = ptr(ctypes.c_uint)
PDWORD64 = ptr(ctypes.c_ulong)
PFLOAT = ptr(ctypes.c_float)
PHALF_PTR = ptr(HALF_PTR)
PHANDLE = ptr(ctypes.c_void_p)
PHKEY = ptr(ctypes.c_void_p)
PINT = ptr(ctypes.c_int)
PINT_PTR = ptr(INT_PTR)
PINT8 = ptr(ctypes.c_char)
PINT16 = ptr(ctypes.c_short)
PINT32 = ptr(ctypes.c_int)
PINT64 = ptr(ctypes.c_int64)
PLCID = ptr(ctypes.c_ulong)
PLONG = ptr(ctypes.c_long)
PLONGLONG = ptr(LONGLONG)
PLONG_PTR = ptr(LONG_PTR)
PLONG32 = ptr(ctypes.c_int)
PLONG64 = ptr(ctypes.c_int64)
#if x64:
#  POINTER_32 = ...
#else:
#  POINTER_32 = ...
# how would i define __ptr32, __ptr64, __sptr and __uptr?
PSHORT = ptr(ctypes.c_short)
PSIZE_T = ptr(ULONG_PTR)
PSSIZE_T = ptr(LONG_PTR)
PSTR = ptr(ctypes.c_char)
#PTBYTE = 
#PTCHAR =
#PTSTR =
PUCHAR = ptr(ctypes.c_ubyte)
if x64:
  UHALF_PTR = ctypes.c_uint
else:
  UHALF_PTR = ctypes.c_short
PUHALF_PTR = ptr(UHALF_PTR)
PUINT = ptr(ctypes.c_uint)
if x64:
  UINT_PTR = ctypes.c_uint64
else:
  UINT_PTR = ctypes.c_uint
PUINT_PTR = ptr(UINT_PTR)
PUINT8 = ptr(ctypes.c_ubyte)
PUINT16 = ptr(ctypes.c_ushort)
PUINT32 = ptr(ctypes.c_uint)
PUINT64 = ptr(ctypes.c_uint64)
PULONG = ptr(ctypes.c_ulong)
if not x64:
  ULONGLONG = ctypes.c_uint64
else:
  ULONGLONG = ctypes.c_double
PULONGLONG = ptr(ULONGLONG)
if x64:
  ULONG_PTR = ctypes.c_uint64
else:
  ULONG_PTR = ctypes.c_ulong
PULONG_PTR = ptr(ULONG_PTR)
PULONG32 = ptr(ctypes.c_uint)
PULONG64 = ptr(ctypes.c_uint64)
PUSHORT = ptr(ctypes.c_ushort)
PVOID = ctypes.c_void_p
PWCHAR = ptr(ctypes.c_wchar)
PWORD = ptr(ctypes.c_ushort)
PWSTR = ptr(PWCHAR)
QWORD = ctypes.c_uint64
SC_HANDLE = ctypes.c_void_p
SC_LOCK = ctypes.c_void_p
SERVICE_STATUS_HANDLE = ctypes.c_void_p
SHORT = ctypes.c_short
SIZE_T = ULONG_PTR
SSIZE_T = LONG_PTR
#TBYTE =
#TCHAR =
UCHAR = ctypes.c_ubyte
UINT = ctypes.c_uint
UINT8 = ctypes.c_ubyte
UINT16 = ctypes.c_ushort
UINT32 = ctypes.c_uint
UINT64 = ctypes.c_uint64
ULONG = ctypes.c_ulong
ULONG32 = ctypes.c_uint
ULONG64 = ctypes.c_uint64
USHORT = ctypes.c_ushort
USN = LONGLONG
#VOID = ctypes.c_void ## impossible
WCHAR = ctypes.c_wchar
WORD = ctypes.c_ushort
WPARAM = UINT_PTR

# NOTE: UNICODE_STRING, PUNICODE_STRING and PCUNICODE_STRING are defined in windows_structures.py

# NOTE: type definitions which vary based on whether UNICODE is defined are *not* defined because there's no real way (that i know of) which you can equivalently check for UNICODE definition

