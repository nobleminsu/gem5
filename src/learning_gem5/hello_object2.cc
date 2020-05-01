#include "learning_gem5/hello_object2.hh"

#include <iostream>

#include "debug/Hello.hh"

HelloObject2::HelloObject2(HelloObject2Params *params) :
    SimObject(params)
{
    DPRINTF(Hello, "Created the hello object\n");
}

HelloObject2*
HelloObject2Params::create()
{
    return new HelloObject2(this);
}
