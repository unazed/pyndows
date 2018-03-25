import utils
import ctypes
from getprocessimagefilename import *

try:
  input = raw_input
except NameError:
  pass


buffer_ = ctypes.create_string_buffer(260)

process = input("Process name: ") 

with utils.get_handle_by_process_name(process) as proc_handle:
  get_process_image_filename_ansi(proc_handle, buffer_, 260)

print("{}: {}".format(process, buffer_.value.decode()))
