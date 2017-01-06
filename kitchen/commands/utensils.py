"""kitchen-cli / user action: utensils"""

import os.path

from .base import Base

from .classes import termcolor
 


class Utensils(Base):


          def run(self):

              print termcolor.BOLD +'\nYou open the utensils drawer...'+ termcolor.ENDC
              
              from ConfigParser import SafeConfigParser
              config_ini_parser  = SafeConfigParser() #parser for config.ini
              
              dir = os.path.dirname(__file__)
              config_ini_path = os.path.join(dir,'..','config.ini') #path of config.ini      
              config_ini_parser.read(config_ini_path) #read from config.ini

              if config_ini_parser.has_option('utensils','auto-alias'):
                 print termcolor.OKGREEN +('TADAM! You are happy to find clean and organised utensils.')+ termcolor.ENDC
                 print config_ini_parser.items('utensils')         
              
              else:
                  print termcolor.FAIL +('You could not find any useable utensils...I bet they are dirty!')+ termcolor.ENDC
                    




