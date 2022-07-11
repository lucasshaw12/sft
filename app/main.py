#! python
# Main script

import functions  # custom-made functions.py file to be used as module

print('STARTING PROGRAM... \n')

##########################################
# Download raw data for UK housing prices
##########################################

print('housing price data ----'.upper())
housing_price_url = 'https://www.ons.gov.uk/generator?uri=/economy/inflationandpriceindices/bulletins/housepriceindex/april2022/ce532115&format=csv'
functions.download_uk_housing_data(housing_price_url)
functions.organise_uk_housing_data()

##########################################
# Download raw data for UK electricity prices
##########################################

print('electricity price data ----'.upper())
electric_price_url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53e/mm23'
functions.download_uk_electric_data(electric_price_url)
functions.organise_uk_electric_data()

##########################################
#
##########################################

print('done.'.upper())