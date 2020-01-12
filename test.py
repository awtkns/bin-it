import os
import pandas as pd

# Open recycle data
data_file_name = os.path.abspath('nw-hack/recycle-data.csv')
data = pd.read_csv(data_file_name)

def processLabels(labels):

    # Process JSON
    action = data.loc[data['Item'].str.match('Food')]['Action'].values[0]
    return action

# if __name__ == '__main__':
#     processData()