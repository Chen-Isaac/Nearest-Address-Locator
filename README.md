# Nearest Address Locator

## Overview

The `nearest_address_locator.py` script helps you find the nearest location from a set of possible destinations, which all serve the same purpose. This is particularly useful in scenarios where you need to choose the most convenient location from multiple options.

For example:

- **Chinese citizens applying for a Japanese tourist visa**: Personal applications are not allowed, so you must apply through one of the agencies designated by the Japanese embassy or consulate in China. For someone like me who has a poor sense of direction, this tool uses the Amap API to find the closest designated agency to my home.
- **Company health check-ups**: Your company may offer annual health check-ups at several partner clinics, and you want to select the one closest to your home.
- **Dental cleaning appointments**: A well-known dental chain has many branches, and you want to find the branch nearest to your location for your dental cleaning appointment.

### Why Amap (高德)?

Amap (高德地图) is widely used in mainland China for navigation and location services. It is known for its highly accurate geolocation and comprehensive coverage across the country. When trying to find the nearest location within mainland China, using Amap's API provides more precise and reliable results compared to other options. This is why Amap's API is ideal for obtaining accurate driving distances and geocoding information in China.

## How It Works

1. **Input Data**: The script reads a list of addresses from an Excel file, which should include a column with addresses.
2. **Origin Location**: The user specifies a starting point (origin) in plain text, and the script uses Amap’s API to convert this into geographical coordinates.
3. **Distance Calculation**: The script uses Amap’s API to calculate the driving distance between the origin and each destination address.
4. **Nearest Address**: After calculating the driving distances, the script identifies and returns the address with the shortest distance to the origin location.

## Usage

### Prerequisites

- **Python 3.11.3**: This script requires Python version 3.11.3. I recommend using pyenv to manage Python versions more easily. This tool allows you to switch between different Python versions for different projects and is very convenient for managing multiple Python installations.

  If you're unfamiliar with how to use pyenv, I suggest searching online or checking the official documentation for guidance. Due to space constraints, I won’t go into detail here, but a quick Google search for "how to install Python using pyenv" should give you plenty of useful resources.

- **Amap API key**: You will need to register and apply for an API key [here](https://console.amap.com/dev/key/app).
- **Excel file**: The Excel file (100712233.xlsx) should contain a list of addresses under an "address" column and other optional columns for additional information (e.g., "地域" and "名称").

### Setting Up the Environment (on macOS)

1. **Clone the repository**: In the terminal, first use `cd` to navigate to the directory where you want to store the project. Then run the following command to clone the repository:
    ```bash
    git clone https://github.com/Chen-Isaac/Nearest-Address-Locator.git
    ```
2. **Change into the project directory**: After cloning, navigate into the project folder.
    ```bash
    cd Nearest-Address-Locator
    ```
3. **Create and activate a virtual environment**: Set up a virtual environment to manage dependencies.   
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
4. **Install required libraries**: Once the virtual environment is activated, install the required dependencies using the provided requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```
   
### Running the Script

1. After activating the virtual environment and installing the dependencies, run the Python script:
    ```bash
    python nearest_address_locator.py
    ```
2. The script will prompt you to enter:
   - **Starting location**: Enter the name of your starting location.
   - **Amap API key**: The script will ask for the API key you obtained from Amap. Input the key when prompted.

3. The script will process the Excel file, calculate the driving distances and durations between the starting location and all addresses listed, and return the nearest address based on distance.

### Amap API Limits

- **API Limitations**: Amap provides 5,000 free requests per day for their basic services, including geocoding and route calculation. This should be sufficient for personal use, but consider reviewing their [pricing and quota limits](https://console.amap.com/) if you need more requests.

### Deactivating the Virtual Environment

- When you're done working in the virtual environment, deactivate it by running the following command:
    ```bash
    deactivate
    ```

## References
To learn more about the API used in this script, you can refer to the official Amap API documentation:

- [Geocoding/Reverse Geocoding](https://lbs.amap.com/api/webservice/guide/api/georegeo)
- [Driving Route Planning](https://lbs.amap.com/api/webservice/guide/api/direction)

These documentation links provide examples and details on how the API function, including parameters, response formats, and additional features you can use in your own projects.

## Support the Project
If you find this project useful and would like to support future development, consider making a donation. Your contributions are greatly appreciated!

For domestic users (China):
You can support me via Alipay:
![Alipay QR Code](./images/alipay_qr.png)

For international users:
You can support me via PayPal:
![PayPal QR Code](./images/paypal_qr.png)