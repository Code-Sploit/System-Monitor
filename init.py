import sys
import os as cmd

os = sys.platform

if ("linux" in os):
    cmd.system("python3 src/linux_setup.py")
elif ("bsd" in os):
    cmd.system("python3 src/openbsd_setup.py")
