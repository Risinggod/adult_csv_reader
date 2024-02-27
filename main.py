import pandas as pd

df = pd.read_csv('adult.csv')

#print(df.head())
#print(df.tail())
#print(df.info())

new_df = df[["age", "occupation", "income"]]

#print(new_df.head(10))

incomefilter= df[(df["income"] == ">50K")]

#print(incomefilter)

dobblefilter = df[(df["age"] > 30) & (df["education"] == "Bachelors")]

#print(dobblefilter)

df["age_decade"] = df["age"]/10
#print(df.head())

df['income'] = df['income'].replace({'>50K': 'high', '<=50K': 'low'})

print(df.head())

df = df.drop(df[df['occupation'] == "Unknown"].index)

# 1. Deskriptive Statistiken anzeigen
descriptive_stats = df.describe()
print("\n1. Deskriptive Statistiken:")
print(descriptive_stats)

# 2. Gruppieren und Aggregieren: Durchschnitt von sepal_length nach species
avg_income_by_age = df.groupby('income')['age'].mean()
print("\n2. Durchschnittliche sepal_length, gruppiert nach species:")
print(avg_income_by_age)

# 3. Einzigartige Werte in der species-Spalte finden
unique_aducation_values = df['education'].unique()
print("\n3. Einzigartige Werte in der 'species'-Spalte:")
print(unique_aducation_values)
