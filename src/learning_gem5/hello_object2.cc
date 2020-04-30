#include "learning_gem5/hello_object2.hh"

#include <iostream>

HelloObject2::HelloObject2(HelloObject2Params *params) :
    SimObject(params)
{
    std::cout << "Hello World! From a SimObject!" << std::endl;
}

HelloObject2*
HelloObject2Params::create()
{
    return new HelloObject2(this);
}