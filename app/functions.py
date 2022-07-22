#! python3
# Functions.py

import requests
import os
import datetime
import csv
from pathlib import Path
import zipfile
import openpyxl

##################################################
#   Gathering and organising raw data
##################################################

##########################################
# Download and organise raw data for UK housing prices
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
    print(f'downloaded UK housing price data - DONE - time taken = {end_time}'.upper())

    return raw_csv_data


def organise_uk_housing_data():
    # Parse, clean and organise csv data

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
    print(f'organised UK housing price data - DONE - time taken = {end_time}'.upper())

##########################################
# Download and organise raw data for UK electricity cpi index
##########################################


def download_uk_electric_cpi_change_data(raw_csv_data):
    # Download UK electricity CPI (Consumer Price Index 2015=100) price data

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
    print(f'downloaded UK electricity CPI price data - DONE - time taken = {end_time}'.upper())

    return raw_csv_data


def organise_uk_electric_cpi_change_data():
    # Parse, clean and organise csv data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    # Read the raw csv  data
    with open('../raw data/electricdata/ukcpielectricindex.csv') as csv_file:
        dict_reader = csv.DictReader(csv_file, ['Date', 'Value'])  # Create own headers
        csvRows = []
        for row in dict_reader:
            if dict_reader.line_num < 9 or dict_reader.line_num > 42:  # remove irrelevant rows of data from file
                continue
            csvRows.append(row)

    # Write out the csv file to a clean file
    csv_obj = open(os.path.join('../raw data/electricdata', 'cleanukcpielectricindex.csv'), 'w', newline='')
    csv_writer = csv.DictWriter(csv_obj, ['Date', 'Value'])
    csv_writer.writeheader()
    for row in csvRows:
        csv_writer.writerow(row)
    csv_obj.close()

    end_time = datetime.datetime.now() - start_time
    print(f'organised UK electricity CPI price data - DONE - time taken = {end_time}'.upper())


##########################################
# Download and organise raw data for UK gas cpi index
##########################################

def download_uk_gas_cpi_change_price(raw_csv_data):
    # Download UK gas CPI (Consumer Price Index 2015=100) price data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    res = requests.get(raw_csv_data)
    res.raise_for_status()  # Use to time how long the function takes to complete

    # create folder to store the data
    os.makedirs('../raw data/gasdata', exist_ok=True)

    # Download the .csv file data
    raw_data_file = open(os.path.join('../raw data/gasdata', 'ukcpigasindex.csv'), 'wb')
    for chunk in res.iter_content(100000):
        raw_data_file.write(chunk)
    raw_data_file.close()

    end_time = datetime.datetime.now() - start_time
    print(f'downloaded UK gas CPI price data - DONE - time taken = {end_time}'.upper())

    return raw_csv_data


def organise_uk_gas_cpi_change_data():
    # Parse, clean and organise csv data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    # Read the raw csv  data
    with open('../raw data/gasdata/ukcpigasindex.csv') as csv_file:
        dict_reader = csv.DictReader(csv_file, ['Date', 'Value'])  # Create own headers
        csvRows = []
        for row in dict_reader:
            if dict_reader.line_num < 9 or dict_reader.line_num > 42:  # remove irrelevant rows of data from file
                continue
            csvRows.append(row)

    # Write out the csv file to a clean file
    csv_obj = open(os.path.join('../raw data/gasdata', 'cleanukcpigasindex.csv'), 'w', newline='')
    csv_writer = csv.DictWriter(csv_obj, ['Date', 'Value'])
    csv_writer.writeheader()
    for row in csvRows:
        csv_writer.writerow(row)
    csv_obj.close()

    end_time = datetime.datetime.now() - start_time
    print(f'organised UK gas CPI price data - DONE - time taken = {end_time}'.upper())


##########################################
# Download and organise raw data for UK water supply cpi index
##########################################


def download_uk_water_cpi_change_data(raw_csv_data):
    # Download then save UK water cpi data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    res = requests.get(raw_csv_data)
    res.raise_for_status()

    # create folder to store the data
    os.makedirs('../raw data/watersupplydata', exist_ok=True)

    # Download the .csv file data
    raw_data_file = open(os.path.join('../raw data/watersupplydata', 'ukcpiwaterindex.csv'), 'wb')
    for chunk in res.iter_content(100000):
        raw_data_file.write(chunk)
    raw_data_file.close()

    end_time = datetime.datetime.now() - start_time
    print(f'downloaded UK water supply data - DONE - time taken = {end_time}'.upper())

    return raw_csv_data


def organise_uk_water_cpi_change_data():
    # Parse, clean and organise csv data

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    # Read the raw csv  data
    with open('../raw data/watersupplydata/ukcpiwaterindex.csv') as csv_file:
        dict_reader = csv.DictReader(csv_file, ['Date', 'Value'])  # Create own headers
        csvRows = []
        for row in dict_reader:
            if dict_reader.line_num < 9 or dict_reader.line_num > 42:  # remove irrelevant rows of data from file
                continue
            csvRows.append(row)

    # Write out the csv file to a clean file
    csv_obj = open(os.path.join('../raw data/watersupplydata', 'cleanukcpiwaterindex.csv'), 'w', newline='')
    csv_writer = csv.DictWriter(csv_obj, ['Date', 'Value'])
    csv_writer.writeheader()
    for row in csvRows:
        csv_writer.writerow(row)
    csv_obj.close()

    end_time = datetime.datetime.now() - start_time
    print(f'organised UK water supply data - DONE - time taken = {end_time}'.upper())

##########################################
# Download and organise raw data for UK consumer price index CPI
##########################################


def download_uk_cpi_data(raw_csv_data):
    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    res = requests.get(raw_csv_data)
    res.raise_for_status()

    # create folder to store the data
    os.makedirs('../raw data/cpi', exist_ok=True)

    # Download the .zip file data
    raw_data_file = open(os.path.join('../raw data/cpi', 'ukcpi.zip'), 'wb')
    for chunk in res.iter_content(100000):
        raw_data_file.write(chunk)
    raw_data_file.close()

    end_time = datetime.datetime.now() - start_time
    print(f'downloaded UK Consumer price index (CPI) data - DONE - time taken = {end_time}'.upper())

    return raw_csv_data


def organise_uk_cpi_data():
    # Unzip, clean and read the cpi .csv file

    start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

    p = Path('../raw data/cpi/')

    # Unzip the .zip file
    data_zip = zipfile.ZipFile(p / 'ukcpi.zip')
    data_zip.extractall(p)

    # Get the .csv file (CPI file only) from the .zip extracted folder
    for filename in p.glob('API*.csv'):
        uk_cpi_file = filename

    # Read the csv file
    csv_rows = []
    with open(uk_cpi_file) as csv_file:
        reader_obj = csv.reader(csv_file)
        for row in reader_obj:
            if reader_obj.line_num != 87 and reader_obj.line_num != 5:
                continue  # Skip all other rows besides 5 and 87
            csv_rows.append(row)
        csv_file.close()

        # Write out the csv file
        csv_file_obj = open(os.path.join(p, 'ukcpi.csv'), 'w', newline='')
        csv_writer = csv.writer(csv_file_obj)
        for row in csv_rows:
            csv_writer.writerow(row)
        csv_file_obj.close()

    end_time = datetime.datetime.now() - start_time
    print(f'unzipped and organised UK CPI data - DONE - time taken = {end_time}'.upper())


##########################################
# Download and organise T212 personal holdings
##########################################

# def download_t212_data():
#     pass
#
#
# def organise_t212_data():
#     pass


##################################################
# Converting .csv files to .xlsx files
##################################################

def convert_csv_to_excel(csv_file):
    # Convert .csv files to .xlsx in preparation for chart plotting

    wb = openpyxl.Workbook()
    ws = wb.active

    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)

        xlsx_file = csv_file.rstrip('.csv') + '.xlsx'
        wb.save(xlsx_file)

    print(f'converted {os.path.basename(csv_file)} to .xlsx format'.upper())

##########################################
# Plotting .xlsx files to chart/graphs
##########################################

