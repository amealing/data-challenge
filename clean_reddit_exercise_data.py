import csv
import sys
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

## Read CSV

def read_raw_data_csv():
	csv_data = sys.argv[1] 
	dfRaw = pd.read_csv(csv_data)
	return dfRaw

## Clean CSV
## Sync Dates

def fix_date(date):
	# Some dates are in d/m/y format while the majority are in y/m/d
	# It was quickest to convert all based on yearfirst=True
	# and then if date not between 1/5/17 and 31/7/17
	# reformat the date to align with rest of dates (switch month first, then year)
	if date.month < 5 or date.month > 7:
		date = pd.to_datetime(date.strftime('%y-%d-%m'), yearfirst=True)	
	if date.year != 2017:
		date = pd.to_datetime(date.strftime('%y-%m-%d'), dayfirst=True)
	return date

def clean_dates(df):
	df['date'] = df['date'].apply(pd.to_datetime, yearfirst=True)
	df['date'] = df['date'].apply(fix_date)


## Bucket app_bought and money_spent

# print(dfRaw.money_spent.describe())

def bucket_app_bought(purchases):
	# Approx equal distribution of users across 3 buckets
	if purchases <= 33:
		return "low"
	if purchases <= 66:
		return "medium"
	return "high"

def bucket_money_spent(spending):
	# Bucket into three groups
	# Differentiate between low/medium/high spenders
	# Total spending power of each group approx equal
	if spending <= 100:
		return "low"
	if spending <= 250:
		return "medium"
	return "high"

def apply_buckets(df):
	df["app_bought_bucket"] = df.app_bought.apply(bucket_app_bought)
	df["money_spent_bucket"] = df.money_spent.apply(bucket_money_spent)

# print(dfRaw.money_spent_bucket.value_counts())
# print(dfRaw.app_bought_bucket.value_counts())

## Write to new csv

def write_to_csv(df):
	clean_file_name = sys.argv[1].split(".")[0] + "_clean.csv"
	df.to_csv(clean_file_name)
	return clean_file_name

if __name__ == '__main__':
	dfRaw = read_raw_data_csv()
	clean_dates(dfRaw)
	apply_buckets(dfRaw)
	clean_file_name = write_to_csv(dfRaw)
	print("Clean CSV created as {}".format(clean_file_name))
