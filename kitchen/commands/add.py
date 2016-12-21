"""kitchen-cli / user action: add"""

import os.path

import re

from ConfigParser import SafeConfigParser

from json import dumps

from .base import Base

from .classes import termcolor



class Add(Base):


    def run(self):

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

        kitchen_alias = str(raw_input("Walk to kitchen alias : "))


        if config_ini_parser.has_option('kitchens',kitchen_alias):
           kitchen_ini_path = config_ini_parser.get('kitchens',kitchen_alias) #retrieve kitchen.ini from current selected kitchen alias

        else:
            print ('This kitchen alias does not exist!')
            raise SystemExit 

        kitchen_ini_parser.read(kitchen_ini_path) #read from selected kitchen.ini

        if 'table' not in kitchen_ini_parser.sections():
            print 'You need a table before fetching your ingredients'
            raise SystemExit
