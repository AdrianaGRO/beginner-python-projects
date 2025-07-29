"""
Project: City Information
Description: Create a nested dictionary mapping city names to information such as country, population, landmarks, and coordinates. Implement functions to retrieve, update, and manage city information, including finding the closest city.

# TODO-1: Create a nested dictionary with city names as keys and info (country, population, landmarks, coordinates) as values.
# TODO-2: Define a function that takes a city name (string) as an argument and retrieves its information.
# TODO-3: In the function, look up the city in the dictionary.
# TODO-4: If the city exists, return a formatted string with its information.
# TODO-5: If the city does not exist, return a message indicating it is not found.
# TODO-6: Add a function to update the information for an existing city.
# TODO-7: Add a function to change a city’s name (key) in the dictionary.
# TODO-8: Add coordinates (latitude, longitude) to each city and a function to find the closest city to given coordinates.


Output Format:
London is in UK, has a population of 8.9 million, and landmarks: Big Ben, London Eye.

Sample Call:
get_city_info("London")
# Expected: London is in UK, has a population of 8.9 million, and landmarks: Big Ben, London Eye.

Note: Use hard-coded values for testing, not input().
"""

cities_info = {
    "London": {
        "country": "UK",
        "population": "8.9 million",
        "landmarks": ["Big Ben", "London Eye"],
        "coordinates": {"latitude": 51.5074, "longitude": -0.1278}
    },
    "New York": {
        "country": "USA",
        "population": "8.4 million",
        "landmarks": ["Statue of Liberty", "Central Park"],
        "coordinates": {"latitude": 40.7128, "longitude": -74.0060}
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "landmarks": ["Tokyo Tower", "Shibuya Crossing"],
        "coordinates": {"latitude": 35.6762, "longitude": 139.6503}
    },
    "Bucharest": {
        "country": "Romania",
        "population": "1.8 million",
        "landmarks": ["Palace of the Parliament", "Old Town"],
        "coordinates": {"latitude": 44.4268, "longitude": 26.1025}
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "landmarks": ["Eiffel Tower", "Louvre Museum"],
        "coordinates": {"latitude": 48.8566, "longitude": 2.3522}
    },
    "Berlin": {
        "country": "Germany",
        "population": "3.6 million",
        "landmarks": ["Brandenburg Gate", "Berlin Wall"],
        "coordinates": {"latitude": 52.5200, "longitude": 13.4050}
    },
    "Madrid": {
        "country": "Spain",
        "population": "3.2 million",
        "landmarks": ["Prado Museum", "Royal Palace"],
        "coordinates": {"latitude": 40.4168, "longitude": -3.7038}
    },
    "Rome": {
        "country": "Italy",
        "population": "2.8 million",
        "landmarks": ["Colosseum", "Vatican City"],
        "coordinates": {"latitude": 41.9028, "longitude": 12.4964}
    },
    "Moscow": {
        "country": "Russia",
        "population": "12.5 million",
        "landmarks": ["Red Square", "Kremlin"],
        "coordinates": {"latitude": 55.7558, "longitude": 37.6173}
    },
    "Beijing": {
        "country": "China",
        "population": "21 million",
        "landmarks": ["Great Wall", "Forbidden City"],
        "coordinates": {"latitude": 39.9042, "longitude": 116.4074}
    },  
    "Sydney": {
        "country": "Australia",
        "population": "5.3 million",
        "landmarks": ["Sydney Opera House", "Harbour Bridge"],
        "coordinates": {"latitude": -33.8688, "longitude": 151.2093}
    },
    "Cape Town": {
        "country": "South Africa",
        "population": "4.6 million",
        "landmarks": ["Table Mountain", "Robben Island"],
        "coordinates": {"latitude": -33.9249, "longitude": 18.4241}
    },
    "Rio de Janeiro": {
        "country": "Brazil",
        "population": "6.7 million",
        "landmarks": ["Christ the Redeemer", "Sugarloaf Mountain"],
        "coordinates": {"latitude": -22.9068, "longitude": -43.1729}
    },
    "Istanbul": {
        "country": "Turkey",
        "population": "15 million",
        "landmarks": ["Hagia Sophia", "Blue Mosque"],
        "coordinates": {"latitude": 41.0082, "longitude": 28.9784}
    },
    "Cairo": {
        "country": "Egypt",
        "population": "9.5 million",
        "landmarks": ["Pyramids of Giza", "Sphinx"],
        "coordinates": {"latitude": 30.0444, "longitude": 31.2357}
    },
    "Mumbai": {
        "country": "India",
        "population": "20.4 million",
        "landmarks": ["Gateway of India", "Marine Drive"],
        "coordinates": {"latitude": 19.0760, "longitude": 72.8777}
    },
    "Bangkok": {
        "country": "Thailand",
        "population": "10.5 million",
        "landmarks": ["Grand Palace", "Wat Arun"],
        "coordinates": {"latitude": 13.7563, "longitude": 100.5018}
    },
    "Buenos Aires": {
        "country": "Argentina",
        "population": "15.2 million",
        "landmarks": ["Obelisco", "Casa Rosada"],
        "coordinates": {"latitude": -34.6037, "longitude": -58.3816}
    },
    "Kuala Lumpur": {
        "country": "Malaysia",
        "population": "8.2 million",
        "landmarks": ["Petronas Towers", "Batu Caves"],
        "coordinates": {"latitude": 3.139,"longitude": 101.6869}
    },
    "Seoul": {
        "country": "South Korea",
        "population": "9.7 million",
        "landmarks": ["Gyeongbokgung Palace", "N Seoul Tower"],
        "coordinates": {"latitude": 37.5665, "longitude": 126.9780}
    },
    "Lagos": {
        "country": "Nigeria",
        "population": "14.8 million",
        "landmarks": ["Lekki Conservation Centre", "Nike Art Gallery"],
        "coordinates": {"latitude": 6.5244, "longitude": 3.3792}
    }
}

def get_city(name):
    if name in cities_info:
        return f"{name} has the following informations {cities_info[name]}"
    else:
        return f"{name} not found! Sorry!"

print(get_city("London"))


def update_city(name, new_info):
    if name in cities_info:
        cities_info[name].update(new_info)
        return f"New values for {name} in here: {cities_info[name]}"
    else:
        return f"{name} not found! Sorry!"

print(update_city("Tokyo", {"landmarks": ["Tokyo Tower", "Shibuya Crossing", "Tsukiji Market"]}))

def change_city_name(old_name, new_name):
    if old_name in cities_info:
        cities_info[new_name] = cities_info.pop(old_name)
        return f"City name changed from {old_name} to {new_name}."
    else:
        return f"{old_name} not found!"

print(change_city_name("Bucharest", "London"))



# TODO-8: Add coordinates (latitude, longitude) to each city and a function to find the closest city to given coordinates.

def nearest_city(latitude, longitude):
    if latitude is None or longitude is None:
        return "Invalid coordinates!"
    closest_city = None
    closest_distance = float('inf')
    for city in cities_info:
        city_latitude = cities_info[city]["coordinates"]["latitude"]
        city_longitude = cities_info[city]["coordinates"]["longitude"]
        distance = ((city_latitude - latitude) ** 2 + (city_longitude - longitude) ** 2) ** 0.5
        if distance < closest_distance:
            closest_distance = distance
            closest_city = city
    return f"The closest city to the coordinates ({latitude}, {longitude}), that is located in Romania, Bucharest is {closest_city}."

print(nearest_city(44.4268, 26.1025))

