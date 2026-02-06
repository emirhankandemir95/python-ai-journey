import random

band_name_list = []


print("Welcome to the band name generator!")
band_numbers = int(input("How many band names do you want?\n3"))

for i in range(band_numbers):
    city_name = input("What's the name of the city you grew up in?\n").strip().title()
    pet_name = input("What's your pet's name?\n").strip().title()
    band_name_list.append(f"{city_name} {pet_name}")
    randomized_picks = random.choice(band_name_list)
    print(f"{i+1}. {randomized_picks}")