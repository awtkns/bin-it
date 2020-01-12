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
    for label in json.loads(labels)['payload']:
        actions = data.loc[data['Item'].str.match(label['description'])]['Action'].values
        if actions.size > 0:
            addToDB(label['description'], "hits")
            return actions[0]
    addToDB(label['description'], "mishits")
    return "Landfill"


def addToDB(label, table):
    db = firebase.database()
    dbData = {"label": label}
    db.child(table).push(dbData)


# if __name__ == '__main__':
#     processData()