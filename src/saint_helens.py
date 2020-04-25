# download file:
# 10-meter DEM (with vertical units in feet)
# http://gis.ess.washington.edu/data/raster/tenmeter/byquad/hoquiam/f2323.zip

#%%
#import numpy as np
#from rasterio.transform import from_bounds, from_origin
#from rasterio.warp import reproject, Resampling
#import rasterio
#dem_raster = rasterio.open('../data/f2323.dem')
#src_crs = dem_raster.crs
#src_shape = src_height, src_width = dem_raster.shape

# %%
import osgeo
from osgeo import gdal
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

gdal_data = osgeo.gdal.Open("../data/f2323.dem")
data_array = gdal_data.ReadAsArray().astype(np.float)

fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
plt.contour(data_array, cmap = "viridis", 
            levels = list(range(0, 5000, 100)))
plt.title("Elevation Contours of Mt. Shasta")
cbar = plt.colorbar()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#%%
data_array[data_array==-32767.] = np.nan
plt.imshow(data_array, cmap="gist_earth")
plt.colorbar()
plt.show()

#%%
data_array /= 3.28084 # convert to metres
x = np.arange(data_array.shape[1])
y = np.arange(data_array.shape[0])
x, y = np.meshgrid(x, y)
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_surface(x, y, data_array, cmap="gist_earth", linewidth=0, vmin=676, vmax=2951)
