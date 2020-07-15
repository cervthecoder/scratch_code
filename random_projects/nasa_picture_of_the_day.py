from nasa import apod
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
from PIL import Image
import numpy as np



os.environ['NASA_API_KEY'] = 'z0AbyDWDUTBz62emA5XsJbeqKiamrqN3kGNzKPFf'
picture = apod.apod('2003-05-26')
print(picture.title)
image = Image.open(requests.get(picture.url, stream=True).raw)
img = np.array(image)
implt = plt.imshow(img)
plt.show()


