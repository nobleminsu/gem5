#include "learning_gem5/hello_object2.hh"

#include <iostream>

#include "debug/Hello.hh"

HelloObject2::HelloObject2(HelloObject2Params *params) :
    SimObject(params),
    event(*this),
    goodbye2(params->goodbye_object2),
    myName(params->name),
    latency(params->time_to_wait),
    timesLeft(params->number_of_fires)
{
    DPRINTF(Hello, "Created the hello object with the name %s\n", myName);
    panic_if(!goodbye2, "HelloObject must have a non-null GoodbyeObject");
}

HelloObject2*
HelloObject2Params::create()
{
    return new HelloObject2(this);
}

void
HelloObject2::processEvent()
{
    timesLeft--;
    DPRINTF(Hello, "Hello world! Processing the event! %d left\n", timesLeft);

    if (timesLeft <= 0) {
        DPRINTF(Hello, "Done firing!\n");
        goodbye2->sayGoodbye(myName);
    } else {
        schedule(event, curTick() + latency);
    }
}

void
HelloObject2::startup()
{
    schedule(event, latency);
}
