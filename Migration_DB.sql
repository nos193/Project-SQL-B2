-- Connect to the source database

--  Insert data from source to destination

ATTACH 'tpb2.db' AS src;



BEGIN;

INSERT INTO Game (Name)
SELECT DISTINCT Name
FROM src.game
ORDER BY IdGame;

INSERT INTO main.Place (Name, Adress, City)
SELECT 
placeName, 
Address, 
src.tournament.City
FROM src.tournament
GROUP BY 
placeName,
address,
city;

INSERT INTO main.Tournament (IdPlace, IdGame, Date, Duration)
SELECT IdPlace,
IdGame,
Date, 
Duration
FROM main.Place,
src.tournament
WHERE 
src.tournament.placeName = main.Place.Name;



INSERT INTO 
main.Employee_Data (LastName, FirstName , Gender, Age, Wage)
SELECT 
LastName, 
FirstName, 
Gender, 
Age ,
Wage
FROM 
src.staff;

INSERT INTO main.Employee_Data( Lastname, Firstname, Gender, Age, Wage)
SELECT Lastname, Firstname, Gender, Age, Wage 
FROM src.coach;

INSERT INTO Employee_Data( Lastname, Firstname, Gender, Age, Wage)
SELECT Lastname, Firstname, Gender, Age, Wage 
FROM src.player;


INSERT INTO main.Staff (idEmployeeData)
SELECT
IdEmployee
FROM 
main.Employee_Data , src.staff
WHERE 
src.staff.lastname = main.Employee_Data.Lastname
AND
src.staff.firstname = main.Employee_Data.Firstname;


INSERT  
main.Coach (IdCoach, IdGame,LicenseDate, IdEmployeeData)
SELECT IdCoach,
IdGame, 
licenseDate,
main.Employee_Data.IdEmployee 
FROM src.coach
INNER JOIN
 main.Employee_Data 
on main.Employee_Data.Lastname = src.coach.lastname 
AND main.Employee_Data.Firstname = src.coach.firstname;

INSERT 
 main.Player (IdPlayer, IdGame, Ranking, IdEmployeeData)
SELECT  IdPlayer,
IdGame,
ranking,
main.Employee_Data.IdEmployee 
FROM
src.player 
INNER JOIN
 main.Employee_Data 
on main.Employee_Data.Lastname = src.player.lastname 
AND main.Employee_Data.Firstname = src.player.firstname;



COMMIT;
DETACH src;