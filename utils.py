import ctypes
from processentry32 import PROCESSENTRY32
from createtoolhelp32snapshot import create_toolhelp32_snapshot
from process32first import process32_first
from process32next import process32_next
from openprocess import open_process
from closehandle import close_handle
from getlasterror import get_last_error
from getprocessimagefilename import get_process_image_filename_unicode


class get_handle_by_process_name(object):
  def __init__(self, proc_name):
    self.proc_name = proc_name
  def __enter__(self):
    entry = PROCESSENTRY32()
    entry.dwSize = ctypes.sizeof(PROCESSENTRY32)
    snapshot = create_toolhelp32_snapshot(0x2, 0)
    self._process = None

    if process32_first(snapshot, ctypes.pointer(entry)) == 1:
      while process32_next(snapshot, ctypes.pointer(entry)) == 1:
        if entry.szExeFile.decode() == self.proc_name:
          self._process = open_process(0x1f0fff, 0, entry.th32ProcessID)
          break
    self._snapshot = snapshot
    return self._process
  def __exit__(self, *args):
    close_handle(self._snapshot)
    if self._process is not None:
      close_handle(self._process)


def get_process_path_by_name(proc_name):
  buffer_ = ctypes.create_unicode_buffer(260)
  with get_handle_by_process_name(proc_name) as proc_handle:
    get_process_image_filename_unicode(proc_handle, buffer_, 260)
  return buffer_.value.decode()

