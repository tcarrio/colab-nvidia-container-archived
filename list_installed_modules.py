#!/usr/bin/env python3

'''
Inspects the current runtime using pip to determine installed packages,
given that the environment has the `pip` module available.

This is used to determine the latest Python modules requirements.txt
to mirror the runtime environment provided in Colab.
'''

from pip import _internal as pip

for module in pip.commands.freeze.freeze():
  print(module)
