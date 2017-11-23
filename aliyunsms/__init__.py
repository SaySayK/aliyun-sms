# usr/bin/env python
# -*- coding: utf-8 -*-

# Add dummy imports for pyinstaller. These should probably belong in
# future since they are needed for pyinstaller to properly handle
# future.standard_library.install_aliases()
if 0:
    import UserList
    import UserString
    import UserDict
    import itertools
    import collections
    import future.backports.misc
    import commands
    import base64
    import __buildin__
    import math
    import reprlib
    import functools
    import re
    import subprocess