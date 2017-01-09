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
*  _freezer_     -> a folder where you store your old pastries
*  _ingredients_ -> your project files used to make new pastries and update your kitchen 
*  _recipe_      -> config file used by your oven or freezer to either cook or unfreeze your pastries
*  _pastries_    -> a group of patch files which either reside in your freezer (pre-patch) or kitchen (post-patch)
*  _blueprint_   -> your kitchen foundation on which you will build upon
*  _cookbook_    -> a master log of all recipe files and user actions

###Kitchen-cli user actions : 

> build

> add

> make

> cook

> unfreeze

> utensils

> examine

_Each actions have a subset of objects that you can interact with within the current action context._


#build:

**execute this command to get a list of objects for this given action : `kitchen build`**

*Before we can start cooking we must first build up our kitchen...:wrench::nut_and_bolt:*


> :bulb: `build kitchen` - lets you set the path to your project root folder and configure your kitchen.

> :bulb: `build freezer` - lets you set the path to your freezer, this is where you store all of your old pastries.

> :bulb: `build table`   - lets you set the path to your table, this is where you add all of your ingredients.

> :bulb: `build oven`    - lets you configure your oven so you can cook fresh and perfect pastries for your taste.


*Your kitchen is now almost ready to operate, you must configure it first! :fork_and_knife:*


#add:

**execute this command to bring up the interactive menu : `kitchen add`**

*Now that we have have a working kitchen we can start adding ingredients to our table :custard:*


> :bulb: `kitchen add ingredient` - Let the user add ingredient to his table.


#make: 

**execute this command to get a list of objects for this given action : `kitchen make`**


> :bulb: `kitchen make blueprint` - This command is needed when you implement kitchen-cli to a new or existing project.
                                    Blueprint will log all files path to your cookbook and this will serve as your foundation on which you will build upon.
                                    Each time you cook fresh pastries, a new blueprint will be made post-patch.

> :bulb: `kitchen make recipe` - analyze all the ingredients on your table and check if they already exist inside your kitchen, 
                                 if some ingredients are not found it will ask the user to input the full path to allocate the new 
                                 ingredients inside your kitchen. This process will create `recipe.ini` and store all the needed information 
                                 to cook your ingredients into new pastries or unfreeze your old pastries.

*You can already smell the pastries, it is now time to cook :fire:*


#cook:

**execute this command to get a list of objects for this given action : `kitchen cook`**

*Cooking time! Please note that cooking pastries relies on your oven configuration.*


> :bulb: `kitchen cook pastries` -  if `make recipe` returned "success", you will be able to move on and add the ingredients from your table to your oven. 
                                    The process will begin by validating if an existing blueprint has ever been made and if none is found  it will proceed to make one. 
                                    Finally, you can cook some delicious pastries! This process will tarball `recipe.ini` along with your existing pastries (pre-patch) which are to be affected 
                                    by your future pastries (post-patch) and move them to your freezer. Next, it will cook your new pastries and update your kitchen, your new pastries
                                    are now placed inside your kitchen ready to be eaten!


#unfreeze:

**execute this command to get a list of objects for this given action : `kitchen unfreeze`**

> :bulb: `kitchen unfreeze` - roll back to a previous kitchen state by unfreezing the selected pastries from your freezer. 
                              This process will also remove all the files that did not exist prior to this update by reading from `recipe.ini`

#utensils:

**execute this command to get a state overview of all available utensils : `kitchen utensils`**

**edit the following file to enable/disable utensils : `kitchen/config.ini`**

> :bulb: `auto-alias` - if this utensil is enabled each actions will automatically refer to this value when selecting a kitchen alias.

                        default value : `unset`

                        enabled value : `a valid kitchen alias`


> :bulb: `auto-add`   - if this utensil is enabled it will automatically skip the `kitchen add ingredient` prompt asking you to confirm your current selection.

                        default value : `unset`

                        enabled value : `set` 

