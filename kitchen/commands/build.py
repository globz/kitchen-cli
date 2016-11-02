"""kitchen-cli / user action: build"""

import os

from ConfigParser import SafeConfigParser

from json import dumps

from .base import Base

from .classes import bcolors

config = SafeConfigParser()
dir = os.path.dirname(__file__)
kitchen_conf = os.path.join(dir,'..','config.ini')
config.read(kitchen_conf)


class Build(Base):
    

    def run(self):
        print 'You are hungry for pastries...'

        if 'kitchens' not in config.sections():       
            print 'oh no! The kitchen is nowhere to be found! .'
        else:
            print 'The following kitchens currently exist:' 
            print config.items('kitchens')

        print bcolors.WARNING +'You can build the following objects : (kitchen,freezer,table,oven)'+ bcolors.ENDC
        print 'usage : build (object)'
        print 'type exit to abort'

        while True:
           try:
               object = str(raw_input("Please select the object you would like to build : "))
           except OSError as err:
                print("OS error: {0}".format(err))
                 
           else:
               if object == 'build kitchen':
                   kitchen_path = str(raw_input("Type the full path of your project folder so we can build a kitchen : "))
                   if os.path.exists(kitchen_path):
                      """add regex so we can remove path like this : /home/dev/project/ """
                      kitchen_path = kitchen_path+'/kitchen.ini'
                      open(kitchen_path,'a').close() #save kitchen.ini to project folder
                      
                      print 'A kitchen alias is needed so you can walk into different kitchens (useful when managing multiple projects)'
                      kitchen_alias = str(raw_input("Input an alias for this kitchen : "))
                      
                      if 'kitchens' not in config.sections():
                          config.add_section('kitchens')

                      config.set('kitchens', kitchen_alias, kitchen_path) #save new kitchen to config.ini
                      
                      with open(kitchen_conf, 'w') as f:
                           config.write(f)

                      print ('Kitchen built.')
                      print ('The following files were created/updated : ')
                      print bcolors.OKGREEN+kitchen_path
                      print 'updated config.ini : '+kitchen_alias+' = '+config.get('kitchens',kitchen_alias)+ bcolors.ENDC
                      break

                   else:
                       print ('input path is wrong')

               if object == 'build freezer':
                   print ('Freezer built.')
                   break
               
               if object == 'build table':
                   print ('Table built.') 
                   break

               if object == 'build oven':
                   print ('Oven built.')
                   break

               if object == 'exit':
                  break

               else:
                   print ('cannot build object')
