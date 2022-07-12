#! python3
# Functions.py

import requests
import os
import datetime
import csv

##################################################
#   Gathering and organising raw data
##################################################

##########################################
# Download raw data for UK housing prices
##########################################


def download_uk_housing_data(raw_csv_data):
    # Download then save UK housing price data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    res = requests.get(raw_csv_data)
    res.raise_for_status()

    # create folder to store the data
    os.makedirs('../raw data/housingprices', exist_ok=True)

    # Download the .csv file data
    raw_data_file = open(os.path.join('../raw data/housingprices', 'ukaveragehouseprice.csv'), 'wb')
    for chunk in res.iter_content(100000):
        raw_data_file.write(chunk)
    raw_data_file.close()

    end_time = datetime.datetime.now() - start_time
    print(f'downloaded UK housing price data - DONE - time taken = {end_time}\n'.upper())

    return raw_csv_data


def organise_uk_housing_data():
    # Parse, clean and organise all csv data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    # Read the raw csv  data
    with open('../raw data/housingprices/ukaveragehouseprice.csv') as csv_file:
        dict_reader = csv.DictReader(csv_file, ['Date', 'England (pop)', 'Wales (pop)', 'Scotland (pop)', 'NI (pop)'])  # Create own headers
        csvRows = []
        for row in dict_reader:
            if dict_reader.line_num < 11:  # remove irrelevant rows of data from file
                continue
            csvRows.append(row)

    # Write out the csv file to a clean file
    csv_obj = open(os.path.join('../raw data/housingprices', 'cleanukaveragehouseprice.csv'), 'w', newline='')
    csv_writer = csv.DictWriter(csv_obj, ['Date', 'England (pop)', 'Wales (pop)', 'Scotland (pop)', 'NI (pop)'])
    csv_writer.writeheader()
    for row in csvRows:
        csv_writer.writerow(row)
    csv_obj.close()

    end_time = datetime.datetime.now() - start_time
    print(f'organised UK housing price data - DONE - time taken = {end_time}\n'.upper())

##########################################
# Download raw data for UK electricity prices
##########################################


def download_uk_electric_data(raw_csv_data):
    # Download then save UK electricity CPI (Consumer Price Index 2015=100) price data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    res = requests.get(raw_csv_data)
    res.raise_for_status()  # Use to time how long the function takes to complete

    # create folder to store the data
    os.makedirs('../raw data/electricdata', exist_ok=True)

    # Download the .csv file data

    raw_data_file = open(os.path.join('../raw data/electricdata', 'ukcpielectricindex.csv'), 'wb')
    for chunk in res.iter_content(100000):
        raw_data_file.write(chunk)
    raw_data_file.close()

    end_time = datetime.datetime.now() - start_time
    print(f'downloaded UK electricity CPI price data - DONE - time taken = {end_time}\n'.upper())

    return raw_csv_data


def organise_uk_electric_data():
    # Parse, clean and organise all csv data

    print('organising UK electricity data...'.upper(), end='')
    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    # Read the raw csv  data
    with open('../raw data/electricdata/ukcpielectricindex.csv') as csv_file:
        dict_reader = csv.DictReader(csv_file, ['Date', 'Value'])  # Create own headers
        csvRows = []
        for row in dict_reader:
            if dict_reader.line_num < 9 or dict_reader.line_num > 42:  # remove irrelevant rows of data from file
                continue
            csvRows.append(row)
            # print(row['Date'], row['England (pop)'], row['Wales (pop)'], row['Scotland (pop)'], row['NI (pop)'])

    # Write out the csv file to a clean file
    csv_obj = open(os.path.join('../raw data/electricdata', 'cleanukcpielectricindex.csv'), 'w', newline='')
    csv_writer = csv.DictWriter(csv_obj, ['Date', 'Value'])
    csv_writer.writeheader()
    for row in csvRows:
        csv_writer.writerow(row)
    csv_obj.close()

    end_time = datetime.datetime.now() - start_time
    print(f'organised UK electricity CPI price data - DONE - time taken = {end_time}\n'.upper())
