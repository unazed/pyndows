import ctypes


BCryptCloseAlgorithmProvider = ctypes.windll.bcrypt.BCryptCloseAlgorithmProvider
BCryptCloseAlgorithmProvider.argtypes = (
  ctypes.c_void_p,  # hAlgorithm
  ctypes.c_ulong,  # dwFlags
)
BCryptCloseAlgorithmProvider.restype = ctypes.c_long  # NTSTATUS

def bcrypt_close_algorithm_provider(algorithm, flags):
  return BCryptCloseAlgorithmProvider(algorithm, flags)

