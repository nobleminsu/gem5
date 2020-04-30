from m5.params import *
from m5.SimObject import SimObject

class HelloObject2(SimObject):
    type = 'HelloObject2'
    cxx_header = "learning_gem5/hello_object2.hh"