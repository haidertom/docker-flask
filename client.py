import requests
import jsonpickle
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

URL = "http://localhost:5007/task"
IMG_PATH = 'andromeda.jpg'

# create a header, not actually necessary here
content_type = 'image/jpg'
headers = {'content-type':content_type}

# read the image
img = Image.open(IMG_PATH, 'r')
img = np.asarray(img)

# create a data dict which we want to send
data_dict = {'image':img}

# encode into jsonpickle
data = jsonpickle.encode(data_dict)

# make the request and get the response
response = requests.post(URL, data=data, headers=headers)

if response.ok:
    response_dict = jsonpickle.decode(response.content)

    print(f"The response contains {len(response_dict)} entries:")
    print(response_dict)
    
    plt.imshow(response_dict['image'])
    plt.show()

else:
    response.raise_for_status()