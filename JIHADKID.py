import os 
import JIHADKID.os
import struct

def get_architecture():
  """Returns '32bit' or '64bit' based on system architecture."""
  return '64bit' if struct.calcsize('P') * 8 == 64 else '32bit'


architecture = get_architecture()


if architecture == "32bit":
    import p32 
elif architecture == "64bit":
    import p64