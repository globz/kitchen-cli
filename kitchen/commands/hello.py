"""The hello command."""

from json import dumps
from .base import Base



class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print 'Hello, world!'
        #print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
        for key, value in self.options.items():
            print key,value        
            if value == 'kitchen':
                 print ('found kitchen....')
