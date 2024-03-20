import requests

# Base URL of the Random User Generator API
BASE_URL = 'https://randomuser.me/api/'


def get_random_user(**params):
    """Fetch a random user with optional parameters.

    :param params: Optional parameters for the API call.
    :return: JSON response containing random user data.
    """
    response = requests.get(BASE_URL, params=params)
    return response.json()


# Example function calls with key parameters

# Fetch a single random user
print(get_random_user())

# Fetch 5 random users
print(get_random_user(results=5))

# Fetch a random female user
print(get_random_user(gender='female'))

# Fetch a random user with a specific password setting
print(get_random_user(password='upper,lower,1-16'))

# Fetch a random user with a specific nationality
print(get_random_user(nat='us'))

# Fetch a random user with certain fields included
print(get_random_user(inc='gender,name,nat'))

# Fetch a random user with certain fields excluded
print(get_random_user(exc='login'))

# Fetch a random user with pagination
print(get_random_user(page=3, results=10, seed='abc'))

# Fetch a random user with no info
print(get_random_user(noinfo=True))

# Fetch a random user with a JSONP callback
print(get_random_user(callback='randomuserdata'))
