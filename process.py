from flask import jsonify
from googlesearch import search
import os
import pandas as pd
import json
import pyrebase

# Open recycle data
data_file_name = os.path.abspath('nw-hack/recycle-data.csv')
data = pd.read_csv(data_file_name)

# Initialize firebase
config = {
    "apiKey": "AIzaSyApyB34Te2NlD7d3apnJFlt39yY5ltUeqY",
    "authDomain": "binit-420.firebaseapp.com",
    "databaseURL": "https://binit-420.firebaseio.com",
    "projectId": "binit-420",
    "storageBucket": "binit-420.appspot.com",
    "messagingSenderId": "834490258600",
    "appId": "1:834490258600:web:cc5d308b029138851d5e9d",
    "measurementId": "G-514TEBL75N"
}
firebase = pyrebase.initialize_app(config)


def processLabels(labels):

    # Process labels
    labels = json.loads(labels)['payload']
    for label in labels:
        actions = data.loc[data['Item'].str.match(label['description'])]['Action'].values
        if actions.size > 0:
            addToDB(label['description'], "hits")
            return generatePacket(label['description'], "You can " + actions[0] + " it!")

    addToDB(labels[0]['description'], "mishits")
    return generatePacket(labels[0]['description'], "I'm not sure!")


def generatePacket(label, action):

    try:
        results = search("how to recycle " + label, tld='com', lang='en', num=2, start=0, stop=1, pause=2.0)
        for j in results:
            print(j)
            link = j

    except:
        link = "https://www.google.ca"

    return jsonify(label, action, link)


def addToDB(label, table):
    db = firebase.database()
    dbData = {"label": label}
    db.child(table).push(dbData)


def getList():
    db = firebase.database()
    data = db.child('hits').get().val()

    labels = []
    for label in data.values():
        labels.append(list(label.values())[0])

    return list(labels)



#
# if __name__ == '__main__':
#     getList()