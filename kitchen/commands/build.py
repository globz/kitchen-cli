"""kitchen-cli / user action: build"""

import os.path

import re

from ConfigParser import SafeConfigParser

from json import dumps

from .base import Base

from .classes import termcolor



class Build(Base):


    def run(self):

        for key, value in self.options.items(): 
           
            #read optional command argument if supplied by the user and jump to the appropriate menu 
 
            if value == 'kitchen':
                 object = 'kitchen'
            
            if value == 'freezer':
                 object = 'freezer'

            if value == 'table':
                 object = 'table'

            if value == 'oven':
                 object = 'oven'

            if value == 'exit':
                 object = 'exit'


        config_ini_parser  = SafeConfigParser() #parser for config.ini
        kitchen_ini_parser = SafeConfigParser() #parser for kitchen.ini

        dir = os.path.dirname(__file__)
        config_ini_path = os.path.join(dir,'..','config.ini') #path of config.ini

        config_ini_parser.read(config_ini_path) #read from config.ini

        print termcolor.BOLD +'\nYou are hungry for pastries...'+ termcolor.ENDC

        if 'kitchens' not in config_ini_parser.sections():
            print 'oh no! The kitchen is nowhere to be found!'

        else:
            print termcolor.OKGREEN +'The following kitchens alias(es) currently exist:'+ termcolor.ENDC
            print  config_ini_parser.items('kitchens')

        print termcolor.WARNING +'\nYou can build the following objects : [<kitchen>,<freezer>,<table>,<oven>]'+ termcolor.ENDC
        print 'usage :<object>'
        print 'type exit to abort \n'

        while True:

           try:
               object        #check if object is already defined

           except NameError:
               object = None #if object was not defined by optional command arguments then set it to None and read from prompt


               if object is None:
                  object = str(raw_input("Please select the object you would like to build : "))

           except OSError as err:
                print("OS error: {0}".format(err))


           else:
               if object == 'kitchen':
                   kitchen_ini_path = str(raw_input("Type the full path of your project folder so we can build a kitchen : "))


                   if kitchen_ini_path == 'exit':

                    print ('Aborting...')
                    break                   


                   if os.path.exists(kitchen_ini_path):

                      kitchen_ini_path = re.sub('[\/]$','',kitchen_ini_path)# remove last / from path (/home/dev/project/ => /home/dev/project)
                      kitchen_ini_path = kitchen_ini_path+'/kitchen.ini'
                      open(kitchen_ini_path,'w').close() #save kitchen.ini to project folder

                      print '\nA kitchen alias is needed so you can walk into different kitchens (useful when managing multiple projects)'
                      kitchen_alias = str(raw_input("Input an alias for this kitchen : "))


                      if kitchen_alias == 'exit':

                       print ('Aborting...')
                       break                   


                      if 'kitchens' not in config_ini_parser.sections(): #add new section to config.ini if it does not exist (kitchens)
                          config_ini_parser.add_section('kitchens')

                      config_ini_parser.set('kitchens', kitchen_alias, kitchen_ini_path)

                      with open(config_ini_path, 'w') as f: 
                           #save new kitchen to config.ini
                           config_ini_parser.write(f)
                           f.close()

                      #read from kitchen.ini 
                      kitchen_ini_parser.read(kitchen_ini_path) 

                      if 'blueprint' not in kitchen_ini_parser.sections(): #add new section to kitchen.ini if it does not exist (blueprint)
                          kitchen_ini_parser.add_section('blueprint')

                      kitchen_ini_parser.set('blueprint','exclusions','unset')
                      kitchen_ini_parser.set('blueprint','auto-append','unset')

                      with open(kitchen_ini_path,'w') as f: 
                           #save new section (blueprint) to kitchen.ini
                           kitchen_ini_parser.write(f)
                           f.close()

                      print ('\nKitchen built.')
                      print ('\nThe following files were created/updated : \n')
                      print termcolor.OKGREEN+kitchen_ini_path
                      print '+ [blueprint] exclusions = '+kitchen_ini_parser.get('blueprint','exclusions')
                      print '+ [blueprint] auto-append = '+kitchen_ini_parser.get('blueprint','auto-append')+'\n'
                      print 'Updated config.ini : '+kitchen_alias+' = '+config_ini_parser.get('kitchens',kitchen_alias)+ termcolor.ENDC+'\n'
                      print ('All parameters values are configured to "unset" by default!')
                      print ('You MUST edit the default parameters values inside kitchen.ini manually - see https://github.com/globz/kitchen-cli for configuration help.\n')
                      break

                   else:
                       print ('input path is wrong')

               if object == 'freezer':

                   if 'kitchens' not in config_ini_parser.sections():
                        print ('You cannot build a freezer without a kitchen...')
                        break

                   print ('Please type the desired kitchen alias so you can walk to the appropriate location... ')

                   kitchen_alias = str(raw_input("Walk to kitchen alias : "))


                   if kitchen_alias == 'exit':

                       print ('Aborting...')
                       break                   


                   if config_ini_parser.has_option('kitchens',kitchen_alias):
                      kitchen_ini_path = config_ini_parser.get('kitchens',kitchen_alias) #retrieve kitchen.ini from current selected kitchen alias

                   else:
                      print ('This kitchen alias does not exist!')
                      break


                   print ('\nA freezer is needed so you can store your cooked pastries...\n')
                   print ('Provide the full path and the name of the folder that will host your freezer, if the directory does not exist it will be created.')

                   freezer_path = str(raw_input("Input full path to freezer directory : "))


                   if freezer_path == 'exit':

                       print ('Aborting...')
                       break


                   freezer_path = re.sub('[\/]$','',freezer_path)# remove last / from path (/home/dev/project/freezer/ => /home/dev/project/freezer

                   if not os.path.exists(freezer_path):
                       #create folder if it does not exist
                       os.makedirs(freezer_path) 


                   kitchen_ini_parser.read(kitchen_ini_path) #read from kitchen.ini


                   if 'freezer' not in kitchen_ini_parser.sections(): #add new section to kitchen.ini if it does not exist (freezer)
                       kitchen_ini_parser.add_section('freezer')


                   kitchen_ini_parser.set('freezer','path',freezer_path)


                   with open(kitchen_ini_path,'w') as f: #save new section (freezer) to kitchen.ini
                           kitchen_ini_parser.write(f)
                           f.close()

                   print ('\nFreezer built.')
                   print ('\nThe following file was created/updated : \n')
                   print termcolor.OKGREEN+kitchen_ini_path
                   print '+ [freezer] path = '+kitchen_ini_parser.get('freezer','path')+ termcolor.ENDC+'\n'
                   break


               if object == 'table':

                    if 'kitchens' not in config_ini_parser.sections():
                         print ('You cannot build a table without a kitchen...')
                         break

                    print ('Please type the desired kitchen alias so you can walk to the appropriate location... ')
 
                    kitchen_alias = str(raw_input("Walk to kitchen alias : "))
 

                    if kitchen_alias == 'exit':

                       print ('Aborting...')
                       break


                    if config_ini_parser.has_option('kitchens',kitchen_alias):
                       kitchen_ini_path = config_ini_parser.get('kitchens',kitchen_alias) #retrieve kitchen.ini from current selected kitchen alias

                    else:
                        print ('This kitchen alias does not exist!')
                        break


                    print ('\nA table is needed so you can place your ingredients and prepare your pastries...\n')
                    print ('Provide the full path and the name of the folder that will host your table, if the directory does not exist it will be created.')

                    table_path = str(raw_input("Input full path to table directory : "))


                    if table_path == 'exit':

                       print ('Aborting...')
                       break


                    table_path = re.sub('[\/]$','',table_path)# remove last / from path (/home/dev/project/table/ => /home/dev/project/table

                    if not os.path.exists(table_path):
                        #create folder if it does not exist
                        os.makedirs(table_path) 


                    kitchen_ini_parser.read(kitchen_ini_path) #read from kitchen.ini


                    if 'table' not in kitchen_ini_parser.sections(): #add new section to kitchen.ini if it does not exist (table)
                       kitchen_ini_parser.add_section('table')


                    kitchen_ini_parser.set('table','path',table_path)


                    with open(kitchen_ini_path,'w') as f: #save new section (table) to kitchen.ini
                            kitchen_ini_parser.write(f)
                            f.close()

                    print ('\nTable built.')
                    print ('\nThe following file was created/updated : \n')
                    print termcolor.OKGREEN+kitchen_ini_path
                    print '+ [table] path =  '+kitchen_ini_parser.get('table','path')+ termcolor.ENDC+'\n'
                    break
 

               if object == 'oven':

                    if 'kitchens' not in config_ini_parser.sections():
                         print ('You cannot build an oven without a kitchen...')
                         break

                    print ('Please type the desired kitchen alias so you can walk to the appropriate location... ')
 
                    kitchen_alias = str(raw_input("Walk to kitchen alias : "))
 

                    if kitchen_alias == 'exit':

                       print ('Aborting...')
                       break


                    if config_ini_parser.has_option('kitchens',kitchen_alias):
                       kitchen_ini_path = config_ini_parser.get('kitchens',kitchen_alias) #retrieve kitchen.ini from current selected kitchen alias

                    else:
                        print ('This kitchen alias does not exist!')
                        break


                    kitchen_ini_parser.read(kitchen_ini_path) #read from kitchen.ini
                    
 
                    if 'oven' not in kitchen_ini_parser.sections(): #add new section to kitchen.ini if it does not exist (table)
                       kitchen_ini_parser.add_section('oven')


                    kitchen_ini_parser.set('oven','auto-append','unset')
                    kitchen_ini_parser.set('oven','auto-commit','unset')
                    kitchen_ini_parser.set('oven','cookbook','unset')


                    with open(kitchen_ini_path,'w') as f: #save new section (oven) to kitchen.ini
                            kitchen_ini_parser.write(f)
                            f.close()

                   
                    print ('\nOven built.')
                    print ('You are now able to cook pastries!')
                    print ('\nThe following files were created/updated : \n')
                    print termcolor.OKGREEN+kitchen_ini_path
                    print '+ [oven] auto-append = ' +kitchen_ini_parser.get('oven','auto-append')
                    print '+ [oven] auto-commit = ' +kitchen_ini_parser.get('oven','auto-commit')
                    print '+ [oven] cookbook = '    +kitchen_ini_parser.get('oven','cookbook')+ termcolor.ENDC+'\n'
                    print ('All parameters values are configured to "unset" by default!')
                    print ('You MUST edit the default parameters values inside kitchen.ini manually - see https://github.com/globz/kitchen-cli for configuration help.\n')
                    break

               if object == 'exit':

                    print ('Aborting...')
                    break

               else:
                   print ('cannot build object')
                   break
