# kitchen-cli

kitchen-cli is a simple and very basic version control software embedded as an interactive "cooking simulator" :cake:

This tool has obvious limitation and is aimed at solo developpers who want to manage a personal or small business project.


The following analogies are used by kitchen-cli :

*  _kitchen_     -> Your project folder
*  _table_       -> A folder where you dump your ingredients
*  _freezer_     -> A folder where you store your pastries
*  _ingredients_ -> Your project files used to update your kitchen
*  _pastries_    -> Your update files archived as a tarball
*  _recipe_      -> Config file used by your oven to cook your pastries
*  _blueprint_   -> A complete backup of your kitchen



#Build:

before we can start cooking we must first build up our kitchen...


> :bulb: kitchen-cli `build kitchen` - Lets you set the path to your project root folder. 

> :bulb: kitchen-cli `build freezer` - Lets you set the path to your freezer, this is where you store all of your pastries.

> :bulb: kitchen-cli `build table`   - Lets you set the path to your table, this is where you drop all of your ingredients.


your kitchen is now ready to operate :fork_and_knife:


#Make: 


> :bulb: kitchen-cli `make blueprint` - Lets you backup your whole kitchen and store the backup inside your freezer. 
                                        This command is useful when you implement kitchen to an existing project.

> :bulb: kitchen-cli `make recipe` - Analyze all the ingredients on your table and check if they already exist inside                                        your kitchen, if some ingredients are not found it will ask the user to input the full path                                              to allocate the new ingredients inside your kitchen. This process will create `recipe.ini` and                                          store all the needed information to cook your ingredients or unfreeze your pastries.


