import requests

# Make a GET request to the API endpoint
response = requests.get("https://api.tvmaze.com/schedule/full")

# Check for successful response
if response.status_code == 200:
    # Parse the JSON response
    schedule = response.json()

    # Access data from the schedule (a list of dictionaries)
    for show in schedule:
        name = show["show"]["name"]
        episode_name = show["name"]
        airtime = show["airtime"]
        print(f"{name}: {episode_name} at {airtime}")
else:
    print(f"Error: {response.status_code}")
