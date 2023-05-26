import requests

#function to use the facilities endpoint to find the campground ID by name
def get_campground_id(api_key, campground_name):
    base_url = "https://ridb.recreation.gov/api/v1"
    endpoint = "/facilities"
    url = base_url + endpoint

    headers = {
        "Accept": "application/json",
        "apikey": api_key
    }

    params = {
        "query": campground_name,
        "limit": 1
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(f"http response code: {response.status_code}")
        campgrounds_info = response.json()
        if "RECDATA" in campgrounds_info and len(campgrounds_info["RECDATA"]) > 0:
            campground_id = campgrounds_info["RECDATA"][0]["FacilityID"]
            return campground_id
        else:
            print("Campground not found.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None


#function to use the facilities endpoint for details on campsites
def get_available_campsites(api_key, campground_id, start_date, end_date):
    base_url = "https://ridb.recreation.gov/api/v1"
    endpoint = f"/facilities/{campground_id}/campsites"
    url = base_url + endpoint

    headers = {
        "Accept": "application/json",
        "apikey": api_key
    }

    params = {
       
       "start_date": start_date,
        "end_date": end_date,
        "current": "true"
        #"limit": 10  # Change the limit as needed
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(f"http response code: {response.status_code}")
        campsites_info = response.json()
        return campsites_info   
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None