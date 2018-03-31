import ctypes


BCryptCreateHash = ctypes.windll.bcrypt.BCryptCreateHash
BCryptCreateHash.argtypes = (
  ctypes.c_void_p,  # hAlgorithm
  ctypes.POINTER(ctypes.c_void_p),  # phHash
  ctypes.POINTER(ctypes.c_uchar),  # pbHashObject
  ctypes.c_ulong,  # cbHashObject
  ctypes.POINTER(ctypes.c_uchar),  # pbSecret
  ctypes.c_ulong,  # cbSecret
  ctypes.c_ulong  # dwFlags
)
BCryptCreateHash.restype = ctypes.c_long  # NTSTATUS

def bcrypt_create_hash(algorithm, hash_, hashobject1, hashobject2, secret1, secret2, flags):
  return BCryptCreateHash(algorithm, hash_, hashobject1, hashobject2, secret1, secret2, flags)

