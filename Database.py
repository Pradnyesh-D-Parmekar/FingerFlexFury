import mysql.connector
import pygame
mydb =mysql.connector.connect(
    host="localhost",
    user= "root",
    database= "project_app",
    password= "$Tiger@0710$",
    port='3306'
)

mycursor = mydb.cursor()
# sql = 'Select SUM(Score1) FROM `project_app`.`fff`;'
# mycursor.execute(sql)
# # mydb.commit()
# data = mycursor.fetchone()[0]
#
# sql2 = 'Select SUM(Score2) FROM `project_app`.`fff`;'
# mycursor.execute(sql2)
# # mydb.commit()
# data2 = mycursor.fetchone()[0]
#
# if data > data2 :
#     print("Alphonse Wins ",data)
# else:
#     print("Pradnyesh Wins",data2)
# for d in data:
#     print(d)
class GameData():
    def __int__(self):
        # self.data = data
        self.score = self.checking()

    def checking(self):
        sql = 'Select SUM(Score1) FROM `project_app`.`fff`;'
        mycursor.execute(sql)
        data = mycursor.fetchone()[0]
        return data
    def checking2(self):
        sql2 = 'Select SUM(Score2) FROM `project_app`.`fff`;'
        mycursor.execute(sql2)
        data2 = mycursor.fetchone()[0]
        return data2

    def update_score(self):
        sql = 'SELECT MAX(`Round`) FROM `project_app`.`fff`'  # Get the maximum value of the Round column
        mycursor.execute(sql)
        result = mycursor.fetchone()
        max_round = result[0] if result[0] is not None else 0  # Extract the maximum value, if any

        # Increment the round for the new row
        new_round = max_round + 1
        sql = f'INSERT INTO `project_app`.`fff` (`Round`, `Player1`, `Player2`, `Score1`,`Score2`) VALUES ({new_round}, "Alphonse", "Pradnyesh", 1, 0);'
        mycursor.execute(sql)
        mydb.commit()
        print("Query Commited")

    def NewG_data(self):
        dsql = 'TRUNCATE `project_app`.`fff`;'
        mycursor.execute(dsql)
        mydb.commit()
        print("Truncate Executed")

        isql = 'INSERT INTO `project_app`.`fff` (`Round`, `Player1`, `Player2`, `Score1`,`Score2`) VALUES (0, "Alphonse", "Pradnyesh", 0, 0);'
        mycursor.execute(isql)
        mydb.commit()
        print("Insert Executed")

    def update_score2(self):
        sql = 'SELECT MAX(`Round`) FROM `project_app`.`fff`'  # Get the maximum value of the Round column
        mycursor.execute(sql)
        result = mycursor.fetchone()
        max_round = result[0] if result[0] is not None else 0  # Extract the maximum value, if any

        # Increment the round for the new row
        new_round = max_round + 1
        sql = f'INSERT INTO `project_app`.`fff` (`Round`, `Player1`, `Player2`, `Score1`,`Score2`) VALUES ({new_round}, "Alphonse", "Pradnyesh", 0, 1);'
        mycursor.execute(sql)
        mydb.commit()
        print("Query Commited")

    # def round_Update(self):
    #     sql = 'SELECT MAX(`Round`) FROM `project_app`.`fff`'  # Get the maximum value of the Round column
    #     mycursor.execute(sql)
    #     result = mycursor.fetchone()
    #     max_round = result[0] if result[0] is not None else 0  # Extract the maximum value, if any
    #
    #     # Increment the round for the new row
    #     new_round = max_round + 1
    #     sql = f'Select Score1 from `project_app`.`fff` where {new_round}='
class Selection():
    def __init__(self, player):
        self.player = player

    def FSelect(self):
        sql = 'SELECT * FROM `project_app`.`WarriorData`'  # Get the maximum value of the Round column
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)