#
# Database access functions for the web forum.
# 
import psycopg2
import time

## Database connection
#DB = []



## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    #posts.sort(key=lambda row: row['time'], reverse=True)
    #UpdatePost()
    DeleteCheese()
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    QUERY = "select time, content from posts order by time desc"
    c.execute(QUERY)
    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
    #posts = c.fetchall()	
    DB.close()
    return posts

#'); delete from posts; --

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    #QUERY = "insert into posts(content) values(%s)",(content,)
    c.execute("insert into posts(content) values(%s)",(content,))
    DB.commit()
    DB.close()
    #t = time.strftime('%c', time.localtime())
    #DB.append((t, content))

#Update post in the database
def UpdatePost():
    '''Update the content of the databse
    '''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("UPDATE posts SET content='Cheese' where content like '%spam%'")
    DB.commit()
    DB.close()

#Delete Cheese from from posts table
def DeleteCheese():
    '''Delete Cheese posts
	'''
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("DELETE from posts WHERE content='Cheese'")
    DB.commit()
    DB.close()