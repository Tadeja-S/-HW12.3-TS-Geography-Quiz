# Homework 12.3: Geography Quiz

import random

countries_cities = {"Austria": "Vienna", 
                    "Belgium": "Brussels", 
                    "Bulgaria": "Sofia", 
                    "Croatia": "Zagreb", 
                    "Republic of Cyprus": "Nicosia", 
                    "Czech Republic": "Prague", 
                    "Denmark": "Copenhagen", 
                    "Estonia": "Tallinn", 
                    "Finland": "Helsinki", 
                    "France": "Paris", 
                    "Germany": "Berlin", 
                    "Greece": "Athens", 
                    "Hungary": "Budapest", 
                    "Ireland": "Dublin", 
                    "Italy": "Rome", 
                    "Latvia": "Riga", 
                    "Lithuania": "Vilnius", 
                    "Luxembourg": "Luxembourg", 
                    "Malta": "Valletta", 
                    "Netherlands": "Amsterdam", 
                    "Poland": "Warsaw", 
                    "Portugal": "Lisbon", 
                    "Romania": "Bucharest", 
                    "Slovakia": "Bratislava", 
                    "Slovenia": "Ljubljana", 
                    "Spain": "Madrid",
                    "Sweden": "Stockholm"}

def geo_quiz():
    country = random.choice(list(countries_cities.keys()))
    capital = countries_cities[country]

    print(f"What is the capital city of {country}?")
    answer = input("Answer: ")

    if answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Wrong! The capital city of {country} is {capital}.")

    user_input = input("Do you want to guess again? (Y/N)")

    if user_input.lower() == "y":
        geo_quiz()
    else:
        print("Thank you for playing!")

geo_quiz()