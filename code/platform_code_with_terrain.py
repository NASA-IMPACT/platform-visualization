import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from PIL import Image
from IPython.display import display 


def plot_navigation_with_map(file_name, lon_col='Longitude', lat_col='Latitude', alt_col='Altitude',
                             alt_units='km', extent=[-125, -75, 20, 60], cmap='jet', skip_rows=0,
                             legend_orientation='horizontal', map_image_path=None):
    # Reads a CSV file into a pandas DataFrame, skipping a number of rows from the top as specified by the skip_rows parameter.
    df = pd.read_csv(file_name, skiprows=skip_rows)
    print(df.columns)
    display(df)  # Displays the DataFrame
    df = df.replace({-999999: np.nan})  # Replaces -999999 with NaN

    # Converts the DataFrame to a GeoDataFrame, using the longitude and latitude columns as the geometry
    df_gpd = gpd.GeoDataFrame(df,
                              geometry=gpd.points_from_xy(df[lon_col], df[lat_col]),
                              crs='epsg:4326')

    # Create the figure and axes with a Plate Carree projection
    fig, ax = plt.subplots(figsize=(12, 9), subplot_kw={'projection': ccrs.PlateCarree()})

    # Add background features
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.STATES, edgecolor='black')
    ax.add_feature(cfeature.OCEAN, alpha=0.8)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.8)
    ax.add_feature(cfeature.RIVERS)

    # Add and format gridlines. Remove top and right labels
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl.top_labels, gl.right_labels = False, False
    gl.xlabel_style = {'size': 15}
    gl.ylabel_style = {'size': 15}

    ax.set_extent(extent)  # Sets the extent of the plot to be the extent specified by the extent parameter

    # Open and display the map image
    if map_image_path: 
        img = Image.open(map_image_path)
        ax.imshow(img, origin='upper', extent=[-180, 180, -90, 90], transform=ccrs.PlateCarree())

    # Plot the data on the map
    scatter = ax.scatter(df[lon_col], df[lat_col], c=df[alt_col], cmap=cmap, vmin=0)

    # Add a colorbar
    cb = plt.colorbar(scatter, orientation='horizontal', pad=0.05, aspect=70)
    cb.set_label("Altitude (" + alt_units + ")", fontsize=15, weight='bold')

    plt.show()


#f = '/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/1IMPACTS_MetNav_P3B_20220225_R0.ict' from impacts 
f ='/Users/anabellebrodsky/Desktop/NASA/ADMG/FIREX-AQ/DC-8/168FIREXAQ-METNAV5HZ_DC8_20190730_R1.ict' #from firex-aq
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/ER-2/2IMPACTS_MetNav_ER2_20220225_R0.ict' #from impacts - ER-2 aircraft
map_image_path = '/Users/anabellebrodsky/Desktop/NASA/ADMG/blueMarble.png'

plot_navigation_with_map(f, lon_col='Longitude', lat_col='Latitude', alt_col='MSL_GPS_Altitude',
                         alt_units='m', extent = [-125, -104, 40, 50], cmap='jet',
                         skip_rows=76, map_image_path=map_image_path)
                         #to visualize east coat extent = [-80.7, -67.5, 36.5, 45.4]
                        #to visualize california extent = [-124.5, -113.5, 32.5, 42]
                        #to visualize lower midwest extent =[-125, -85, 25, 45]  
                        #to have zoomed out view of upper midwest extent = [-130, -70, 25, 60]
                        #to have more zoomed in view of upper midwest extent = [-125, -104, 40, 50]
