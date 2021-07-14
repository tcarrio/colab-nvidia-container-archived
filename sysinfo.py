#!/usr/bin/env python3

'''
Provides system information such as kernel version and Linux distribution
to determine base image requirements of Colab runtime environment
'''

import subprocess as sp

def print_stdout(prefix, completed_process):
  print("%s:\n%s\n" % (prefix, completed_process.stdout.decode("utf-8")))

spargs = {"check": True, "capture_output": True}

kernel_info = sp.run(["/bin/uname", "-a"], **spargs)
print_stdout("kernel info", kernel_info)

distro_info = sp.run(["cat", "/etc/os-release"], **spargs)
print_stdout("distro info", distro_info)

import sys
print("Runtime version:\n%s\n" % sys.version)

py2_version = sp.run(["python2", "--version"], **spargs)
print_stdout("python2 info", py2_version)

py3_version = sp.run(["python3", "--version"], **spargs)
print_stdout("python3 info", py3_version)
