
import pandas as pd 
import geopandas as gpd 
import numpy as np 
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 
from IPython.display import display 

def plot_navigation(file_name, lon_col = 'Longitude', lat_col = 'Latitude', alt_col = 'Altitude',
                    alt_units = 'km', extent = [-125,-75,20,60], cmap='jet',skip_rows = 0, legend_orientation= 'horizontal'):
  
  #reads a CSV file into a pandas DataFrame, skipping a number of rows from the top as specified by the skip_rows parameter.
  #file_name= '/Users/anabellebrodsky/Desktop/NASA/ADMG/granule1Olympex.excel.xlsx'
  df = pd.read_csv(file_name,skiprows=skip_rows)
  print(df.columns)
  display(df) #displays the DataFrame 
  df = df.replace({-999999: np.nan}) #replaces -999999 with NaN
  
  #converts the DataFrame to a GeoDataFrame, using the longitude and latitude columns as the geometry
  df_gpd = gpd.GeoDataFrame(df,
                          geometry=gpd.points_from_xy(df[lon_col], df[lat_col]),
                          crs='epsg:4326')
  from mpl_toolkits.axes_grid1 import make_axes_locatable
  from matplotlib.ticker import StrMethodFormatter
  # Define the plot CRS
  crs = ccrs.PlateCarree() #sets Coordinate Reference System (CRS) to be Plate Carree, a type of geographic projection 


  # Create the figure
  fig = plt.figure()
  ax = plt.axes(projection=crs)

  fig.set_size_inches(15, 15)  # sets size of plot to be 15 x 15 inches

  
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
  #These lines set the size of the grid labels on the x and y axes.
  
  

  ax.set_extent(extent) #sets the extent of the plot to be the extent specified by the extent parameter
  scatter = df_gpd.plot(ax=ax, column=alt_col,legend=True,cmap=cmap,legend_kwds={'orientation': legend_orientation, 'pad': 0.05, 'aspect':70},vmin=0) #plots the GeoDataFrame on the map, using the altitude column as the color
  if legend_orientation == "horizontal": #sets the size of the legend labels
    cb = fig.axes[1] #sets the colorbar to be the second axis of the figure
    cb.tick_params(labelsize=15) #sets the size of the colorbar labels
    label = "Altitude (" + alt_units + ")" #sets the label of the colorbar
    cb.set_xlabel(label,fontsize=15,weight='bold') #sets the size and weight of the colorbar label
  else: #if the legend orientation is vertical
    cb = fig.axes[1] 
    cb.tick_params(labelsize=15)
    label = "Altitude (" + alt_units + ")"
    cb.set_ylabel(label,fontsize=15,weight='bold')
  
  plt.show() #displays the plot

#ALL OF THE DATA GRAUNLES IN NUMERICAL ORDER
#f = '/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/0IMPACTS_MetNav_P3B_20200125_R1.ict' #sets the file path to the data file
#f = '/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/1IMPACTS_MetNav_P3B_20220225_R0.ict' #file from same platfrom and campagin but just different granule
#f = '/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/2IMPACTS_MetNav_P3B_20220219_R0.ict' 
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/3IMPACTS_MetNav_P3B_20220217_R0.ict'
#f= '/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/4IMPACTS_MetNav_P3B_20220213_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/5IMPACTS_MetNav_P3B_20220208_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/6IMPACTS_MetNav_P3B_20220204_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/7IMPACTS_MetNav_P3B_20220203_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/8IMPACTS_MetNav_P3B_20220129_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/9IMPACTS_MetNav_P3B_20220128_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/10IMPACTS_MetNav_P3B_20220119_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/11IMPACTS_MetNav_P3B_20220117_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/12IMPACTS_MetNav_P3B_20220114_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/13IMPACTS_MetNav_P3B_20220111_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/14IMPACTS_MetNav_P3B_20220106_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/15IMPACTS_MetNav_P3B_20200225_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/16IMPACTS_MetNav_P3B_20200224_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/17IMPACTS_MetNav_P3B_20200220_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/18IMPACTS_MetNav_P3B_20200218_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/19IMPACTS_MetNav_P3B_20200213_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/20IMPACTS_MetNav_P3B_20200207_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/21IMPACTS_MetNav_P3B_20200205_R0.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/22IMPACTS_MetNav_P3B_20200201_R0.ict'
f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/23IMPACTS_MetNav_P3B_20200125_R1.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/24IMPACTS_MetNav_P3B_20200118_R1.ict'
#f='/Users/anabellebrodsky/Desktop/NASA/ADMG/IMPACTS/P-3/25IMPACTS_MetNav_P3B_20200112_R0.ict'
plot_navigation(f, lon_col = 'Longitude', lat_col = 'Latitude', alt_col = 'GPS_Altitude', 
                alt_units = 'm', extent =[-80.7, -67.5, 36.5, 45.4], cmap='jet',
                skip_rows =76) #calls the plot_navigation function, specifying the parameters



#EXTRA FILES
#f = '/Users/anabellebrodsky/Desktop/NASA/ADMG/olympex_naver2_IWG1_20151215-2007.txt
#f= '/Users/anabellebrodsky/Desktop/NASA/ADMG/granule1Olympex.excel.xlsx'