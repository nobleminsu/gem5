import m5
from m5.objects import *

root = Root(full_system = False)

root.hello = HelloObject2(time_to_wait = '2us', number_of_fires = 5)
root.hello.goodbye_object2 = GoodbyeObject2(buffer_size='100B')

m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'
      .format(m5.curTick(), exit_event.getCause()))