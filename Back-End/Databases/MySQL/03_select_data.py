def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)


# NOTE: Posts
select_posts = "SELECT * FROM posts"
posts = execute_read_query(connection, select_posts)

for post in posts:
    print(post)


# NOTE: It’s not recommended to use SELECT * on large tables since it can result in a large number of I/O operations that increase the network traffic.



# ============================ < Join > ============================ #



# ============================ < Multiple Join > ============================ #



# ============================ < WHERE > ============================ #

