import imageio.v3 as iio
from pathlib import Path

images = list()
for file in Path("terr-fish.jpeg").iterdir():
    if not file.is_file():
        continue

    images.append(iio.imread(file))

print(images)