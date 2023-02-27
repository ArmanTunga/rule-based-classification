# TASK 1: Answer the following questions.
# Q1: Read the persona.csv file and show the general information about the dataset.


# Q2: How many unique SOURCE are there? What are their frequencies?


# Q3: How many unique PRICEs are there?


# Q4: How many sales were made from which PRICE?


# Q5: How many sales were made from which country?


# Q6: How much was earned in total from sales by country?


# Q7: What are the sales numbers according to SOURCE types?


# Q8: What are the PRICE averages by country?


# Q9: What are the PRICE averages by SOURCE?


# Q10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?


########################################################################################
# TASK 2: What are the average earnings in breakdown of COUNTRY, SOURCE, SEX, AGE?


########################################################################################
# TASK 3: Sort the output by PRICE.
# To see the output of the previous question better, apply the sort_values method to PRICE in descending order.
# Save the output as agg_df.


########################################################################################
# TASK 4: Convert the names in the index to variable names.
# All variables except PRICE in the output of the third question are index names.
# Convert these names to variable names
# Hint: reset_index()
# agg_df.reset_index(inplace=True)


########################################################################################
# TASK 5: Convert AGE variable to categorical variable and add it to agg_df.
# Convert the numeric variable age to a categorical variable.
# Create the intervals in whatever way you think will be persuasive.
# For example: '0_18', '19_23', '24_30', '31_40', '41_70'


########################################################################################
# TASK 6: Define new level based customers and add them as variables to the dataset.
# Define a variable named customers_level_based and add this variable to the dataset.
# CAUTION!
# After creating customers_level_based values with list comp, these values need to be deduplicated.
# For example, it could be more than one of the following: USA_ANDROID_MALE_0_18
# It is necessary to take them to groupby and get the price average.


########################################################################################
# TASK 7: Segment new customers (USA_ANDROID_MALE_0_18).
# Segment by PRICE,
# add segments to agg_df with "SEGMENT" naming,
# describe the segments,
# Hint: pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"]

########################################################################################
# TASK 8: Classify the new customers and estimate how much income they can bring.
# Which segment does a 33-year-old Turkish woman using ANDROID belongs to and how much income is expected to earn on
# average?
# In which segment and on average how much income would a 35-year-old French woman using iOS expect to earn?
# Hint:
# new_user = "TUR_ANDROID_FEMALE_31_40"
