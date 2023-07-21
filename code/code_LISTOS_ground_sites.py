import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from PIL import Image
from IPython.display import display 


def plot_single_point_map(df_list, lon, lat, extent=[-125, -75, 20, 60], skip_rows=0, map_image_path=None):
   

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



    colors = ['ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro', 'ro','ro', 'ro', 'ro','ro'];
    for df, color in zip(df_list, colors):
        ax.scatter(df[lon], df[lat], facecolor = 'red', edgecolor = 'black')

    plt.show()

df1 = pd.DataFrame({
    'lon': [-74.192892],
    'lat': [40.720989]
})

df2 = pd.DataFrame({
    'lon': [-73.9020],
    'lat': [40.8162]
})

df3 = pd.DataFrame({
    'lon': [-73.9020],
    'lat': [40.8162]

})

df4 = pd.DataFrame({
    'lon': [-72.07882],
    'lat': [41.35362]

})

df5 = pd.DataFrame({
    'lon': [-73.58382],
    'lat': [41.005047]

})

df6 = pd.DataFrame({
    'lon': [-72.38674],
    'lat': [41.97568]
})

df7 = pd.DataFrame({
    'lon': [-72.679923],
    'lat': [41.771444]
})

df8 = pd.DataFrame({
    'lon': [-72.63158],
    'lat': [41.78471]
})

df9 = pd.DataFrame({
    'lon': [-73.443148],
    'lat': [41.398692]
})

df10 = pd.DataFrame({
    'lon': [-72.63004],
    'lat': [41.55224]
})

df11 = pd.DataFrame({
    'lon': [-73.19476],
    'lat': [41.17086]
})

df12 = pd.DataFrame({
    'lon': [-73.29733],
    'lat': [41.82140]
})


df13 = pd.DataFrame({
    'lon': [-73.10334],
    'lat': [41.15181]
})


df14 = pd.DataFrame({
    'lon': [-73.991994],
    'lat': [40.870436]
})


df15 = pd.DataFrame({
    'lon': [-74.806671],
    'lat': [40.515262]
})

df16 = pd.DataFrame({
    'lon': [-74.676301],
    'lat': [40.787628]
})

df17 = pd.DataFrame({
    'lon': [-74.192892],
    'lat': [40.720989]
})


df18 = pd.DataFrame({
    'lon': [-74.255544],
    'lat': [41.058617]
})


df19 = pd.DataFrame({
    'lon': [-73.966180],
    'lat': [40.853550]
})

df20 = pd.DataFrame({
    'lon': [-74.861491],
    'lat': [39.684250]
})


df21 = pd.DataFrame({
    'lon': [-72.07882 ],
    'lat': [41.35362]
})

df22 = pd.DataFrame({
    'lon': [-73.58382],
    'lat': [41.005047 ]
})

df23 = pd.DataFrame({
    'lon': [-73.9020],
    'lat': [40.8162]
})

df24 = pd.DataFrame({
    'lon': [-73.9020],
    'lat': [ 40.8162]
})

df25 = pd.DataFrame({
    'lon': [-73.9020],
    'lat': [40.8162]
})

df26 = pd.DataFrame({
    'lon': [-72.55018],
    'lat': [41.25984]
})


df27 = pd.DataFrame({
    'lon': [-72.5533 ],
    'lat': [41.2568]
})


df28 = pd.DataFrame({
    'lon': [-72.5533],
    'lat': [41.2568]

})

df29 = pd.DataFrame({
    'lon': [-73.87809],
    'lat': [40.86790]
})


df30 = pd.DataFrame({
    'lon': [-73.87809],
    'lat': [40.86790]
})

df31 = pd.DataFrame({
    'lon': [-73.87809],
    'lat': [40.86790]

})


df32 = pd.DataFrame({
    'lon': [-73.87809],
    'lat': [40.86790]

})


df33 = pd.DataFrame({
    'lon': [-73.87809],
    'lat': [41.005047]

})


df34 = pd.DataFrame({
    'lon': [-73.8781],
    'lat': [40.8679]
})


df35 = pd.DataFrame({
    'lon': [-73.8781],
    'lat': [40.8679]
})     

df36 = pd.DataFrame({
    'lon': [-73.880341],
    'lat': [40.861706]
})

df37 = pd.DataFrame({
    'lon': [-73.139046],
    'lat': [40.961017]
})

df38 = pd.DataFrame({
    'lon': [-73.139046],
    'lat': [40.961017]
})

df39 = pd.DataFrame({
    'lon': [-73.139046],
    'lat': [40.961017]
})

df40 = pd.DataFrame({
    'lon': [-73.139046],
    'lat': [40.96101]
})

df41 = pd.DataFrame({
    'lon': [-73.82153],
    'lat': [40.73614]
})

df42 = pd.DataFrame({
    'lon': [-73.13905],
    'lat': [40.96101]
})

df43 = pd.DataFrame({
    'lon': [-72.7],
    'lat': [41.2]
})

df44 = pd.DataFrame({
    'lon': [-74.126081],
    'lat': [40.670250]
})

df45 = pd.DataFrame({
    'lon': [-74.1261],
    'lat': [40.6703]
})

df46 = pd.DataFrame({
    'lon': [-74.1261],
    'lat': [40.6703]
})

df47 = pd.DataFrame({
    'lon': [-73.94825],
    'lat': [40.81976]
})

df48 = pd.DataFrame({
    'lon': [-72.9029],
    'lat': [41.3014]
})

df49 = pd.DataFrame({
    'lon': [-74.4294],
    'lat': [40.4622]
})

df50 = pd.DataFrame({
    'lon': [-74.4294],
    'lat': [40.4622]
})

df51 = pd.DataFrame({
    'lon': [-74.429439],
    'lat': [40.462182]
})

df52 = pd.DataFrame({
    'lon': [-74.4316],
    'lat': [40.4665]
})

df53 = pd.DataFrame({
    'lon': [-73.33681],
    'lat': [41.11822]
})

df53 = pd.DataFrame({
    'lon': [-73.3367],
    'lat': [41.1183]
})

df53 = pd.DataFrame({
    'lon': [-73.336753],
    'lat': [41.118228]
})

df53 = pd.DataFrame({
    'lon': [-73.3369],
    'lat': [41.1180]
})


df_list = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20, df21, df22, df23, df24, df25, df26, df27, df28, df29, df30, df31, df32, df33, df34, df35, df36, df37, df38, df39, df40, df41, df42, df43, df44, df45, df46, df47, df48, df49, df50, df51, df52, df53]


map_image_path = '/Users/anabellebrodsky/Desktop/NASA/ADMG/platform-visualization/blueMarble.png'

plot_single_point_map(df_list, 'lon', 'lat', extent = [-81, -66, 33, 46],
                         skip_rows=0, map_image_path=map_image_path)
                         #to visualize east coat extent = [-80.7, -67.5, 36.5, 45.4]
                        #to visualize california extent = [-124.5, -113.5, 32.5, 42]
                        #to visualize lower midwest extent =[-125, -85, 25, 45]  
                        #to have zoomed out view of upper midwest extent = [-130, -70, 25, 60]
                        #to have more zoomed in view of upper midwest extent = [-125, -104, 40, 50]
                        #zoomed out east coast [-81, -66, 33, 46]
                        #kentucky to indiana [-89, -74, 33, 43]
                        #east coast [-90, -65, 24, 49]
                        #lower east coast [-88, -74, 29, 39]
                        #zoomed out view incuding eastern canada [-88, -50, 23, 55]
                        #zoomed out west coast [-135, -105, 25, 52]
                        #Southern california [-124.5, -114.1, 32.5, 42.1]

