# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import gsw
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

path1 = path1 = r"C:\25cl05001\mvl_lab\ORAS5_1deg_SSS_1990_2008.nc"
data1 = xr.open_dataset(path1)
print(data1)

path2 = r"C:\25cl05001\mvl_lab\ORAS5_1deg_SST_1990_2008.nc"
data2 = xr.open_dataset(path2)
print(data2)

lat = data1['LAT']
lon = data1['LONN179_181']
time = data1['TIME']
sss = data1['SOSALINE']
sst = data2['SOSSTSST']

Arabian_sea_sss = sss.sel(LONN179_181= slice(50,75), LAT = slice(8,27))
Arabian_sea_sst = sst.sel(LONN179_181= slice(50,75), LAT = slice(8,27))
'''

'''
ASAS = gsw.SA_from_SP(Arabian_sea_sss,0,Arabian_sea_sss.LONN179_181,Arabian_sea_sss.LAT)
AST = gsw.SA_from_SP(Arabian_sea_sst,0,Arabian_sea_sst.LONN179_181,Arabian_sea_sst.LAT)
'''

'''
sigma0_ASA_AR=gsw.SA_from_SP(ASAS,0,data1.LONN179_181,data2.LAT)
CT_AR=gsw.CT_from_pt(ASAS,sst)
 
plt.scatter(Arabian_sea_sss,Arabian_sea_sst)
SA_g=np.linspace(np.nanmin(ASAS),np.nanmax(ASAS),60)
CT_g=np.linspace(np.nanmin(CT_AR),np.nanmax(CT_AR),60)
SA_grid,CT_grid=np.meshgrid(SA_g,CT_g)
sigma_grid=gsw.sigma0(SA_grid,CT_grid)
cs=plt.contour(SA_grid,CT_grid,sigma_grid,colors="k")
plt.clabel(cs,fontsize=8)
plt.show()


bay_of_bengal_sss = sss.sel(LONN179_181= slice(76,100), LAT = slice(4,24))
bay_of_bengal_sst = sst.sel(LONN179_181= slice(76,100), LAT = slice(4,24))
bobas = gsw.SA_from_SP(bay_of_bengal_sss,0,bay_of_bengal_sss.LONN179_181,bay_of_bengal_sss.LAT)
CT_BOB=gsw.CT_from_pt(bobas,sst)
plt.scatter(bay_of_bengal_sss,bay_of_bengal_sst)
SA_g_1=np.linspace(np.nanmin(bobas),np.nanmax(bobas),60)
CT_g_1=np.linspace(np.nanmin(CT_BOB),np.nanmax(CT_BOB),60)
SA_grid_1,CT_grid_1=np.meshgrid(SA_g_1,CT_g_1)
sigma_grid_1=gsw.sigma0(SA_grid_1,CT_grid_1)
cs_1=plt.contour(SA_grid_1,CT_grid_1,sigma_grid_1,colors="k")
plt.clabel(cs_1,fontsize=8)
plt.show()


A=gsw.CT_freezing_poly(ASAS,0,1)
B=gsw.CT_maxdensity(ASAS,0)
plt.scatter(Arabian_sea_sss,Arabian_sea_sst)
plt.title('T-S plot over Arabian sea',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)
SA_g = np.linspace(np.nanmin(ASAS),np.nanmax(ASAS),60)
CT_g = np.linspace(-np.nanmin(CT_AR),np.nanmax(CT_AR),60)
SA_grid,CT_grid = np.meshgrid(SA_g,CT_g)
sigma_grid = gsw.sigma0(SA_grid,CT_grid)
cs = plt.contour(SA_grid,CT_grid,sigma_grid,10,colors = "k")
plt.clabel(cs,fontsize = 10)

SA_g2 = np.linspace(np.nanmin(ASAS),np.nanmax(ASAS),60)
CT_1 = gsw.CT_freezing_poly(SA_g2,0,1)
MX_1 = gsw.CT_maxdensity(SA_g2,0)
plt.plot(SA_g2,CT_1,'r--',label= 'Freezing CT')
plt.plot(SA_g2,MX_1,'g--',label= 'Temprature of max density')
plt.legend()


C=gsw.CT_freezing_poly(bobas,0,1)
D=gsw.CT_maxdensity(bobas,0)
plt.scatter(bay_of_bengal_sss,bay_of_bengal_sst)
plt.title('T-S plot over bay of bengal',fontsize = 18)
plt.xlabel("Salinity",fontsize = 12)
plt.ylabel("Temperature",fontsize = 12)
plt.grid(True)
SA_g3 = np.linspace(np.nanmin(bobas),np.nanmax(bobas),60)
CT_g3 = np.linspace(-np.nanmin(CT_BOB),np.nanmax(CT_BOB),60)
SA_grid1,CT_grid1 = np.meshgrid(SA_g3,CT_g3)
sigma_grid1 = gsw.sigma0(SA_grid1,CT_grid1)
cs1 = plt.contour(SA_grid1,CT_grid1,sigma_grid1,10,colors = "k")
plt.clabel(cs1,fontsize = 10)

SA_g4 = np.linspace(np.nanmin(bobas),np.nanmax(bobas),60)
CT_2 = gsw.CT_freezing_poly(SA_g4,0,1)
MX_2 = gsw.CT_maxdensity(SA_g4,0)
plt.plot(SA_g4,CT_2,'r--',label= 'Freezing CT')
plt.plot(SA_g2,MX_2,'g--',label= 'Temprature of max density')
plt.legend()



help(gsw.SA_from_SP)
import cartopy.crs as cc
import cartopy.feature as cf

SA = gsw.SA_from_SP(sss, 0, data1['LONN179_181'],data1['LAT'])
CT = gsw.CT_from_t(sss,sst, 0)
L=gsw.alpha(SA,CT,0)
tm=L.mean(dim="TIME")
plt.figure(figsize=(10,8))
ax=plt.axes(projection=cc.Mercator())
ax.gridlines(draw_labels=True)
ax.add_feature(cf.COASTLINE)
cp=tm.plot.contourf(transform=cc.PlateCarree(),add_colorbar=False)
plt.colorbar(cp,label="°C$^-1$")
ax.add_feature(cf.LAND)
plt.tight_layout()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

