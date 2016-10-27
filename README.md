# kitchen-cli

kitchen-cli is a simple and very basic version control software embedded as an interactive "cooking simulator" :cake:

This tool has obvious limitation and is aimed at solo developpers who want to manage a personal or small business project.


The following analogies are used by kitchen-cli :

*  kitchen     -> Your project folder
*  table       -> A folder where you dump your ingredients
*  freezer     -> A folder where you store your pastries
*  ingredients -> Your project files used to update your kitchen
*  pastries    -> Your update files archived as a tarball
*  recipe      -> Config file used by your oven to cook your pastries
*  blueprint   -> A complete backup of your kitchen



#Build:

before we can start cooking we must first build up our kitchen...


> :bulb: kitchen-cli `build kitchen` - Lets you set the path to your project root folder. 

> :bulb: kitchen-cli `build freezer` - Lets you set the path to your freezer, this is where you store all of your pastries.

> :bulb: kitchen-cli `build table`   - Lets you set the path to your table, this is where you drop all of your ingredients.


your kitchen-cli is now ready to operate :fork_and_knife:


#Make: 


> :bulb: kitchen-cli `make blueprint` - Lets you backup your whole kitchen and store the backup inside your freezer.

> :bulb: kitchen-cli `make recipe` - Analyze all the ingredients (update files) on your table and checks if they already exist inside                                        your kitchen, if some ingredients (files) are not found it will ask the user to input the full path                                      to allocate the new ingredients inside your kitchen. This process will create `recipe.ini` and                                          store all the needed information to cook or unfreeze your pastries.


