#! python
# Main script

import functions  # custom-made functions.py file to be used as module
import threading
import time

print('STARTING PROGRAM... \n')

##########################################
# Download raw data
##########################################

# Raw data url's
housing_price_url = 'https://www.ons.gov.uk/generator?uri=/economy/inflationandpriceindices/bulletins/housepriceindex/april2022/ce532115&format=csv'
electric_price_url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53e/mm23'

# Run the functions simultaneously using threading
download_data_thread_1 = threading.Thread(target=functions.download_uk_electric_data, args=[electric_price_url])
download_data_thread_2 = threading.Thread(target=functions.download_uk_housing_data, args=[housing_price_url])
download_data_thread_1.start()
download_data_thread_2.start()

time.sleep(1)

organise_data_thread_1 = threading.Thread(target=functions.organise_uk_housing_data)
organise_data_thread_2 = threading.Thread(target=functions.organise_uk_electric_data)
organise_data_thread_1.start()
organise_data_thread_2.start()

time.sleep(1)
print('done.'.upper())