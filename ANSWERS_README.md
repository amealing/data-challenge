## ANSWERS_README

1) python clean_reddit_exercise_data.py reddit_exercise_data.csv

Takes a single argument (the raw data file), cleans the data and 
outputs to a new file using the old file name and "clean" on the end

2) python write_to_db reddit_exercise_data_clean.csv

Writes data from csv argument into the reviews table

3) python read_from_db.py

Executes the 3 SQL commands and outputs data to three separate CSVs:
- avg_score_by_iso.csv
- max_score_by_apps_bought.csv
- avg_score_time_series.csv
