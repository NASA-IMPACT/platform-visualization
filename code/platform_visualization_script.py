
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from IPython.display import display

def plot_navigation(file_name, lon_col = 'Longitude', lat_col = 'Latitude', alt_col = 'Altitude',
                    alt_units = 'km', extent = [-125,-75,20,60], cmap='jet',skip_rows = 0, legend_orientation= 'horizontal'):
  df = pd.read_csv(file_name,skiprows=skip_rows)
  display(df)
  df = df.replace({-999999: np.nan})
  df_gpd = gpd.GeoDataFrame(df,
                          geometry=gpd.points_from_xy(df[lon_col], df[lat_col]),
                          crs='epsg:4326')
  from mpl_toolkits.axes_grid1 import make_axes_locatable
  from matplotlib.ticker import StrMethodFormatter
  # Define the plot CRS
  crs = ccrs.PlateCarree()


  # Create the figure
  fig = plt.figure()
  ax = plt.axes(projection=crs)

  fig.set_size_inches(15, 15)  # Increase the size of the plot

  
  # Add background features
  ax.add_feature(cfeature.LAND,edgecolor='black')
  ax.add_feature(cfeature.STATES,edgecolor='black')
  ax.add_feature(cfeature.OCEAN,alpha=0.8)
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
  

  ax.set_extent(extent)  # Broaden extent of plot
  scatter = df_gpd.plot(ax=ax, column=alt_col,legend=True,cmap=cmap,legend_kwds={'orientation': legend_orientation, 'pad': 0.05, 'aspect':70},vmin=0)
  if legend_orientation == "horizontal":
    cb = fig.axes[1]
    cb.tick_params(labelsize=15)
    label = "Altitude (" + alt_units + ")"
    cb.set_xlabel(label,fontsize=15,weight='bold')
  else:
    cb = fig.axes[1]
    cb.tick_params(labelsize=15)
    label = "Altitude (" + alt_units + ")"
    cb.set_ylabel(label,fontsize=15,weight='bold')
  
  plt.show()

f = '/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS_MetNav_P3B_20200125_R1.ict'
plot_navigation(f, lon_col = 'Longitude', lat_col = 'Latitude', alt_col = 'GPS_Altitude',
                alt_units = 'm', extent =[-80.7, -67.5, 36.5, 45.4], cmap='jet',
                skip_rows =76)