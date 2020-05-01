#ifndef __LEARNING_GEM5_HELLO_OBJECT_HH__
#define __LEARNING_GEM5_HELLO_OBJECT_HH__

#include "learning_gem5/goodbye_object2.hh"
#include "params/HelloObject2.hh"
#include "sim/sim_object.hh"

class HelloObject2 : public SimObject
{
  private:
    void processEvent();

    EventWrapper<HelloObject2, &HelloObject2::processEvent> event;

    GoodbyeObject2* goodbye2;

    std::string myName;

    Tick latency;

    int timesLeft;


  public:
    HelloObject2(HelloObject2Params *p);

    void startup();
};

#endif // __LEARNING_GEM5_HELLO_OBJECT_HH__
