import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the csv file into a Pandas DataFrame object. Print the shape of that dataframe.
car_data = pd.read_csv("car_info.csv")
print("Shape of the DataFrame:", car_data.shape)

# 2. Print the names of the Japanese cars having v6 engines
japanese_v6_cars = car_data[(car_data["origin"] == "japan") & (car_data["cylinders"] == 6)]["name"]
print("Japanese cars with V6 engines:", japanese_v6_cars.tolist())

# 3. Print the car names for which the horsepower data is missing
cars_missing_horsepower = car_data[car_data["horsepower"].isnull()]["name"]
print("Cars with missing horsepower data:", cars_missing_horsepower.tolist())

# 4. Print the number of cars having mpg >= 20
high_mpg_cars = car_data[car_data["mpg"] >= 20]
print("Number of cars having mpg >= 20:", len(high_mpg_cars))

# 5. Print the name of the car which has the highest mpg
car_with_highest_mpg = car_data.loc[car_data["mpg"].idxmax()]["name"]
print("Most fuel-efficient car:", car_with_highest_mpg)

# 6. Print the maximum, minimum, and average of the car weights
max_weight = car_data["weight"].max()
min_weight = car_data["weight"].min()
avg_weight = car_data["weight"].mean()
print("Minimum weight:", min_weight)
print("Maximum weight:", max_weight)
print("Average weight:", avg_weight)

# 7. Drop the rows from the dataframe which have any missing value. Print the shape of the resulting dataframe.
car_data_cleaned = car_data.dropna()
print("Shape after removing the missing value:", car_data_cleaned.shape)

# 8. Create a pie chart showing the proportion of cars manufactured in different countries
country_counts = car_data_cleaned["origin"].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%')
plt.title("Proportion of Cars Manufactured in Different Countries")
plt.axis('equal')
plt.show()

# 9. Create a plot containing two subplots placed vertically.
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

# i. Scatter plot showing mpg vs. weight
axes[0].scatter(car_data_cleaned["mpg"], car_data_cleaned["weight"], color='b', label='mpg vs. weight')
axes[0].set_xlabel('mpg')
axes[0].set_ylabel('weight')
axes[0].legend()

# ii. Line plot showing mpg vs displacement
axes[1].plot(car_data_cleaned["mpg"], car_data_cleaned["displacement"], color='r', label='mpg vs. displacement')
axes[1].set_xlabel('mpg')
axes[1].set_ylabel('displacement')
axes[1].legend()

plt.tight_layout()
plt.show()
