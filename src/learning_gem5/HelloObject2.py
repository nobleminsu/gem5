from m5.params import *
from m5.SimObject import SimObject

class HelloObject2(SimObject):
    type = 'HelloObject2'
    cxx_header = "learning_gem5/hello_object2.hh"

    time_to_wait = Param.Latency("Time before firing the event")
    number_of_fires = Param.Int(1, "Number of times to fire the event before "
                                    "goodbye")
    goodbye_object2 = Param.GoodbyeObject2("A goodbye object")


class GoodbyeObject2(SimObject):
    type = 'GoodbyeObject2'
    cxx_header = "learning_gem5/goodbye_object2.hh"

    buffer_size = Param.MemorySize('1kB',
                                   "Size of buffer to fill with goodbye")
    write_bandwidth = Param.MemoryBandwidth('100MB/s', "Bandwidth to fill "
                                            "the buffer")