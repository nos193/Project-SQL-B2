# SQL-Poject
Project by Menou Lucas B2
i realy enjoy works on this project because it's chalenging when you never use sql before
# Summary
- [Project Goals](#project-goals)
- [Require for the project](#require-for-the-project)
- [1- Architecture](#1-architecture)\
        - [The Old One](#the-old-one)\
        - [The New One](#the-new-one)\
        - [How i make the new Data Base](#how-i-make-my-new-database)
- [2- The Migration Script](#2-the-migration-script)\
        - [The 2 first important points](#the-2-first-important-points)\
        - [The code explanation](#the-code-explanation)\
        - [THE BASIC SELECT](#the-basic-select)
- [3- How launch the code](#how-launch-the-code)
- [Python Script for data analyze](#python-script-for-data-analyze)
- [Conclusion](#conlusion)


# Project goals 
- New Architecture of the database 
- Migration script using sql 
- Python script for data analyse  
# require for the project 
- sqlite3
- visual studio code 
- python 
- git 


its all the stuff i used to finish this project

# 1- Architecture
 We started this project by the analyse of the old and the new architecture
 ## The old one 
 ![image](https://user-images.githubusercontent.com/91542549/214823033-e211ccf0-6bfd-469d-8d44-c1869e4f87bf.png)

 
 we can see the old database with the tables primary key, foreign key etc.
 we started from this to find how this is working and how we gonna work on it 
 
 ## The New One 
 ![image](https://user-images.githubusercontent.com/91542549/214823151-eb913d09-9fa2-4159-9298-9dd12d205764.png)
 
 We see the huge diference beetween these 2 database and how the architecture gonna be changed.
 - creation of new tables 
 - changing some row to another table 
 - more connection between the primary key and foreign key 
 
 ## How i make my new Database 
 #### for this part im gonna explain how i imagined the way of how the new db gonna be made
 ![image](https://user-images.githubusercontent.com/91542549/214890627-782099b5-e054-44c4-bd0d-5ea55ebf7a89.png)
 
 
 In first in gonna create a NEW TABLE IF NOT **EXIST** 
 the not exist is for the case where the table i already made. To says "you don't have to recreate it"
 
 ![image](https://user-images.githubusercontent.com/91542549/214894420-92488c83-7dee-4fcf-ae9d-5c1a705e7c54.png)

  After that i declare in first the **PRIMARY KEY** , its because we always declare the primary key in first instead it inst work well.
  We also use the **AUTOINCREMENT** and **NOT NULL** because we want this, a primary key can't be null and need to autoincrement.
  
  After this we declare the rows of our table in this case its only TEXT type in this table.
  
  ![image](https://user-images.githubusercontent.com/91542549/214892553-cf6cefac-98d3-4dbc-9feb-f8728fdbd532.png)


The second major case is when we using a **FOREIGN KEY** . this type is always placed at the bottom of the create table and is for indicate the foreign key gonna grab the info from a Primary Key, in this case its from the primary key **IdEmployeeData** from the table **Employee_data**
After doing this for all the table with the new database schema we have our new architecture for the database.
### Important point 
- Primary Key is alway the first we declare 
- foreign key is always the last 
- between these declare the other row we want 

# **2-The Migration Script**

### How its gonna works ?
its realy easy we gonna declare where and how the old info gonna be transfert.


![image](https://user-images.githubusercontent.com/91542549/214896569-b6d1f960-6406-4cce-ac65-73ab7e0bae72.png)

in first we gonna **ATTACH** the old database to the script and give him an ALIAS **src** with the **AS**.
we doing this to easily spot when we call the old database info like in this case 

![image](https://user-images.githubusercontent.com/91542549/214897497-51dba582-5f55-48ca-8f7c-0a32b3ffcc60.png)

the **src.tournament.city** is for indicate the code where the info come from 
in this case we want the info from the old database in the table tournament and in the row city.
with this way of work we dodge the **ambigious** problems.

![image](https://user-images.githubusercontent.com/91542549/214898909-684bc681-e742-4898-921f-fac22e79142c.png)

As we do for the src we call the info from the new database with the alias **main**.
its the default name we using because when we gonna run the script we are already in the new database (im gonna explain this more later)
with this way of coding we can't be lost in the call we made.

### The 2 first important points 

- using an alias for the old database like ***".src"***
- using ***".main"*** for the new one 

### The code explanation

Now i'm gonna explain how my code works and why i chose this way.
In first we have this order of SELECT because in many case the info where the table want to gets the info gonna be on a new tables, so everytime i need to find an information from the ***"main"*** i must declare it earlier and  im about to show you some example to be more explicit.

![image](https://user-images.githubusercontent.com/91542549/214900934-022553ea-2ac2-4b46-9f3e-da7ffe9e1aa8.png) ![image](https://user-images.githubusercontent.com/91542549/214901005-cfecd101-9f12-421e-9b17-cb8be9ce0f4a.png)

In this case i declare first the Game because in the second function for tournament i need the info from ***"main.Game.Idgame"*** so if we search for an info we don't already have its not gonna works well 
its gonna be like thats for all the row we want to incremant, if the info we want ins't already in the row we looking at its not gonna works.
its a huge points because its can be frustating, your function are right but just because of the wrong order it's ins"t works.

Now im gonna explain the basics way to using a SELECT and the 2 different way i use in my project
- The ***Where***
- The ***Inner Join***

#### THE WHERE

![image](https://user-images.githubusercontent.com/91542549/214903992-3702e42d-f8cb-4879-87e9-acef35abcad8.png)


the Where is like a comparaison for the program like "if in this we have this info and this info"
For exemple in the employee_data we using the where condition to check the First name and the last name of the old database player and do the same in the new databse. by doing thats the code can uderstand "who is who" 


#### THE INNER JOIN 

![image](https://user-images.githubusercontent.com/91542549/214903480-9f68a69e-0aed-477b-bc08-f1822c819495.png)

An inner join is made for the case where we want to join commun inforamtion from 2 table.
if i have 2 same Foreign key in two different tables thats help de code to make the link between the tables and easily compare an store it.

## THE BASIC SELECT 
#### In this im gonna just explain how a basic ***SELECT*** work 
 and for it im using the place function.
 
 ![image](https://user-images.githubusercontent.com/91542549/214904460-bbb7992f-b669-4cd4-90b2-09342f2d0191.png)

So : 
we INSERT INTO => we want to give this info in the table ***main.Place*** 
we want the Name, adress and city information

we SELECT the row we want to increment and the row where the infos come from 
In this case its placeName, address, src.tournament.city.

We know these inforamtions come from the table src.tournament from the old database because we using the ***src***

and finaly we want to GROUP BY placename, address and city its for indicate the order of the rows inforamtion.

***VERY IMPORTANT***
***we do not declare the Primary Key in the Select because the code already do where she is because of the status of primary key***

With all these information we already have all the key for a good migration script but we forget 2 details

![image](https://user-images.githubusercontent.com/91542549/214906342-ff10fcd0-bc6d-44db-8110-84ae6231ae4f.png)

![image](https://user-images.githubusercontent.com/91542549/214906316-19e777cd-7b9b-47f4-93e8-f8fe930defd7.png)

 The BEGIN; And the COMMIT; we put these at the begining and the end of our code its the way to says at the code "your start you work here and finish here"
 
 
# How launch the code 

Now our code is ready we want to test it. Im gonna explain how i do in my case to launch the code.

![image](https://user-images.githubusercontent.com/91542549/214909624-f24a9a2d-0692-4b15-8cbf-6df5203f433c.png)

###first you open the cmd from the directory of the project 

![image](https://user-images.githubusercontent.com/91542549/214909953-7796910f-170e-40e7-99cd-2b95aa27f279.png)

### after you right ***sqlite3*** and the "newdbname.db" and "VACUUM;" i case where information still in the db 

![image](https://user-images.githubusercontent.com/91542549/214910765-18e7e5fa-b47a-49a4-a939-cc82a5064f10.png)

### After we launch the first script for the architecture of the new database by using this syntax
### its because we launch the script in the db directly while using ***<*** symbol

![image](https://user-images.githubusercontent.com/91542549/214911085-30639691-b503-45d4-99c5-26b513370184.png)

### In last we launch the last script for the data migration by using the same method 

if all works well you gonna see the tables

![image](https://user-images.githubusercontent.com/91542549/214911633-afb39c0d-a74e-4b48-b4df-396a64156e52.png)

and see the table full of info too 

![image](https://user-images.githubusercontent.com/91542549/214912029-06d9ca85-c08d-489a-83ad-4925e425d2d6.png)

*exemple of the game table*

## PYTHON SCRIPT FOR DATA ANALYZE 

### What this code do ? 
#### in fisrt we list all the possibilty we offer by a menu
![image](https://user-images.githubusercontent.com/91542549/214919691-53fcd362-bdfa-485d-81e7-e3fc716f966f.png)


![image](https://user-images.githubusercontent.com/91542549/214914780-c9317119-2840-414a-8333-d2f656364e47.png)


in this code we can list all the tournament by game name by using call from database 


![image](https://user-images.githubusercontent.com/91542549/214913039-e29b0985-a8b3-4a30-94d2-ac0663e36254.png)

![image](https://user-images.githubusercontent.com/91542549/214919806-c3368117-ccdf-43c4-a92d-0b8d1539e2db.png)

![image](https://user-images.githubusercontent.com/91542549/214919886-75b684cb-fdb4-4184-bdf0-6b08131f6228.png)


and the second part can list all the game and adress from a tournament place like home , stadium etc...

![image](https://user-images.githubusercontent.com/91542549/214915737-408a0fd5-2c98-4304-8cb4-48fc05736821.png)

![image](https://user-images.githubusercontent.com/91542549/214919953-5ff5ce93-3c46-456b-94de-c7f8924f9be3.png)

![image](https://user-images.githubusercontent.com/91542549/214920151-22f4dd7f-9d39-4ff6-908f-c4f175ca1919.png)

For the last fucntion we want the average Wage of player for each games, 

```python
#get all the wages from database
        cursor.execute(f'''SELECT AVG(Wage) 
        FROM Player
        INNER JOIN Employee_Data ON idEmployee = idEmployeeData
        INNER JOIN Game ON Player.IdGame = Game.IdGame
        WHERE Game.name = "{chosen_game}";''')
```
this will give the answear by the same type of menu like this

```
Le Salaire moyen des joueurs de Tekken 7 :
AVG(Wage)
--
135000.0
```


# Conlusion

### in conclusion i can says that i have fully request the project goal by the utilisation of SQL and Python, my script works like i want and the result is exaclty what i was looking for.
- the architecture works 
- the Migration works 
- python code works 

all my goals are completed, if i have to do more on this project its will be about a full python script for the launching of the 2 sql script, like a centralize version where the user have to launch only one code and can choose where the db gonna be created, the name of the db too.
i don't have the time for this because of other project on the way at the same time.

thanks for reading this long read.me i hope my works is enough.












