# Open Remote Sensing AI Library Training Data (OpenRSAI-Data)

## Description

OpenRSAI-Data contains training datasets and demonstration data for [OpenRSAI-Core](https://github.com/miron77s/open_rsai) and [OpenRSAI-Algos](https://github.com/miron77s/open_rsai_algos).

## Tutorial

The OpenRSAI-Data is the [Open Remote Sensing AI Library Core](https://github.com/miron77s/open_rsai) library extension that can be installed and used in complex according the [tutorial](https://github.com/miron77s/open_rsai/blob/main/tutorial/TUTORIAL.md).

## Hardware

The full dataset requires 40Gb of free disk space to be downloaded and extracted. The actual dataset size is 30Gb.

## Requirements

To extract the splitted archives of hydro and greenery training dataset the `p7zip` is required by the download scripts:

```
sudo apt-get update
sudo apt-get install p7zip-full
```

## Contents and Installation

The repository contains the following data:
- vector maps of buidings, greenery and hydrography in shape format (`{green|hydro|buildings/vector/osm}` directory);
- QGIS projects for source raster / vector data visualization (`{green|hydro|buildings/vector/qgis}` directory);
- downloadable raster images (`raster` directory):
```
sh download_rasters.sh
```
- downloadable buildings training dataset in Yolo format (`buildings/training` directory):
```
download_building_dataset.sh
```
- downloadable greenery training dataset in MS COCO format (`green/training` directory):
```
download_green_dataset.sh
```
- downloadable hydrography training dataset in MS COCO format (`hydro/training` directory):
```
download_hydro_dataset.sh
```

To download all data simply run:
```
download_all.sh
```

All data is georeferenced using Web-Merkator (EPSG:3395) coordinate system.

## Disclaimer

All data was collected from resources with open public access and is intended exclusively for the training and testing of neural networks.

## Special Thanks

We wish to thank Innovations Assistance Fund (Фонд содействия инновациям, https://fasie.ru/)
for their support in our project within Code-AI program (https://fasie.ru/press/fund/kod-ai/).
