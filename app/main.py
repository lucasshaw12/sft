#! python
# Main script

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