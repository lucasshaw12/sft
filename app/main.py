#! python
# Main script to run from terminal

import functions  # custom-made functions.py file to be used as module
import threading
import time

print('starting program... \n'.upper())

##########################################
# Download and organise/clean raw data
##########################################

# Raw data URLs
housing_price_url = 'https://www.ons.gov.uk/generator?uri=/economy/inflationandpriceindices/bulletins/housepriceindex/april2022/ce532115&format=csv'
electric_price_url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53e/mm23'
uk_cpi_url = 'https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=csv'

# Run the functions simultaneously using threading
download_data_thread_1 = threading.Thread(target=functions.download_uk_electric_data, args=[electric_price_url])
download_data_thread_2 = threading.Thread(target=functions.download_uk_housing_data, args=[housing_price_url])
download_data_thread_3 = threading.Thread(target=functions.download_uk_cpi_data, args=[uk_cpi_url])
download_data_thread_1.start()
download_data_thread_2.start()
download_data_thread_3.start()

time.sleep(1)

organise_data_thread_1 = threading.Thread(target=functions.organise_uk_housing_data)
organise_data_thread_2 = threading.Thread(target=functions.organise_uk_electric_data)
organise_data_thread_3 = threading.Thread(target=functions.organise_uk_cpi_data)
organise_data_thread_1.start()
organise_data_thread_2.start()
organise_data_thread_3.start()

time.sleep(1)
print('done.'.upper())

##########################################
# END
##########################################

##########################################
# Convert .csv files to .xlsx files for chart/graph plotting prep
##########################################

# filepath of .csv files

housing_csv_file = '../raw data/housingprices/cleanukaveragehouseprice.csv'
electric_cpi_csv = '../raw data/electricdata/cleanukcpielectricindex.csv'
uk_cpi_csv = '../raw data/cpi/ukcpi.csv'

convert_data_thread_1 = threading.Thread(target=functions.convert_csv_to_excel, args=[housing_csv_file])  # Housing .csv file
convert_data_thread_2 = threading.Thread(target=functions.convert_csv_to_excel, args=[electric_cpi_csv])  # UK cpi .csv file
convert_data_thread_3 = threading.Thread(target=functions.convert_csv_to_excel, args=[uk_cpi_csv])  # UK electricity CPI .csv file
convert_data_thread_1.start()
convert_data_thread_2.start()
convert_data_thread_3.start()
print('done'.upper())

##########################################
# END
##########################################

