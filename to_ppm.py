import pandas as pd

df = pd.read_csv(
    "output.csv")
df["coordinate"] = df["coordinate"].transform(
    lambda s: (int(s.split(",")[1]), int(s.split(",")[0])))

print("P3")
print("2000 2000")
print("255")

m = dict()
for x, y in zip(df["coordinate"], df["pixel_color"]):
    m[f"{x}"] = y

for y in range(0, 2000):
    for x in range(0, 2000):
        pp = f"({y}, {x})"
        z = m.get(pp)
        if z is None:
            print("255 255 255")
        else:
            p = z
            value = int(p[1:], 16)
            r = (value & 0xFF0000) >> 16
            g = (value & 0x00FF00) >> 8
            b = (value & 0x0000FF) >> 0
            print(f"{r} {g} {b}")
