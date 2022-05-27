/*
App impersonator
Skills used: UPDATE, DELETE, CREATE TABLE 
*/

-- Think about your favorite apps, and pick one that stores your data- like a game that stores scores, 
-- an app that lets you post updates, etc. Now in this project, you're going to imagine that the app stores your data in a SQL database (which is pretty likely!), 
-- and write SQL statements that might look like their own SQL.

--  CREATE a table to store the data.
--  INSERT a few example rows in the table.
--  Use an UPDATE to emulate what happens when you edit data in the app.
--  Use a DELETE to emulate what happens when you delete data in the app.


/* What does the app's SQL look like? */

CREATE TABLE runing_app (id INTEGER PRIMARY KEY AUTOINCREMENT, place_start TEXT, duration INTEGER, place_finish TEXT, date INTEGER);

INSERT INTO runing_app (place_start,duration,place_finish,date) VALUES("Church",20,"Plaza bolivar","2022-12-01");
INSERT INTO runing_app (place_start,duration,place_finish,date) VALUES("apartment",30,"pedro y pablo","2022-22-01");
INSERT INTO runing_app (place_start,duration,place_finish,date) VALUES("house",60,"obelisco","2022-16-02");

SELECT * FROM runing_app;

UPDATE runing_app SET duration = "22" WHERE id = 1;

SELECT * FROM runing_app;

DELETE FROM runing_app WHERE id = 1;

SELECT * FROM runing_app;

