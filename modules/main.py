# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

import this
import time
import math
from datetime import datetime
import sys
from greet import supergreeting

# 1.
print(this)


# 2.
def wait(seconds):
    time.sleep(seconds)
    return


# 3.
def my_sin(float):
    return math.sin(float)


# 4.
def iso_now():
    return str(datetime.now().isoformat())


# 5.
def platform():
    return sys.platform


# 6.
def supergreeting_wrapper(name: str):
    return supergreeting(name)


wait(1)
my_sin(1.4)
iso_now()
platform()
supergreeting_wrapper('Bob')
