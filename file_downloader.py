import requests
import pandas as pd
import matplotlib.pyplot as plt


class FileDownloader:
    def __init__(self, url):
        self.url = url
        self.data = None

    def download(self):
        response = requests.get(self.url)
        self.data = response.content

    def save_data(self, save_path):
        if self.data:
            with open(save_path, 'wb') as file:
                file.write(self.data)
        else:
            print("No data available")

    def visualize(self):
        df = pd.read_csv('save_data.csv', encoding="ISO-8859-1", sep=";")
        data_list = [(row['GESAMT'], row['DISTRICT_NAME']) for i,
                     row in df.iterrows()]

        district_names_list = df['DISTRICT_NAME'].unique()
        district_values_list = []

        for district in district_names_list:
            district_val = 0
            for data in data_list:
                if data[1] is district:
                    district_val += data[0]
            district_values_list.append(district_val)

        plt.figure(figsize=(10, 10))

        plt.pie(district_values_list, labels=district_names_list,
                autopct='%1.1f%%', startangle=90, radius=1.4)

        plt.title('Schüler in jedem Bezirk')

        plt.show()
