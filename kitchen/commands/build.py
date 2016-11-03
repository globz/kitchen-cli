"""kitchen-cli / user action: build"""

import os.path

from ConfigParser import SafeConfigParser

from json import dumps

from .base import Base

from .classes import termcolor

#config = SafeConfigParser()
#dir = os.path.dirname(__file__)
#kitchen_conf = os.path.join(dir,'..','config.ini')


class Build(Base):
    

    def run(self):

        config_ini_parser  = SafeConfigParser() #parser for config.ini
        kitchen_ini_parser = SafeConfigParser() #parser for kitchen.ini

        dir = os.path.dirname(__file__)
        config_ini_path = os.path.join(dir,'..','config.ini') #path of config.ini

        config_ini_parser.read(config_ini_path) #read from config.ini

        print termcolor.BOLD +'You are hungry for pastries...'+ termcolor.ENDC

        if 'kitchens' not in config_ini_parser.sections():       
            print 'oh no! The kitchen is nowhere to be found!'
        else:
            print termcolor.OKGREEN +'The following kitchens currently exist:'+ termcolor.ENDC 
            print  config_ini_parser.items('kitchens')

        print termcolor.WARNING +'You can build the following objects : (kitchen,freezer,table,oven)'+ termcolor.ENDC
        print 'usage : build (object)'
        print 'type exit to abort'

        while True:
           try:
               object = str(raw_input("Please select the object you would like to build : "))
           except OSError as err:
                print("OS error: {0}".format(err))
                 
           else:
               if object == 'build kitchen':
                   kitchen_ini_path = str(raw_input("Type the full path of your project folder so we can build a kitchen : "))
                   if os.path.exists(kitchen_ini_path):
                      """add regex so we can remove path like this : /home/dev/project/ """
                      kitchen_ini_path = kitchen_ini_path+'/kitchen.ini'
                      open(kitchen_ini_path,'w').close() #save kitchen.ini to project folder 
                      
                      print 'A kitchen alias is needed so you can walk into different kitchens (useful when managing multiple projects)'
                      kitchen_alias = str(raw_input("Input an alias for this kitchen : "))
                      
                      
                      if 'kitchens' not in config_ini_parser.sections(): #add new section to config.ini if it does not exist (kitchens)
                          config_ini_parser.add_section('kitchens')

                      config_ini_parser.set('kitchens', kitchen_alias, kitchen_ini_path) 
                      
                      with open(config_ini_path, 'w') as f: #save new kitchen to config.ini
                           config_ini_parser.write(f)           
                           f.close()                   
                      
 
                      kitchen_ini_parser.read(kitchen_ini_path) #read from kitchen.ini
                      
                      if 'blueprint excludes' not in kitchen_ini_parser.sections(): #add new section to kitchen.ini if it does not exist (blueprint excludes)
                          kitchen_ini_parser.add_section('blueprint excludes')

                      kitchen_ini_parser.set('blueprint excludes','ex1','add exclusion here')
                      
                      with open(kitchen_ini_path,'w') as f: #save new section (blueprint excludes) to kitchen.ini
                           kitchen_ini_parser.write(f)
                           f.close()
                            
                      print ('Kitchen built.')
                      print ('The following files were created/updated : ')
                      print termcolor.OKGREEN+kitchen_ini_path
                      print 'updated config.ini : '+kitchen_alias+' = '+config_ini_parser.get('kitchens',kitchen_alias)+ termcolor.ENDC
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
