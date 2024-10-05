import pandas as pd
import requests

# Function to get location coordinates from the Amap API
def get_location(address, key):
    base_url = "https://restapi.amap.com/v3/geocode/geo"

    # Set request parameters
    params = {
        'address': address,
        'key': key,
        'output': 'JSON'
    }

    # Send GET request
    response = requests.get(base_url, params)

    # Check response status
    if response.status_code == 200:
        result = response.json()
        if result['status'] == '1' and result['geocodes']:
            location = result['geocodes'][0]['location']
            return True, location
        else:
            return False, "Location not found"
    else:
        return False, "API request failed"

# Function to get the driving distance and duration between two locations
def get_distance(orig_loc, dest_loc, key):
    base_url = "https://restapi.amap.com/v3/direction/driving"

    # Set request parameters
    params = {
        'key': key,
        'origin': orig_loc,
        'destination': dest_loc,
        'output': 'JSON'
    }

    # Send GET request
    response = requests.get(base_url, params)

    # Check response status
    if response.status_code == 200:
        result = response.json()
        if result['status'] == '1' and result['route']:
            distance = result['route']['paths'][0]['distance']
            duration = result['route']['paths'][0]['duration']
            return True, distance, duration
        else:
            return False, "Driving route not found", "Driving route not found"
    else:
        return False, "API request failed", "API request failed"



origin_address = input("Please enter your starting location: ")


# Ask the user to input their API key
print("You can find the API key you applied for at https://console.amap.com/dev/key/app.")
api_key = input("Please enter your Amap API key: ")

# Get the location for the origin address
origin_location_found, origin_location = get_location(origin_address, api_key)

if origin_location_found:
    df = pd.read_excel('100712233.xlsx', header=4, usecols=['地域', '名称', 'address'])
    shanghai_df = df[df['地域'] == '上海']
    address_column = shanghai_df['address']

    shortest_duration = None
    shortest_distance = None
    index = None

    # Iterate through the addresses and calculate distances and durations
    for i, destination_address in enumerate(address_column):
        destination_location_found, destination_location = get_location(destination_address, api_key)
        print(f"Coordinates for address '{destination_address}': {destination_location}")
        if destination_location_found:
            path_found, drive_distance, drive_duration = get_distance(origin_location, destination_location, api_key)
            print(f"from {origin_address} to {destination_address}, the distance is {drive_distance}m, and it will take {drive_duration}s.")
            if  shortest_distance is None or drive_distance < shortest_distance:
                shortest_distance = drive_distance
                shortest_duration = drive_duration
                index = i
        else:
            print(f"The destination address {destination_address} is not found from the Amap API.")

    if index is not None:
        print(f"The nearest location is {address_column.iloc[index]}."
              f"From {origin_address} to {address_column.iloc[index]}, the distance is {shortest_distance}m and it will take {shortest_duration}s.")
    else:
        print("No valid addresses found or unable to calculate the distance.")
else:
    print(f"The origin {origin_address} is not found from the Amap API. Stopping further analysis.")