"""kitchen-cli / user action: add"""

import os.path

import re

from ConfigParser import SafeConfigParser

from json import dumps

from .base import Base

from .classes import termcolor

try:
    from safeutil import move, copyfile

except ImportError:

    from shutil import move, copyfile



class Add(Base):


    def run(self):

        for key, value in self.options.items(): 
           
            #read optional command argument if supplied by the user (ingredient) 

            if type(value) == str: #if type str is found from options.items assign it to ingredient
               ingredient = value
                              
        config_ini_parser  = SafeConfigParser() #parser for config.ini
        kitchen_ini_parser = SafeConfigParser() #parser for kitchen.ini

        dir = os.path.dirname(__file__)
        config_ini_path = os.path.join(dir,'..','config.ini') #path of config.ini

        config_ini_parser.read(config_ini_path) #read from config.ini

        print termcolor.BOLD +'\nYou are now gathering ingredients for your delicious pastries...'+ termcolor.ENDC

        if 'kitchens' not in config_ini_parser.sections():
            print 'oh no! The kitchen is nowhere to be found'
            raise SystemExit


        else:
            print termcolor.OKGREEN +'The following kitchens alias(es) currently exist:'+ termcolor.ENDC
            print  config_ini_parser.items('kitchens')

        print ('\nPlease type the desired kitchen alias so you can walk to the appropriate location... ')

        if config_ini_parser.has_option('utensils','auto-alias'):
           auto_alias = config_ini_parser.get('utensils','auto-alias') #retrieve value from utensil :: auto-alias
        
        if auto_alias =='unset':
           kitchen_alias = str(raw_input("Walk to kitchen alias : "))

       
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
            print 'You need a table before fetching out your ingredients'
            raise SystemExit


        table_path = kitchen_ini_parser.get('table','path') #find table location for the selected kitchen alias
        print '\n'+termcolor.OKGREEN +'table located @ '+table_path+ termcolor.ENDC

        print termcolor.WARNING +'You can now begin to fetch out your ingredients...\n'+ termcolor.ENDC


        try:
           ingredient        #check if ingredient is already defined

        except NameError:
            ingredient = None #if object was not defined by optional command arguments then set it to None and read from prompt


            if ingredient is None:
               ingredient = str(raw_input("Please select the ingredient you would like to add to your table : "))
          
               copyfile(ingredient,table_path+ingredient) #the ingredient is now safely copied to a kitchen table

               print termcolor.OKGREEN +'\nYou added the following ingredient to your kitchen table: '+ingredient+ termcolor.ENDC
               
        except OSError as err:
            print("OS error: {0}".format(err))


        else:
            if config_ini_parser.has_option('utensils','auto-add'):
               auto_add = config_ini_parser.get('utensils','auto-add') #retrieve value from utensil :: auto-add

            if auto_add =='unset':
               print 'The following ingredient has already been selected: '+termcolor.OKBLUE +ingredient+ termcolor.ENDC +'\nWould you like to add it to your table?'
               copy_prompt = str(raw_input("(y/n) : "))
            
               if copy_prompt == 'y':
                  copyfile(ingredient,table_path+ingredient) #the ingredient is now safely copied to a kitchen table

                  print termcolor.OKGREEN +'\nYou added the following ingredient to your kitchen table: '+ingredient+ termcolor.ENDC
               

               if copy_prompt == 'n':
                  print 'Aborting...'
                  raise SystemExit


            else:
                #utensil auto-add is currently enabled so lets copy the file without prompting for approval
                print 'The following ingredient has already been selected: '+termcolor.OKBLUE +ingredient+ termcolor.ENDC
                print termcolor.WARNING +'\nUtensil :: auto-add is currently enabled! - skipping prompt!'+termcolor.ENDC
                copyfile(ingredient,table_path+ingredient) #the ingredient is now safely copied to a kitchen table
                print termcolor.OKGREEN +'\nYou added the following ingredient to your kitchen table: '+ingredient+ termcolor.ENDC






            
