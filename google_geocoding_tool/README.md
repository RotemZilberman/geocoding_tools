# Google Geocoding Tool
The Google Geocoding Tool is a Python-based utility designed to process addresses, geocode them using the Google Geocoding API, and output the results in a structured format. This tool is especially useful for applications that require converting physical addresses into geographical coordinates (latitude and longitude).
## Project Structure
|-- geocoding_google_tool
|   |-- conversing.py  # Main Python script for geocoding logic
|   |-- pyproject.toml # Configuration file with dependencies and API key
|   |-- README.md          # This documentation
## Key Components
 - conversing.py: The main script for reading input files, geocoding addresses via the Google Geocoding API, and writing the output.

 - pyproject.toml: Contains configurations like API keys and dependencies.

## Prerequisites
Before you begin, ensure you have the following:
 - Python 3.8 or later installed on your system.
 - Pip (Python package manager) installed. If not, install pip using:
```
python -m ensurepip --upgrade
```
 - A valid Google API Key with access to the Geocoding API.

## Installation Dependencies
Dependencies are listed in the pyproject.toml file. Use the following command to install the required packages: (make sure that you are in the folder of the instolation file after unzip it)

```
pip install .
```

Run the Code:
In the code change the Key Line to your api google key:

```
API_KRY = <INPUT HERE>
```

Write in the terminal:
```
python converting.py
```

### Usage

Input File:
Prepare a CSV file containing the addresses to be geocoded.

Execution:
Run the executable and provide the input file path, output path, and API key when prompted.

Output File:
The geocoded results will be saved to the specified output path.
