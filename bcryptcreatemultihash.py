import ctypes


BCryptCreateMultiHash = ctypes.windll.bcrypt.BCryptCreateMultiHash
BCryptCreateMultihash.argtypes = (
  ctypes.c_void_p,  # hAlgorithm
  ctypes.POINTER(ctypes.c_void_p),  # phHash
  ctypes.c_ulong,  # nHashes
  ctypes.POINTER(ctypes.c_uchar),  # pbHashObject
  ctypes.c_ulong,  # cbHashObject
  ctypes.POINTER(ctypes.c_uchar),  # pbSecret
  ctypes.c_ulong,  # cbSecret
  ctypes.c_ulong  # dwFlags
)
BCryptCreateMultiHash.restype = ctypes.c_long  # NTSTATUs


def bcrypt_create_multi_hash(algorithm, hash_, hashes, hashobject1, hashobject2, secret1, secret2, flags):
  return BCryptCreateMultiHash(algorithm, hash_, hashes, hashobject1, hashobject2, secret1, secret2, flags)

