-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
CREATE TABLE players(
id serial primary key,
name text);

-- CREATE TABLE matchresults(
-- winner integer,
-- loser integer);

--CREATE TABLE matchresults(
--id integer,
--score text);

CREATE TABLE matchresults(
id integer,
wins integer,
loss integer);



--select players.id, name, matchresults.wins as wins, (matchresults.wins + matchresults.loss) as matches from players, matchresults where players.id = matchresults.id order by wins desc;


