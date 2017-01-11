"""kitchen-cli / user action: examine"""

import os.path

from os import listdir

from ConfigParser import SafeConfigParser

from json import dumps

from .base import Base

from .classes import termcolor

from os.path import isfile, join


class Examine(Base):


     def run(self):

        
         for key, value in self.options.items():

             #read optional command argument if supplied by the user and jump to the appropriate menu

             if value == 'table':
                  object = 'table'

             if value == 'freezer':
                  object = 'freezer'

             if value == 'exit':
                  object = 'exit'
   
         config_ini_parser  = SafeConfigParser() #parser for config.ini
         kitchen_ini_parser = SafeConfigParser() #parser for kitchen.ini 

         dir = os.path.dirname(__file__)
         config_ini_path = os.path.join(dir,'..','config.ini') #path of config.ini

         config_ini_parser.read(config_ini_path) #read from config.ini
         
         if 'kitchens' not in config_ini_parser.sections():
             print 'oh no! The kitchen is nowhere to be found!'


         else:
             print termcolor.OKGREEN +'The following kitchens alias(es) currently exist:'+ termcolor.ENDC
             print  config_ini_parser.items('kitchens')

         print termcolor.WARNING +'\nYou can examine the following objects : [<freezer>,<table>]'+ termcolor.ENDC
         print 'usage :<object>'
         print 'type exit to abort \n'       
 
         while True:

           try:
               object        #check if object is already defined

           except NameError:
               object = None #if object was not defined by optional command arguments then set it to None and read from prompt


               if object is None:
                  object = str(raw_input("Please select the object you would like to examine : "))

           except OSError as err:
                print("OS error: {0}".format(err))

           
           else:
               if object == 'freezer':

                  print ('\nPlease type the desired kitchen alias so you can walk to the appropriate location... ')

                  if config_ini_parser.has_option('utensils','auto-alias'):
                     auto_alias = config_ini_parser.get('utensils','auto-alias') #retrieve value from utensil :: auto-alias
        
                  if auto_alias =='unset':
                     kitchen_alias = str(raw_input("Walk to kitchen alias : "))


                     if kitchen_alias == 'exit':

                        print ('Aborting...')
                        break                 
              

                  else:
                      #utensil auto-alias is currently enabled so lets try out this alias
                      kitchen_alias = auto_alias
                      print termcolor.WARNING +'\nUtensil :: auto-alias is currently enabled and the following alias has been select: '+auto_alias+termcolor.ENDC

                  if config_ini_parser.has_option('kitchens',kitchen_alias):
                     kitchen_ini_path = config_ini_parser.get('kitchens',kitchen_alias) #retrieve kitchen.ini from current selected kitchen alias


                  else:
                      print ('This kitchen alias does not exist!')
                      raise SystemExit 

                  kitchen_ini_parser.read(kitchen_ini_path) #read from selected kitchen.ini

                  if 'freezer' not in kitchen_ini_parser.sections():
                      print 'You cannot examine your freezer because its not even built!'
                      raise SystemExit


                  freezer_path = kitchen_ini_parser.get('freezer','path') #find freezer location for the selected kitchen alias
                  print '\n'+termcolor.OKGREEN +'freezer located @ '+freezer_path+ termcolor.ENDC

                  print termcolor.WARNING +'You open the door of your freezer and you can see the following pastries...\n'+ termcolor.ENDC
           
                  onlyfiles = [f for f in listdir(freezer_path) if isfile(join(freezer_path, f))]
                  print onlyfiles
                  break


               if object == 'table':
                            
                  print ('\nPlease type the desired kitchen alias so you can walk to the appropriate location... ')

                  if config_ini_parser.has_option('utensils','auto-alias'):
                     auto_alias = config_ini_parser.get('utensils','auto-alias') #retrieve value from utensil :: auto-alias
        
                  if auto_alias =='unset':
                     kitchen_alias = str(raw_input("Walk to kitchen alias : "))


                     if kitchen_alias == 'exit':

                        print ('Aborting...')
                        break                 
              

                  else:
                      #utensil auto-alias is currently enabled so lets try out this alias
                      kitchen_alias = auto_alias
                      print termcolor.WARNING +'\nUtensil :: auto-alias is currently enabled and the following alias has been select: '+auto_alias+termcolor.ENDC

                  if config_ini_parser.has_option('kitchens',kitchen_alias):
                     kitchen_ini_path = config_ini_parser.get('kitchens',kitchen_alias) #retrieve kitchen.ini from current selected kitchen alias


                  else:
                      print ('This kitchen alias does not exist!')
                      raise SystemExit 

                  kitchen_ini_parser.read(kitchen_ini_path) #read from selected kitchen.ini

                  if 'table' not in kitchen_ini_parser.sections():
                      print 'You cannot examine your table because its not even built!'
                      raise SystemExit


                  table_path = kitchen_ini_parser.get('table','path') #find table location for the selected kitchen alias
                  print '\n'+termcolor.OKGREEN +'table located @ '+table_path+ termcolor.ENDC

                  print termcolor.WARNING +'You slowly walk to your table and find the following ingredients...\n'+ termcolor.ENDC
           
                  onlyfiles = [f for f in listdir(table_path) if isfile(join(table_path, f))]
                  print onlyfiles
                  break
 

               if object == 'exit':

                    print ('Aborting...')
                    break

               else:
                   print ('cannot examine object')
                   break
