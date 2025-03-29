import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
print("\n🔹 First 5 rows of the dataset:")
print(df.head())
print("\n🔹 Dataset Information:")
print(df.info())
print("\n🔹 Summary Statistics:")
print(df.describe(include="all"))
print("\n🔹 Missing Values:")
print(df.isnull().sum())
df['age'].fillna(df['age'].median(), inplace=True)
df.dropna(subset=['embark_town'], inplace=True)

plt.figure(figsize=(8, 5))
sns.barplot(x="class", y="survived", data=df, ci=None, palette="coolwarm")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.title("Titanic Survival Rate by Class")
plt.show()

survival_counts = df.groupby("class")["survived"].value_counts().unstack()
print("\n🔹 Survival Count by Class:")
print(survival_counts)
