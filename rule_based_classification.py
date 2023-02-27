#########################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * * * * *                                   * * * * * #
# * * * * *     RULE BASED CLASSIFICATION     * * * * * #
# * * * * *                                   * * * * * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################

import pandas as pd
import numpy as np

# TASK 1: Answer the following questions.
# Q1: Read the persona.csv file and show the general information about the dataset.
df = pd.read_csv("persona.csv")


def check_df(dataframe: pd.core.frame.DataFrame, head: int = 5, tail: int = 5):
    """
    Prints the general information about the given dataframe e.g. shape, dtypes, head,
    tail, null sum, describe with quantiles, nunique, info

    Args:
        dataframe: pd.core.frame.DataFrame
            DataFrame that we want to print the general information about
        head: int
            Used to represent how many first n rows will be shown
        tail: int
            Used to represent how many last n rows will be shown

    Returns:

    """
    print("##################### Shape #####################\n")
    print(dataframe.shape)  # the row and column numbers
    print("\n\n##################### Types #####################\n")
    print(dataframe.dtypes)  # data types
    print("\n\n##################### Head #####################\n")
    print(dataframe.head(head))  # the first 5 observation units
    print("\n\n##################### Tail #####################\n")
    print(dataframe.tail(tail))  # the last 5 observation units
    print("\n\n##################### NA #####################\n")
    print(dataframe.isnull().sum())  # missing values of variable
    print("\n\n##################### Quantiles #####################\n")
    print(dataframe.describe([0.05, 0.25, 0.50, 0.75, 0.95, 0.99]).T)  # some statistics such as mean, count, sum, etc.
    print("\n\n###################### Unique Values #################\n")
    print(dataframe.nunique())  # unique values
    print("\n\n###################### Info #################\n")
    print(dataframe.info())  # General info => row and column numbers, col names, non-null counts, dtypes


check_df(df, 15, 15)

# Q2: How many unique SOURCE are there? What are their frequencies?
unique_source_count = df["SOURCE"].nunique()
unique_source_count

# Q3: How many unique PRICEs are there?
unique_price_count = df["PRICE"].nunique()
unique_price_count

# Q4: How many sales were made from which PRICE?
sales_by_price = df["PRICE"].value_counts()
sales_by_price

# Q5: How many sales were made from which country?
sales_by_country = df["COUNTRY"].value_counts()
sales_by_country

# Q6: How much was earned in total from sales by country?
total_earn_by_country = df.groupby("COUNTRY")["PRICE"].sum()
total_earn_by_country

# Q7: What are the sales numbers according to SOURCE types?
sales_by_sources = df["SOURCE"].value_counts()
sales_by_sources

# Q8: What are the PRICE averages by country?
prices_avg_by_country = df.groupby("COUNTRY")["PRICE"].mean()
prices_avg_by_country

# Q9: What are the PRICE averages by SOURCE?
prices_avg_by_source = df.groupby("SOURCE")["PRICE"].mean()
prices_avg_by_source

# Q10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?
price_avg_by_country_source = df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()
price_avg_by_country_source

########################################################################################
# TASK 2: What are the average earnings in breakdown of COUNTRY, SOURCE, SEX, AGE?

# 2nd Option:  avg_earnings_by_cssa = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean()
avg_earnings_by_cssa = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})
avg_earnings_by_cssa

########################################################################################
# TASK 3: Sort the output by PRICE.
# To see the output of the previous question better, apply the sort_values method to PRICE in descending order.
# Save the output as agg_df.

# If used "2nd Option" in TASK 2: agg_df = avg_earnings_by_cssa.sort_values(ascending=False)
# Because 2nd Option generates a pandas.Series but normal option generates pandas.DataFrame
agg_df = avg_earnings_by_cssa.sort_values(by="PRICE", ascending=False)
agg_df

########################################################################################
# TASK 4: Convert the names in the index to variable names.
# All variables except PRICE in the output of the third question are index names.
# Convert these names to variable names
# Hint: reset_index()
# agg_df.reset_index(inplace=True)
agg_df = agg_df.reset_index()
agg_df

########################################################################################
# TASK 5: Convert AGE variable to categorical variable and add it to agg_df.
# Convert the numeric variable age to a categorical variable.
# Create the intervals in whatever way you think will be persuasive.
# For example: '0_18', '19_23', '24_30', '31_40', '41_70'
max_age = str(agg_df["AGE"].max())
bins = [0, 18, 23, 30, 40, max_age]
max_label = f"41_{max_age}"
labels = ['0_18', '19_23', '24_30', '31_40', max_label]

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=bins, labels=labels)
agg_df

########################################################################################
# TASK 6: Define new level based customers and add them as variables to the dataset.
# Define a variable named customers_level_based and add this variable to the dataset.
# CAUTION!
# After creating customers_level_based values with list comp, these values need to be deduplicated.
# For example, it could be more than one of the following: USA_ANDROID_MALE_0_18
# It is necessary to take them to groupby and get the price average.

agg_df["customers_level_based"] = ["{country}_{source}_{gender}_{age_cat}".format(
    country=row["COUNTRY"].upper(),
    source=row["SOURCE"].upper(),
    gender=row["SEX"].upper(),
    age_cat=row["AGE_CAT"]
)
    for row in agg_df.to_dict("index").values()]
agg_df

agg_df = (agg_df
          [["customers_level_based", "PRICE"]]
          .groupby("customers_level_based")["PRICE"]
          .agg("mean")
          .sort_values(ascending=False)
          .reset_index()
          )
agg_df

########################################################################################
# TASK 7: Segment new customers (USA_ANDROID_MALE_0_18).
# Segment by PRICE,
# add segments to agg_df with "SEGMENT" naming,
# describe the segments, (Group by segments and get mean, max, sum of price)
# Hint: pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"]

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df
segment_description = agg_df.groupby("SEGMENT")["PRICE"].agg(["mean", "min", "max", "sum"])
segment_description

########################################################################################
# TASK 8: Classify the new customers and estimate how much income they can bring.
# Which segment does a 33-year-old Turkish woman using ANDROID belongs to and how much income is expected to earn on
# average?
# In which segment and on average how much income would a 35-year-old French woman using iOS expect to earn?
# Hint:
# new_user = "TUR_ANDROID_FEMALE_31_40"

users = ["TUR_ANDROID_FEMALE_31_40", "FRA_IOS_FEMALE_31_40"]  # Define two users

for user in users:
    user_info = agg_df[agg_df["customers_level_based"] == user].iloc[0]
    print(f"User: {user}\n"
          f"    Segment: {user_info['SEGMENT']}\n"
          f"    Expected Income: {user_info['PRICE']:.2f}\n")
