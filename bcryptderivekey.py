from bcryptbufferdesc import BCryptBufferDesc
import ctypes


BCryptDeriveKey = ctypes.windll.bcrypt.BCryptDeriveKey
BCryptDervieKey.argtypes = (
  ctypes.c_void_p,  # hSharedSecret
  ctypes.POINTER(ctypes.c_wchar),  # pwszKDF
  ctypes.POINTER(BCryptBufferDesc),  # pParameterList
  ctypes.POINTER(ctypes.c_uchar),  # pbDerivedKey
  ctypes.c_ulong,  # cbDerivedKey
  ctypes.POINTER(ctypes.c_ulong),  # pcbResult
  ctypes.c_ulong,  # dwFlags
)
BCryptDeriveKey.restype = ctypes.c_long  # NTSTATUS

def bcrypt_derive_key(shared_secret, kdf, param_list, derived_key1, derived_key2, result, flags):
  return BCryptDeriveKey(shared_secret, kdf, param_list, derived_key1, derived_key2, result, flags)

