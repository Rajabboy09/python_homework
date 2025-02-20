import sqlite3
import pandas as pd

# **1. INNER JOIN on Chinook Database**
# Chinook SQLite ma'lumotlar bazasini yuklash
conn = sqlite3.connect("lesson-19\homework\data\chinook.db")

# Customers va Invoices jadvallarini yuklash
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices = pd.read_sql_query("SELECT CustomerId, InvoiceId FROM invoices", conn)

# Inner Join (CustomerId bo‘yicha)
merged_df = pd.merge(customers, invoices, on="CustomerId", how="inner")

# Har bir mijoz uchun invoice sonini hisoblash
invoice_counts = merged_df.groupby(["CustomerId", "FirstName", "LastName"])["InvoiceId"].count().reset_index()
invoice_counts.rename(columns={"InvoiceId": "TotalInvoices"}, inplace=True)
print("Har bir mijoz uchun invoice soni:")
print(invoice_counts)

#2
movie_df = pd.read_csv("lesson-19\homework\data\movie.csv")

# Kerakli ustunlarni tanlab kichik DataFrame'lar yaratish
df1 = movie_df[["director_name", "color"]].drop_duplicates()
df2 = movie_df[["director_name", "num_critic_for_reviews"]].drop_duplicates()

# LEFT JOIN (df1 va df2 ni director_name bo‘yicha birlashtirish)
left_join_df = pd.merge(df1, df2, on="director_name", how="left")

# FULL OUTER JOIN (barcha ma’lumotlarni saqlash)
outer_join_df = pd.merge(df1, df2, on="director_name", how="outer")

# Natija: Har bir join turi uchun qatorlar soni
left_join_count = left_join_df.shape[0]
outer_join_count = outer_join_df.shape[0]

# Natijalarni chiqarish
print(f"\nLEFT JOIN natijasida {left_join_count} ta qator hosil bo‘ldi.")
print(f"FULL OUTER JOIN natijasida {outer_join_count} ta qator hosil bo‘ldi.")

# SQLite ulanishini yopish
conn.close()

#3
import pandas as pd

# Titanic ma'lumotlarini yuklash
titanic_df = pd.read_excel('lesson-19/homework/data/titanic.xlsx', sheet_name='Sheet1')

# Pclass bo‘yicha guruhlash va agregatsiya
titanic_grouped = titanic_df.groupby("Pclass").agg(
    AvgAge=("Age", "mean"),
    TotalFare=("Fare", "sum"),
    PassengerCount=("PassengerId", "count")
).reset_index()

# Natijani chiqarish
print(titanic_grouped)


# Movie ma'lumotlarini yuklash
movie_df = pd.read_csv("lesson-19\homework\data\movie.csv")

# Multi-level grouping (color va director_name bo‘yicha)
movie_grouped = movie_df.groupby(["color", "director_name"]).agg(
    TotalCriticReviews=("num_critic_for_reviews", "sum"),
    AvgDuration=("duration", "mean")
).reset_index()

# Natijani chiqarish
print(movie_grouped)


# Flights ma'lumotlarini yuklash
flights_df = pd.read_parquet('E:/AI and BI/python_homework/lesson-19/homework/data/flights')

# Year va Month bo‘yicha guruhlash
flights_grouped = flights_df.groupby(["Year", "Month"]).agg(
    TotalFlights=("FlightDate", "count"),  
    AvgArrivalDelay=("ArrDelay", "mean"),
    MaxDepartureDelay=("DepDelay", "max")
).reset_index()

# Natijani chiqarish
print(flights_grouped)




# Titanic ma'lumotlarini yuklash
titanic_df = pd.read_excel('lesson-19/homework/data/titanic.xlsx', sheet_name='Sheet1')

# Yoshni tasniflovchi funksiya
def classify_age(age):
    return "Child" if age < 18 else "Adult"

# apply() yordamida yangi ustun yaratish
titanic_df["Age_Group"] = titanic_df["Age"].apply(classify_age)

# Natijaning bir qismini chiqarish
print(titanic_df[["Age", "Age_Group"]].head())


# Employee ma'lumotlarini yuklash
employee_df = pd.read_csv("lesson-19\homework\data\employee.csv")

# Normallashtirish funksiyasi
def normalize(column):
    return (column - column.min()) / (column.max() - column.min())

# Har bir bo‘lim bo‘yicha ish haqlarini normallashtirish
employee_df["Normalized_Salary"] = employee_df.groupby("DEPARTMENT")["BASE_SALARY"].transform(normalize)

# Natijaning bir qismini chiqarish
print(employee_df[["DEPARTMENT", "BASE_SALARY", "Normalized_Salary"]].head())


# Movie ma'lumotlarini yuklash
movie_df = pd.read_csv("lesson-19\homework\data\movie.csv")

# Davomiylik bo‘yicha tasniflovchi funksiya
def classify_duration(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"

# apply() yordamida yangi ustun yaratish
movie_df["Duration_Category"] = movie_df["duration"].apply(classify_duration)

# Natijaning bir qismini chiqarish
print(movie_df[["duration", "Duration_Category"]].head())


import pandas as pd

# Titanic datasetini yuklash
titanic_dff = pd.read_excel('lesson-19/homework/data/titanic.xlsx', sheet_name='Sheet1')

# Funksiyalar yaratish
def filter_survivors(df):
    return df[df["Survived"] == 1]

def fill_missing_age(df):
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df

def create_fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df

# Pipeline orqali amallarni bajarish
titanic_cleaned = (titanic_dff
                   .pipe(filter_survivors)
                   .pipe(fill_missing_age)
                   .pipe(create_fare_per_age))

print(titanic_cleaned.head())


# Funksiyalar yaratish
def filter_delayed_flights(df):
    return df[df["DepDelay"] > 30]

def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / df["CRSElapsedTime"]
    return df

# Pipeline orqali amallarni bajarish
flights_cleaned = (flights_df
                   .pipe(filter_delayed_flights)
                   .pipe(add_delay_per_hour))

print(flights_cleaned.head())