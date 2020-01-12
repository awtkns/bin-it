import io
import os
import pandas as pd

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath('google-auth.json')

def processImage():
    # # Instantiates a client
    # client = vision.ImageAnnotatorClient()
    #
    # # The name of the image file to annotate
    # file_name = os.path.abspath('example/example01.jpg')
    #
    # # Loads the image into memory
    # with io.open(file_name, 'rb') as image_file:
    #     content = image_file.read()
    #
    # image = types.Image(content=content)
    #
    # # Performs label detection on the image file
    # response = client.label_detection(image=image)
    # labels = response.label_annotations
    #
    # print('Labels:')
    # for label in labels:
    #     print(label.description)

    # Open recycle data
    data_file_name = os.path.abspath('recycle-data.csv')
    data = pd.read_csv(data_file_name)

    # Process JSON
    print(data.head())

if __name__ == '__main__':
    processImage()