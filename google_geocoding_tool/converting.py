import pandas as pd
import requests
from tqdm import tqdm
from pathlib import Path

API_KRY = "you most enter a key"

def geocode_address(api_key, address):
    """
    Use Google Geocoding API to get latitude and longitude for a given address.
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            # return the latitude and longitude and the confidence
            return location["lat"], location["lng"], data["results"][0]["geometry"]["location_type"]
        else:
            print(f"Error: {data['status']} for address {address}")
            return None, None, None
    else:
        print(f"HTTP error {response.status_code} for address {address}")
        return None, None, None

def process_file(file_path, api_key, output_path):
    """
    Process a CSV or Excel file, geocode the addresses, and save the output.
    """
    # Determine file format and read the file
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV file.")

    # Check if the address column exists
    if 'Address' not in df.columns:
        raise ValueError(f"Address column Address not found in the file.")

    # Add columns for latitude and longitude
    df["Latitude"] = None
    df["Longitude"] = None
    df["Confidence"] = None

    # Geocode each address
    for i, address in tqdm(enumerate(df['Address']), total=len(df)):
        print(f"Processing address {i + 1}/{len(df)}: {address}")
        lat, lng, conf = geocode_address(api_key, address)
        df.at[i, "Latitude"] = lat
        df.at[i, "Longitude"] = lng
        df.at[i, "Confidence"] = conf

    # Save the output
    df.to_csv(output_path, index=False)
    print(f"Geocoded data saved to {output_path}")


def main():
    input_file = input("Enter the path to the input CSV file: ").strip()
    output_file = input("Enter the path to save the output file: ").strip()
    google_api_key = input("Enter your Google API key: (enter if you want to use the default key) ").strip()
    google_api_key = google_api_key if google_api_key else API_KRY

    # Call the processing function
    process_file(input_file, google_api_key, output_file)

# Main execution
if __name__ == "__main__":
    main()
