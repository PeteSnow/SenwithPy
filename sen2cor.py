# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:16:18 2025

@author: pedro
"""
import subprocess

# Make a change for github_


sen2cor_executable = '"C:/Users/pedro/OneDrive/Documents/Programs/Sen2Cor-02.12.03-win64/L2A_Process.bat"'


# Specify location of the L2A tile
# input_product = '/path/to/S2A_MSIL1C_20250101T000000_N0000_R000_T00T000_20250101T000000.SAFE'

# Or access Sentinel 2 datafrom Copernicus Hub
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
from datetime import datetime

# Login credentials for the Copernicus Open Access Hub
USERNAME = 'pedrososno@gmail.com'  # Replace with your Copernicus username
PASSWORD = 'Sentinel5388!'  # Replace with your Copernicus password

# Connect to the Copernicus Open Access Hub
api = SentinelAPI(USERNAME, PASSWORD, 'https://scihub.copernicus.eu/dhus')

# Define a date range and area of interest 
start_date = datetime(2024, 1, 1)  # Use datetime objects
end_date = datetime(2024, 1, 2)

# Load shapefile using GeoPandas
shapefile_path = "C:/Users/pedro/Dropbox/Database/MOSAIC/Brazil.shp"
gdf = gpd.read_file(shapefile_path)
# Convert shapefile geometry to WKT
# Convert MultiPolygon to WKT
aoi_wkt = gdf.geometry.iloc[0].wkt  # Use `.wkt` attribute instead of `.to_wkt()`




# Run Sen2Cor
subprocess.run([sen2cor_executable, input_product])

