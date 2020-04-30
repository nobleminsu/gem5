#ifndef __LEARNING_GEM5_HELLO_OBJECT_HH__
#define __LEARNING_GEM5_HELLO_OBJECT_HH__

#include "params/HelloObject2.hh"
#include "sim/sim_object.hh"

class HelloObject2 : public SimObject
{
  public:
    HelloObject2(HelloObject2Params *p);
};

#endif // __LEARNING_GEM5_HELLO_OBJECT_HH__