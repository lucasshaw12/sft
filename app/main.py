#! python
# Main script to run from terminal

import functions  # custom-made functions.py file to be used as module
import threading
import time
import datetime

print('starting program...'.upper())
start_time = datetime.datetime.now()  # Use to time how long the function takes to complete

##########################################
# Download and organise/clean raw data
##########################################

# Raw data URLs
housing_price_url = 'https://www.ons.gov.uk/generator?uri=/economy/inflationandpriceindices/bulletins/housepriceindex/april2022/ce532115&format=csv'
electric_price_cpi_change_url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53e/mm23'
gas_price_cpi_change_url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53f/mm23'
uk_cpi_url = 'https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=csv'
water_supply_cpi_change_url = 'https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/timeseries/l53b/mm23'

# Run the functions simultaneously using threading
download_data_thread_1 = threading.Thread(target=functions.download_uk_electric_cpi_change_data, args=[electric_price_cpi_change_url])
download_data_thread_2 = threading.Thread(target=functions.download_uk_housing_data, args=[housing_price_url])
download_data_thread_3 = threading.Thread(target=functions.download_uk_cpi_data, args=[uk_cpi_url])
download_data_thread_4 = threading.Thread(target=functions.download_uk_gas_cpi_change_price, args=[gas_price_cpi_change_url])
download_data_thread_5 = threading.Thread(target=functions.download_uk_water_cpi_change_data, args=[water_supply_cpi_change_url])
download_data_thread_1.start()
download_data_thread_2.start()
download_data_thread_3.start()
download_data_thread_4.start()
download_data_thread_5.start()

print()
time.sleep(5)

organise_data_thread_1 = threading.Thread(target=functions.organise_uk_housing_data)
organise_data_thread_2 = threading.Thread(target=functions.organise_uk_electric_cpi_change_data)
organise_data_thread_3 = threading.Thread(target=functions.organise_uk_cpi_data)
organise_data_thread_4 = threading.Thread(target=functions.organise_uk_gas_cpi_change_data)
organise_data_thread_5 = threading.Thread(target=functions.organise_uk_water_cpi_change_data)
organise_data_thread_1.start()
organise_data_thread_2.start()
organise_data_thread_3.start()
organise_data_thread_4.start()
organise_data_thread_5.start()

print()
time.sleep(5)

##########################################
# END
##########################################

##########################################
# Convert .csv files to .xlsx files for chart/graph plotting prep
##########################################

# filepath of .csv files

housing_csv_file = '../raw data/housingprices/clean_uk_average_house_price.csv'
electric_cpi_change_csv = '../raw data/electricdata/clean_uk_cpi_electric_index.csv'
uk_cpi_csv = '../raw data/cpi/ukcpi.csv'
gas_cpi_change_csv = '../raw data/gasdata/clean_uk_cpi_gas_index.csv'
water_cpi_change_csv = '../raw data/watersupplydata/clean_uk_cpi_water_index.csv'

print()

convert_filetype_data_thread_1 = threading.Thread(target=functions.convert_csv_to_excel, args=[housing_csv_file])  # Housing .csv file
convert_filetype_data_thread_2 = threading.Thread(target=functions.convert_csv_to_excel, args=[electric_cpi_change_csv])  # UK cpi .csv file
convert_filetype_data_thread_3 = threading.Thread(target=functions.convert_csv_to_excel, args=[uk_cpi_csv])  # UK electricity CPI .csv file
convert_filetype_data_thread_4 = threading.Thread(target=functions.convert_csv_to_excel, args=[gas_cpi_change_csv])  # UK gas CPI .csv file
convert_filetype_data_thread_5 = threading.Thread(target=functions.convert_csv_to_excel, args=[water_cpi_change_csv])  # UK water supply CPI .csv file
convert_filetype_data_thread_1.start()
convert_filetype_data_thread_2.start()
convert_filetype_data_thread_3.start()
convert_filetype_data_thread_4.start()
convert_filetype_data_thread_5.start()

time.sleep(3)

##########################################
# END
##########################################

##########################################
# RSS Feeds
##########################################

# BBC RSS Feeds url
print()
bbc_business_feed = 'http://feeds.bbci.co.uk/news/business/rss.xml'
bbc_technology_feed = 'http://feeds.bbci.co.uk/news/technology/rss.xml'
bbc_science_and_environment_feed = 'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml'
bbc_politics_feed = 'http://feeds.bbci.co.uk/news/politics/rss.xml'
bbc_world_feed = 'http://feeds.bbci.co.uk/news/world/rss.xml'
bbc_health_feed = 'http://feeds.bbci.co.uk/news/health/rss.xml'
bbc_education_feed = 'http://feeds.bbci.co.uk/news/education/rss.xml'
bbc_uk_feed = 'http://feeds.bbci.co.uk/news/uk/rss.xml'
morningstar_feed = 'https://uk.investing.com/rss/market_overview.rss'
investing_feed = 'https://uk.investing.com/rss/market_overview.rss'

bbc_rss_data_thread_1 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_business_feed])
bbc_rss_data_thread_2 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_technology_feed])
bbc_rss_data_thread_3 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_science_and_environment_feed])
bbc_rss_data_thread_4 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_politics_feed])
bbc_rss_data_thread_5 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_world_feed])
bbc_rss_data_thread_6 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_uk_feed])
bbc_rss_data_thread_7 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_education_feed])
bbc_rss_data_thread_8 = threading.Thread(target = functions.download_bbc_rss_feed, args=[bbc_health_feed])
morningstar_feed_data_thread = threading.Thread(target = functions.download_morningstar_rss_feed, args=[morningstar_feed])
investing_feed_data_thread = threading.Thread(target = functions.download_investing_rss_feed, args=[investing_feed])

bbc_rss_data_thread_8.start()
bbc_rss_data_thread_7.start()
bbc_rss_data_thread_6.start()
bbc_rss_data_thread_5.start()
bbc_rss_data_thread_4.start()
bbc_rss_data_thread_3.start()
bbc_rss_data_thread_2.start()
bbc_rss_data_thread_1.start()
morningstar_feed_data_thread.start()
investing_feed_data_thread.start()
##########################################
# END
##########################################


##########################################
# PLOTTING EXCEL CHARTS
##########################################

housing_excel_file_to_plot = '../raw data/housingprices/clean_uk_average_house_price.xlsx'
cpi_excel_file_to_plot = '../raw data/cpi/clean_ukcpi.xlsx'
electric_excel_file_to_plot = '../raw data/electricdata/clean_uk_cpi_electric_index.xlsx'
gas_excel_file_to_plot = '../raw data/gasdata/clean_uk_cpi_gas_index.xlsx'
water_excel_file_to_plot = '../raw data/watersupplydata/clean_uk_cpi_water_index.xlsx'

functions.plot_graph_from_excel(housing_excel_file_to_plot)
functions.plot_graph_from_excel(cpi_excel_file_to_plot)
functions.plot_graph_from_excel(electric_excel_file_to_plot)
functions.plot_graph_from_excel(gas_excel_file_to_plot)
functions.plot_graph_from_excel(water_excel_file_to_plot)
##########################################
# END
##########################################

end_time = datetime.datetime.now() - start_time
time.sleep(2)
print(f'\ndone - time taken to run full program = {end_time}'.upper())
