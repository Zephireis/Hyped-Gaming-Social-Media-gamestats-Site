from env_vars import db_user, db_passwd, db_database, db_host
import mysql.connector


def creds(host_name, user_name, user_password, user_database):# the func creds needs the arguments to be filled)
    connection = mysql.connector.connect(
    host=host_name, # hostname will be 1st creds(arg1)
    user=user_name, # user_name will be 2nd creds(arg1, agr2, )
    passwd=user_password, #user_pass wull be 3rd creds(arg1,agr2,arg3)
    database=user_database #user_database will be 4th argument creds(arg1,arg2,arg3,arg4)
    )
    print("Connection to MySQL DB successful")
    return connection # this returns all the variables defined under the connection variable

connection = creds(db_host, db_user, db_passwd, db_database) # in order for creds() to be user we have to pass in the parameters (arguments) in order.
# print(connection)


# connection = creds(db_host, db_user, db_passwd, db_database)
# mycursor = connection.cursor()
# sql = "SELECT * FROM players ORDER BY repscore DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)






# def get_data():
#     mycursor = creds()
#     sql = "SELECT * FROM players ORDER BY repscore DESC"
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()
#     print(myresult)
#




#
# def get_data():
#     mycursor = creds()
#     sql = "SELECT * FROM players ORDER BY repscore DESC"
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()
#     print(myresult)
#
