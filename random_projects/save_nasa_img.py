from nasa import apod
import os
import requests
from PIL import Image



os.environ['NASA_API_KEY'] = 'z0AbyDWDUTBz62emA5XsJbeqKiamrqN3kGNzKPFf'
picture = apod.apod('2018-09-01')
image = Image.open(requests.get(picture.url, stream=True).raw)
image.save(f'/Users/matej/Desktop/images_nasa/{picture.title}.jpg')

