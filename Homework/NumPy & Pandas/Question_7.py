# ==== Question 7: ====

import pandas as pd

'''
aPSEUDOCODE:
1. create a table containing the following information
	- commerical ID
	- region aired
	- time aired
2. create table containing the following information
	- sales ID
	- region sales generated in
	- time sales occurred
	- amount
3. map sale to commerical id
	- for each sale filter the table of commercials by a region equal to the sale's region & that had aired prior to the date of the sale
	- obtain the most recent commercial from this list
	- append this most recent commercial's ID to a mapped array along with the Sales ID, amount & sale date
'''

# commericals dictionary
commercials_data = {
	'CommercialID': [1,2,3,4,5],
	'AirDate': ['2024-08-10', '2024-09-02', '2024-08-25', '2024-09-05','2024-09-05'],
	'Region': ['East', 'South', 'West', 'West', 'South']
}

# sales dictionary
sales_data = {
	'SaleID': [1,2,3,4,5],
	'SaleDate': ['2024-08-15','2024-09-04','2024-09-04','2024-09-10','2024-09-06'],
	'Region': ['East','West','South','West','South'],
	'Amount': [450,100,500,320,750]
}

# convert to DataFrames
commercials_df = pd.DataFrame(commercials_data)
sales_df = pd.DataFrame(sales_data)

# DEBUG
print(commercials_df)
print(sales_df)

# convert date to datetime in order to use filtering
# to_datetime(): https://www.geeksforgeeks.org/python-pandas-to_datetime/
commercials_df['AirDate'] = pd.to_datetime(commercials_df['AirDate'])
sales_df['SaleDate'] = pd.to_datetime(sales_df['SaleDate'])

# empty list to hold mapped results
mapped_sales = []

# iterate through each row/sale in the sales DataFrame using iterrows()
# iterrows(): https://www.w3schools.com/python/pandas/ref_df_iterrows.asp
for row, sale in sales_df.iterrows():

	# filter commercials for the *same region* as the sale & *aired before the sale* date
	filtered_commercials = commercials_df[
		(commercials_df['Region'] == sale['Region']) &
		(commercials_df['AirDate'] < sale['SaleDate'])
	]

	# find most recent commercial from this filtered list of commercials
	if not filtered_commercials.empty:
		# use idxmax() to get the id pertaining to the max value in a column (AirDate)
		# this id corresponds to the row or record for the commercial with the max AirDate (most recent)
		# idxmax(): https://www.geeksforgeeks.org/python-pandas-dataframe-idxmax/
		most_recent_commercial = filtered_commercials.loc[
			filtered_commercials['AirDate'].idxmax()
		]

		# append the result of this most recent commercial (w/ same region as sale & aired before the sale)
		#	and the corresponding sale to previous mapped_sales list
		mapped_sales.append({
			'SaleID': sale['SaleID'],
			'CommercialID': most_recent_commercial['CommercialID'],
			'Amount': sale['Amount'],
			'SaleDate': sale['SaleDate']
		})

# turn the mapped_sales list into a DataFrame
mapped_sales_df = pd.DataFrame(mapped_sales)

print("Mapped Sales")
print(mapped_sales_df)