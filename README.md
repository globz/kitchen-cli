# kitchen-cli

kitchen-cli is a simple and very basic version control software embedded as an interactive "cooking simulator" :cake:

This tool has obvious limitation and is aimed at solo developpers who want to manage a personal or small business project.


The following analogies are used by kitchen-cli :

*  _kitchen_     -> your project folder
*  _table_       -> a folder where you dump your ingredients
*  _freezer_     -> a folder where you store your pastries
*  _ingredients_ -> your project files used to update your kitchen
*  _pastries_    -> your update files archived as a tarball
*  _recipe_      -> config file used by your oven to cook your pastries
*  _blueprint_   -> a complete backup of your kitchen



#build:

before we can start cooking we must first build up our kitchen...


> :bulb: kitchen-cli `build kitchen` - lets you set the path to your project root folder and configure your kitchen.

> :bulb: kitchen-cli `build freezer` - lets you set the path to your freezer, this is where you store all of your pastries.

> :bulb: kitchen-cli `build table`   - lets you set the path to your table, this is where you add all of your ingredients.

> :bulb: kitchen-cli `build oven`    - lets you configure your oven so you can cook the perfect pastries for your taste .


your kitchen is now ready to operate :fork_and_knife:


#add:

now that we have have a working kitchen we can start adding ingredients to our table :custard:


> :bulb: kitchen-cli `add ingredients` - Let the user add ingredients to his table.





#make: 


> :bulb: kitchen-cli `make blueprint` - lets you backup your whole kitchen and store the backup inside your freezer. 
                                        This command is useful when you implement kitchen to an existing project.

> :bulb: kitchen-cli `make recipe` - analyze all the ingredients on your table and check if they already exist inside                                        your kitchen, if some ingredients are not found it will ask the user to input the full path                                              to allocate the new ingredients inside your kitchen. This process will create `recipe.ini` and                                          store all the needed information to cook your ingredients or unfreeze your pastries.

you can already smell the pastries, it is now time to cook :fire:

#oven:

oven time!


> :bulb: kitchen-cli `oven cook pastries` - if `make recipe` returned "success", you will be able to move on and cook your pastries.                                                 This will cook all the ingredients from your table and update your kitchen.                                                             This process will tarball the ingredients and `recipe.ini` then move them to                                                             your freezer. `oven cook pastries` will ask the user to input a name for this group of                                                   cooked pastries going into the freezer.


#unfreeze:

> :bulb: kitchen-cli `unfreeze` - roll back to a previous kitchen state by unfreezing the selected pastries from your freezer. This                                       process will also remove all the files that did not exist prior to this update by reading from `recipe.ini`
