# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:22:37 2020

@author: DELL
"""

import re

email = "john@google.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern,email)
print(ans)
