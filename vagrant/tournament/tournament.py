#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE from matchresults")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE from players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    QUERY = "select count(*) as NumOfRegPlayers from players"
    c.execute(QUERY)
    NumOfRegPlayers = c.fetchall()[0][0]
    DB.close()
    return NumOfRegPlayers


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("insert into players(name) values(%s)",(name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    #QUERY = "select id, name, wins, matches from players, matchresults where players.id = matchresults.id  order by time desc"
    QUERY = '''
    select players.id, name, matchresults.wins as wins, (matchresults.wins + matchresults.loss) as matches
    from players, matchresults 
    where players.id = matchresults.id  
    order by wins desc;
    '''
    c.execute(QUERY)
    playerstanding = []
    for row in c.fetchall():
        playerstanding.append((str(row[0]), str(row[1]), str(row[2]), str(row[3])))
    #playerstanding = ({'id': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
    DB.close()
    return posts


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    #TODO
    #If no update then insert
    
    #Update if already in table
    c.execute("UPDATE matchresults SET wins=matchresults.wins + 1 where matchresults.id = %d",(winner,))
    c.execute("UPDATE matchresults SET loss=matchresults.loss + 1 where matchresults.id = %d",(loser,))
    #c.execute("insert into matchresults(winner, loser) values(%d,%d)",(name, loser,))
    #c.execute("insert into matchresults(id, score) values(%d, 'winner')",(winner,))
    #c.execute("insert into matchresults(id, score) values(%d, 'loser')",(loser,))
    #Else Insert the new outcome
    c.execute("insert into matchresults(id, wins, loss) values(%d, 1, 0)",(winner,))
    c.execute("insert into matchresults(id, wins, loss) values(%d, 0, 1)",(loser,))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


