import os
import pandas as pd
import json

# Open recycle data
data_file_name = os.path.abspath('nw-hack/recycle-data.csv')
data = pd.read_csv(data_file_name)

def processLabels(labels):

    # Process labels
    for label in json.loads(labels)['payload']:
        actions = data.loc[data['Item'].str.match(label['description'])]['Action'].values
        if actions.size > 0:
            return actions[0]
    return "Landfill"

# if __name__ == '__main__':
#     processData()