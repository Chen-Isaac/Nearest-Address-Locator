# Nearest Address Locator

## Overview

The `nearest_address_locator.py` script helps you find the nearest location from a set of possible destinations, which all serve the same purpose. This is particularly useful in scenarios where you need to choose the most convenient location from multiple options.

For example:

- **Chinese citizens applying for a Japanese tourist visa**: Personal applications are not allowed, so you must apply through one of the agencies designated by the Japanese embassy or consulate in China. For someone like me who has a poor sense of direction, this tool uses the Amap API to find the closest designated agency to my home.
- **Company health check-ups**: Your company may offer annual health check-ups at several partner clinics, and you want to select the one closest to your home.
- **Dental cleaning appointments**: A well-known dental chain has many branches, and you want to find the branch nearest to your location for your dental cleaning appointment.

### Why Amap (Gaode)?

Amap (高德地图) is widely used in mainland China for navigation and location services. It is known for its highly accurate geolocation and comprehensive coverage across the country. When trying to find the nearest location within mainland China, using Amap's API provides more precise and reliable results compared to other options. This is why Amap's API is ideal for obtaining accurate driving distances and geocoding information in China.

## How It Works

1. **Input Data**: The script reads a list of addresses from an Excel file, which should include a column with addresses.
2. **Origin Location**: The user specifies a starting point (origin) in plain text, and the script uses Amap’s API to convert this into geographical coordinates.
3. **Distance Calculation**: The script uses Amap’s API to calculate the driving distance between the origin and each destination address.
4. **Nearest Address**: After calculating the driving distances, the script identifies and returns the address with the shortest distance to the origin location.

## Usage

### Prerequisites

- Python 3.x
- Required libraries: `pandas`, `requests`
- A valid **Amap API key**

You can install the required libraries using pip:

```bash
pip install pandas requests
```
### API Key Setup
To use this script, you will need to apply for an Amap API key. You can find your API key at the following link after registration:

https://console.amap.com/dev/key/app

When running the script, it will prompt you to enter your API key.

```bash
# In the terminal
Please enter your Amap API key: [Your API Key]
```

### Input Format
The input Excel file should have the following columns:
- address: The list of addresses to compare.
- Other columns (e.g., 地域, 名称) can be included for additional information but are not required for the distance calculation.

The Excel file 100712233.xlsx used in the source code was downloaded from the website of Consulate-General of Japan in Shanghai.

### Running the Script
1. Ensure your Excel file contains a list of addresses under the address column, along with any other relevant details.
2. Run the script in your terminal:
    ```bash
    # In the terminal
    python nearest_address_locator.py
    ```
3. Input your starting location when prompted, and the script will calculate the nearest destination.

### Amap API Limits
Amap’s basic LBS services, including driving route planning and geocoding, allow up to 5,000 free requests per day. This should be more than enough for personal daily use.

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