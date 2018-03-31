import ctypes


BCryptDecrypt = ctypes.windll.bcrypt.BCryptDecrypt
BCryptDecrypt.argtypes = (
  ctypes.c_void_p,  # hKey
  ctypes.POINTER(ctypes.c_uchar),  # pbInput
  ctypes.c_ulong,  # cbInput
  ctypes.c_void_p,  # pPaddingInfo
  ctypes.POINTER(ctypes.c_uchar),  # pbIV
  ctypes.c_ulong,  # cbIV
  ctypes.POINTER(ctypes.c_uchar),  # pbOutput
  ctypes.c_ulong,  # cbOutput
  ctypes.POINTER(ctypes.c_ulong),  # pcbResult
  ctypes.c_ulong,  # dwFlags
)
BCryptDecrypt.restype = ctypes.c_long  # NTSTATUS

def bcrypt_decrypt(key, input1, input2, padding_info, iv1, iv2, output1, output2, result, flags):
  return BCryptDecrypt(key, input1, input2, padding_info, iv1, iv2, output1, output2, result, flags)

