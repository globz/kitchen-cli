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


> :bulb: Kitchen-CLI `build kitchen` - Lets you set the path to your project root folder. 

> :bulb: Kitchen-CLI `build freezer` - Lets you set the path to your freezer, this is where you store all of your pastries.

> :bulb: Kitchen-CLI `build table`   - Lets you set the path to your table, this is where you drop all of your ingredients.


your kitchen is now ready to operate :fork_and_knife:


#Make: 


> :bulb: Kitchen-CLI `make blueprint` - Lets you backup your whole kitchen and store the backup inside your freezer.


