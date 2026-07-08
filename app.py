import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

print("First 10 Rows")
print(tips.head(10))

print("Last 10 Rows")
print(tips.tail(10))

print("Dataset Information")
tips.info()

print("Statistical Summary")
print(tips.describe())

print("Shape")
print(tips.shape)

print("Columns")
print(tips.columns)

print("Data Types")
print(tips.dtypes)

print("Total Bill Column")
print(tips["total_bill"])

print("Selected Columns")
print(tips[["total_bill", "tip", "sex", "day"]])

print("Rows 30 to 60")
print(tips.iloc[30:61])

print("Customers with Total Bill > 30")
print(tips[tips["total_bill"] > 30])

print("Male Customers")
print(tips[tips["sex"] == "Male"])

print("Smokers")
print(tips[tips["smoker"] == "Yes"])

print("Customers on Sunday")
print(tips[tips["day"] == "Sun"])

print("Customers with Tip > 5")
print(tips[tips["tip"] > 5])

print("Customers with Party Size Between 2 and 4")
print(tips[(tips["size"] >= 2) & (tips["size"] <= 4)])

print("Female Customers with Total Bill > 25")
print(tips[(tips["sex"] == "Female") & (tips["total_bill"] > 25)])

tips(["Tip_Percentage"] =[tips["tip"] / tips["total_bill"]) * 100

print("Dataset with Tip Percentage")
print(tips.head())

print(total_bill_array = tips["total_bill"].to_numpy())

print("Maximum", np.max(total_bill_array))
print("Minimum", np.min(total_bill_array))
print("Mean", np.mean(total_bill_array))
print("Sum", np.sum(total_bill_array))

print(tips["total_bill"].groupby(tips["day"]).mean())
print(tips["tip"].groupby(tips["sex"]).mean())
print(tips["total_bill"].groupby(tips["day"]).max())
print(tips["tip"].groupby(tips["day"]).min())
print(tips["Invoice_ID"].groupby(tips["day"]).count())

avg_bill = tips.groupby("day")["total_bill"].mean()
plt.bar(avg_bill.index, avg_bill.values)
plt.title("Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(tips["total_bill"], bins=10)
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Scatter Plot Total Bill And Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()


sns.barplot(data=tips, x="day", y="tip")
plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.show()

sns.histplot(data=tips, x="total_bill", kde=True)
plt.title("Histogram of Total Bill with KDE")
plt.xlabel("Total Bill")
plt.ylabel("Count")

plt.savefig("restaurant_tips_histogram.png", dpi=300)
