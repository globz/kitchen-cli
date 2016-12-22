# kitchen-cli

kitchen-cli is a basic version control software baked into a "cooking simulator" :cake:

__WARNING:: This tool has obvious limitations and is currently in development for specific use case related to my personal projects.__

Setup
-----

If you've cloned this project, and want to install the library (*and all
development dependencies*), the command you'll want to run is::

    $ pip install -e .[test]


If you'd like to run all tests unit for this project you can run the following command::

    $ python setup.py test

-----

The following analogies are used by kitchen-cli :

*  _kitchen_     -> your project folder
*  _table_       -> a folder where you dump your ingredients
*  _freezer_     -> a folder where you store your pastries
*  _ingredients_ -> your project files used to update your kitchen
*  _pastries_    -> your update files archived as a tarball
*  _recipe_      -> config file used by your oven to cook your pastries
*  _blueprint_   -> a complete backup of your kitchen

###Kitchen-cli user actions : 

> build

> add

> make

> cook

> unfreeze


_Each actions have a subset of objects that you can interact with within the current action context._


#build:

**execute this command to get a list of objects for this given action : `kitchen build`**

*Before we can start cooking we must first build up our kitchen...:wrench::nut_and_bolt:*


> :bulb: `build kitchen` - lets you set the path to your project root folder and configure your kitchen.

> :bulb: `build freezer` - lets you set the path to your freezer, this is where you store all of your pastries.

> :bulb: `build table`   - lets you set the path to your table, this is where you add all of your ingredients.

> :bulb: `build oven`    - lets you configure your oven so you can cook the perfect pastries for your taste.


*Your kitchen is now ready to operate :fork_and_knife:*


#add:

**execute this command to get a list of objects for this given action : `kitchen add`**

*Now that we have have a working kitchen we can start adding ingredients to our table :custard:*


> :bulb: `kitchen add ingredient` - Let the user add ingredient to his table.


#make: 

**execute this command to get a list of objects for this given action : `kitchen make`**

> :bulb: `kitchen make blueprint` - lets you backup your whole kitchen and store the backup inside your freezer. 
                                    This command is useful when you implement kitchen-cli to an existing project.

> :bulb: `kitchen make recipe` - analyze all the ingredients on your table and check if they already exist inside your kitchen, 
                                 if some ingredients are not found it will ask the user to input the full path to allocate the new 
                                 ingredients inside your kitchen. This process will create `recipe.ini` and store all the needed information 
                                 to cook your ingredients or unfreeze your pastries.

*You can already smell the pastries, it is now time to cook :fire:*

#cook:

**execute this command to get a list of objects for this given action : `kitchen cook`**

*Cooking time! Please note that cooking pastries relies on your oven configuration.*


> :bulb: `kitchen cook pastries` -  if `make recipe` returned "success", you will be able to move on and cook your pastries.                                                                               This will cook all the ingredients from your table and update your kitchen.                                                                                            This process will tarball the ingredients and `recipe.ini` then move them to                                                                                           your freezer. `cook pastries` will ask the user to input a name for this group of                                                                                      cooked pastries going into the freezer.


#unfreeze:

**execute this command to get a list of objects for this given action : `kitchen unfreeze`**

> :bulb: `kitchen unfreeze` - roll back to a previous kitchen state by unfreezing the selected pastries from your freezer. 
                              This process will also remove all the files that did not exist prior to this update by reading from `recipe.ini`
