# Place Data

This repo computes the most frequent color for each pixel in r/place 2022.

# Output

![Most Frequent Pixels](./result.png)

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
