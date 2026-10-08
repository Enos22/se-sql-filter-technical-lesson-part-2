import sqlite3
import pandas as pd

conn = sqlite3.connect('pets_database.db')
cursor = conn.cursor()

#read all of the data from this table:
cats_data = pd.read_sql("SELECT * FROM cats;", conn)
print(cats_data)

#use WHERE with >= to select all cats who are at least 5 years old:

cats_at_least_5yrs_old = pd.read_sql("""
SELECT *
FROM cats
WHERE age >= 5;
""", conn)

print(cats_at_least_5yrs_old)

#use WHERE with BETWEEN to select all rows with values in a range, we could do this by combining the <= and AND operators.
#select the names of all of the cats whose age is between 1 and 3.

age_between_1_and_3 = pd.read_sql("""
SELECT *
FROM cats
WHERE age BETWEEN 1 AND 3;
""", conn)
print(age_between_1_and_3)

#use WHERE column is Not NULL
#select all cats that don't currently belong to an owner:

cats_with_no_owner = pd.read_sql("""
SELECT *
FROM cats
WHERE owner_id is NULL;

""", conn)

print(cats_with_no_owner)

#use WHERE with LIKE
#select all cats with names that start with "M" (or "m"):

cats_names_with_M_or_m = pd.read_sql("""
SELECT *
FROM cats
WHERE name LIKE 'M%';
""", conn)

print(cats_names_with_M_or_m)

#May also use substr

cats_names_with_M_or_m_2 =pd.read_sql("""
SELECT *
  FROM cats
 WHERE substr(name, 1, 1) = "M";
""", conn)

print(cats_names_with_M_or_m_2)

#select all cats with names where the second letter is "a" and the name is four letters long:

names_4letters_long_and_second_letter_is_a = pd.read_sql("""
SELECT *
  FROM cats
 WHERE name LIKE '_a__';
""", conn)

print(names_4letters_long_and_second_letter_is_a)

#May also use substr
names_4letters_long_and_second_letter_is_a_2 = pd.read_sql("""
SELECT *
  FROM cats
 WHERE length(name) = 4 AND substr(name, 2, 1) = "a";
""", conn)

print(names_4letters_long_and_second_letter_is_a_2)

#USE Filter and Aggregate
#count the number of cats who have an owner_id of 1.

count_cats_with_owner_id_of_1 = pd.read_sql("""
SELECT COUNT(owner_id)
  FROM cats
 WHERE owner_id = 1;
""", conn)

print(count_cats_with_owner_id_of_1)

conn.close()
