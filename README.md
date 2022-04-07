# Place Data

This repo computes the most frequent color for each pixel in r/place 2022.

# Output

![Most Frequent Pixels](./result.png)

# Download and Extract Reddit Place Data

```sh
# Warning: extracted csv is ~21 GiB
curl https://placedata.reddit.com/data/canvas-history/2022_place_canvas_history.csv.gzip -o 2022_place_canvas_history.csv.gz
gunzip 2022_place_canvas_history.csv.gz
```

# Instructions

```sh
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python main.py

mv output/*.csv output.csv
python to_ppm.py >result.ppm

# Linux Specific
convert result.ppm result.png
```
