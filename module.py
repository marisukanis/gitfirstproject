"""
A module can be deduced as a library
Each python file ".py" is treated as a module

import <<filename>> #imports everything from a file
    import os
    import math
import <<filename>> as <<alias>> #renaming a module/alias
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

from <<filename>> import <<Class, function>>    #import specific items
    from collections import Counter
"""

from functions import my_name
from pythonProject.main import print_something  #imports from upper folder

my_name("Maris", 200)

#pip freeze > requirements.txt - create a requirements text file
# and gives you a list of all the packages that are needed

#pip install -r requirements.txt - this way you can download all
#packacges in one time from the file


