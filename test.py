import io
import os
import pandas as pd

def clense_csv():
    df = pd.read_csv('recycle-data.csv')
    cf = pd.DataFrame(columns={'Item', 'Action'})
    print(df.head())

    i = 0
    for index, row in df.iterrows():
        items = row[0].strip().split(',')
        items = list(filter(None, items))

        for item in items:
            cf.loc[i] = [item, row[1]]
            i += 1

        print(items)

    print(cf.columns)
    print(cf.head())
    cf.to_csv('san.csv')

def processImage():

    # Open recycle data
    data_file_name = os.path.abspath('recycle-data.csv')
    data = pd.read_csv(data_file_name)

    # Process JSON
    action = data.loc[data['Item'].str.match('Food')]['Action'].values[0]
    print(action)

if __name__ == '__main__':
    processImage()
    # clense_csv()