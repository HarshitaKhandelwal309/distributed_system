
import Pyro4
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}. n" .format(name)
greeting_maker=GreetingMaker()
daemon=Pyro4.Daemon()                
uri=daemon.register(greeting_maker)   
print "Ready. Object uri =", uri      
daemon.requestLoop()
uri A variable is Pyro4 In your own way greeting_maker Object generated uri , which includes the socket and the greeting_maker Generated uniquely id . this id Equivalent to the name of the service, but you can also specify a more understandable service name. Here is the client side client2.py : 
import Pyro4
uri=raw_input(" Pyro uri : ").strip()
name=raw_input("Your name: ").strip()
greeting_maker=Pyro4.Proxy(uri)        
print greeting_maker.get_fortune(name)
