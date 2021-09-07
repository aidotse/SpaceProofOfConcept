import matplotlib.pyplot as plt
from pathlib import Path
import xarray as xr

path_src = Path("ex")

patches_20x20_ex = [
    "agriculture_1_2019_i0.nc",
    "archipelago_2020_i12.nc",
    "gothenburg_2020_i12.nc",
    "gotland_2020_i1.nc",
    "kebnekaise_2019_i117.nc",
    "oresund_2019_i0.nc",
    "rural_1_2020_i12.nc",
    "rural_2_2020_i0.nc",
    "vellinge_2019_i0.nc",
]
patches_10x10_ex = [
    "agriculture_1_2019_i0_500_500_1000_1000.nc",
    "archipelago_2020_i12_500_700_1000_1000.nc",
    "gothenburg_2020_i12_500_500_1000_1000.nc",
    "gotland_2020_i1_1000_0_1000_1000.nc",
    "kebnekaise_2019_i117_500_500_1000_1000.nc",
    "oresund_2019_i0_500_500_1000_1000.nc",
    "rural_1_2020_i12_500_500_1000_1000.nc",
    "rural_2_2020_i0_500_500_1000_1000.nc",
    "vellinge_2019_i0_800_700_1000_1000.nc",
]

i = 0  # patch no
path_20x20_i = path_src.joinpath(patches_20x20_ex[i])
path_10x10_i = path_src.joinpath(patches_10x10_ex[i])
ds_20x20 = xr.open_dataset(path_20x20_i, chunks={"time": 10})
ds_10x10 = xr.open_dataset(path_10x10_i, chunks={"time": 10})


da_20x20 = ds_20x20[["B04_10m", "B03_10m", "B02_10m"]].to_array()
da_10x10 = ds_10x10[["B04_10m", "B03_10m", "B02_10m"]].to_array()

da_20x20.plot.imshow(size=10, vmin=0, vmax=2500)
plt.axis("square")
da_10x10.plot.imshow(size=10, vmin=0, vmax=2500)
plt.axis("square")

plt.show()
