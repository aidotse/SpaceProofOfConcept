# Space Proof Of Concept Datasets

Datasets from [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) have been provided by [RISE Space Data Lab](https://rymddatalabbet.se/). 

## Patches and timeseries

Timeseries have been prepared by slicing Sentinel-2 data from the years 2019-2020 over 20x20 km 10 areal patches.   

| Patch             | Type            | Region (Swedish) |
| ----------------- | --------------- | ---------------- |
| **agriculture_1** | farming         | Skåne            |
| **agriculture_2** | farming         | Västra Götaland  |
| **archipelago**   | river mouth     | Götaälv          |
| **gothenburg**    | urban           | Götborg          |
| **gotland**       | open pit mining | Gotland          |
| **kebnekaise**    | mountain        | Kebnekaise       |
| **oresund**       | sea             | Öresund          |
| **rural_1**       | forest          | Småland          |
| **rural_2**       | forest          | Värmland         |
| **vellinge**      | shorline        | Velling          |

The images are quite large 2000x2000 pixels with 12 bands (channels).

For convenience a reduced, cropped, dataset with the size 1000x1000x12 have been prepared. This dataset could be found in the 'crop' directory.

As few examples could be found under the 'example' directory.

## Working with the dataset

The dataset are stored in [NetCDF](https://en.wikipedia.org/wiki/NetCDF) format. We recommend using Python and the [Xarray](http://xarray.pydata.org/en/stable/) module. 

### Installation 
To get started install all requirements in a virtual environment,

```bash
$ python3 -m venv venv
$ venv/bin/pip3 install --upgrade pip
$ venv/bin/pip3 install -r requirements.txt
```

### Loading and plotting the dataset

Run the demo notebook that shows how to load and plot the data,

```bash
$ venv/bin/jupyter-lab demo.ipynb
```
or

```bash
$ venv/bin/python3 demo.py
```

You may also find additional notebook examples [here](https://gitlab.ice.ri.se/sdl/documentation-how-to-notebooks) (just skip the Open Data Cube stuff). 

<!---
We recommend using [Dask](https://dask.org) to speed up computation. It gives a huge performance gain even on a single machine as it also supports multi-threading in addition to distributed computing (assuming of course that you have more than one core :-) Alternatively, you may also use Julia instead of Python. Then you need to use PyCall.jl and load the Xarray library using the code below: 

using PyCall  
`xr = pyimport("xarray”)`  
`ds = xr.open_dataset("./karlstad_2020.nc”)`  
`julia_array = ds.values  # This is a now native Julia array.`  

Distributed.jl and  Dagger.jl can then be used for parallelization, somewhat similar to Dask. 
--->

## Information about Sentinel-2 data in general  

The official website for [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) is quite informative.

Information regarding the [sensor](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/resolutions/radiometric), the frequency bands, etc.

How to [combine](https://gisgeography.com/sentinel-2-bands-combinations/) the Sentinel-2 bands, creating so called "False Color" images. These are meant to help highlight (for us humans), different aspects of what the satellite captures.

## Miscellaneous
[Cloud detection algorithms](https://reader.elsevier.com/reader/sd/pii/S2666017220300092?token=F9F65D197657CA06745DA391448E5392E378E59B8D0A19631FDC8001C3AE0D2D404CCC39881E7EC28A6FC8CA28CAF5E7&originRegion=eu-west-1&originCreation=20210825145047).

