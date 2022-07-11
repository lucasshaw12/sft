#! python3
# Test functions - to be moved to function.py once working
#
# def download_uk_electric_data(raw_csv_data):
#     # Download then save UK office of national statistics housing price data
#     import requests
#     import os
#
#     res = requests.get(raw_csv_data)
#     res.raise_for_status()
#
#     # create folder to store the data
#     os.makedirs('../raw data/electricdata', exist_ok=True)
#
#     # Download the .csv file data
#     raw_data_file = open(os.path.join('../raw data/electricdata', 'ukcpielectricindex.csv'), 'wb')
#     for chunk in res.iter_content(100000):
#         raw_data_file.write(chunk)
#     raw_data_file.close()
#
#     return raw_csv_data
#
#
# # url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53e/mm23'
#
# def organise_uk_electric_data():
#     # Parse, clean and organise all csv data
#     import csv
#     import os
#
#     # Read the raw csv  data
#     with open('../raw data/electricdata/ukcpielectricindex.csv') as csv_file:
#         dict_reader = csv.DictReader(csv_file, ['Date', 'Value'])  # Create own headers
#         csvRows = []
#         for row in dict_reader:
#             if dict_reader.line_num < 9 or dict_reader.line_num > 42:  # remove irrelevant rows of data from file
#                 continue
#             csvRows.append(row)
#             # print(row['Date'], row['England (pop)'], row['Wales (pop)'], row['Scotland (pop)'], row['NI (pop)'])
#
#     # Write out the csv file to a clean file
#     csv_obj = open(os.path.join('../raw data/electricdata', 'cleanukcpielectricindex.csv'), 'w', newline='')
#     csv_writer = csv.DictWriter(csv_obj, ['Date', 'Value'])
#     csv_writer.writeheader()
#     for row in csvRows:
#         csv_writer.writerow(row)
#     csv_obj.close()
#
# electric_price_url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53e/mm23'
# download_uk_electric_data(electric_price_url)
# organise_uk_electric_data()

import datetime
start_time = datetime.datetime.now()
done_time = datetime.datetime.now() - start_time
print(done_time)
# start_time = time.ctime()
# end_time = time.ctime()
# print(f'{start_time}, {end_time}')