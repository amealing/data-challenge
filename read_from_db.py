import sqlite3
import csv

db = sqlite3.connect("exercise_database.db")
cursor = db.cursor()

def execute_sql_to_csv(sql, csv_file_name):
	cursor.execute(sql)
	db.commit()
	with open(csv_file_name,'w') as filename:
		csv_write = csv.writer(filename)
		for row in cursor:
			csv_write.writerow(row)

## Average score by ISO

iso_sql = "select iso, avg(score) from reviews group by iso"
iso_file_name = "avg_score_by_iso.csv"
execute_sql_to_csv(iso_sql, iso_file_name)


## Maximum score by app_bought_bucket

apps_bought_sql = "select apps_bought_bucket, max(score) from reviews group by apps_bought_bucket"
apps_bought_file_name = "max_score_by_apps_bought.csv"
execute_sql_to_csv(apps_bought_sql, apps_bought_file_name)


## Average score over time (day)

time_series_sql = "select date, avg(score) from reviews group by date"
time_series_file_name = "avg_score_time_series.csv"
execute_sql_to_csv(time_series_sql, time_series_file_name)

