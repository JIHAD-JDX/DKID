import os,platform
JIHADKID=platform.architecture()[0]
if JIHADKID=="32bit":
    __import__("p32")
elif JIHADKID=="64bit":
    __import__("p64")