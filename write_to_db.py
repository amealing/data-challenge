import sqlite3
import pandas as pd
from clean_reddit_exercise_data import read_raw_data_csv

cleanDf = read_raw_data_csv()
db = sqlite3.connect("exercise_database.db")
cursor = db.cursor()

for index, row in cleanDf.iterrows():
	cursor.execute("""INSERT INTO reviews(review
										, title
										, iso
										, score
										, date
										, apps_bought
										, money_spent
										, apps_bought_bucket
										, money_spent_bucket
										)
	                  VALUES(?,?,?,?,?,?,?,?,?)""", (row['review']
										, row['title']
										, row['iso']
										, row['score']
										, row['date']
										, row['app_bought']
										, row['money_spent']
										, row['app_bought_bucket']
										, row['money_spent_bucket']))

	print("inserted row {}".format(index))

db.commit()

print("Completed")
