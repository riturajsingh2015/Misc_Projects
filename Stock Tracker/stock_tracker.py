import os, sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import json
import decimal
import locale

#----------Files---------#
stock_names="stock_list.txt"
stock_data_file="stock_data.json"

#----------SiteUrl ---------#
site_url='https://www.google.com/'

#---------Get Stock_names-----# from File--#
with open(stock_names) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
stock_names = [x.strip() for x in content]
#--------Setup Chrome Test-----------------#
options = Options()
options.headless = True
CHROMEDRIVER_PATH=r'C:\Users\Singh\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
#--- Method to retrieve and display stockprices----#

def stocks_price_retriever(stock_names):
    stocks_price_list=[]
    for stock in stock_names:
        driver.get(site_url)
        search_box=driver.find_element_by_css_selector('input[type="text"]')
        search_query="NSE: "+stock
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        stock_price=driver.find_element_by_xpath("//*[@id='knowledge-finance-wholepage__entity-summary']/div/g-card-section/div/g-card-section/span[1]/span/span[1]").text
        #stock_price=stock_price.replace(',', '.')
        locale.setlocale(locale.LC_ALL, 'de_DE')
        stock_price = locale.atof(stock_price, decimal.Decimal)
        stock_price='{}'.format(stock_price)
        stock_price=float(stock_price)
        stocks_price_list.append(stock_price)
    return stocks_price_list

def stocks_price_shower(stock_names,stocks_price_list):
    for idx, stock_name in enumerate(stock_names):
        print(stock_name +"   "+ stocks_price_list[idx])
#----------------Generate Stockpricelist----------------------------#
stocks_price_list=(stocks_price_retriever(stock_names))
current_date_time=str(datetime.datetime.now())

#-----Reading an writing to json file---###
def read_json(filepath,stock_names): # handles whether file exists or not
    try:
        with open(filepath) as json_file:
            return json.load(json_file)
    except: # if file doesnot exist
        with open(filepath, 'w') as json_file:
            data={}
            for i in range(len(stock_names)):
                data[stock_names[i]] = list()
                base_price={"base_price":stocks_price_list[i],"datetime":current_date_time}
                data[stock_names[i]].append(base_price)
            json.dump(data, json_file)
            json_file.close()
            return read_json(filepath,stock_names)


def write_json(filepath,stock_names,stocks_price_list):
    data=read_json(filepath,stock_names)
    # make changes to the data
    for i in range(len(stock_names)):
        json_object={
        'price': stocks_price_list[i],
        'datetime':current_date_time
        }
        data[stock_names[i]].append(json_object)

    with open(filepath, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()

script_path = os.path.dirname(os.path.abspath( __file__ ))
filepath=script_path+"/"+stock_data_file

write_json(filepath,stock_names,stocks_price_list)

#--------This should get exceuted only once in a day 'for time sake ' ###


#------Read the data from the file only once-----#
data=read_json(filepath,stock_names)

def stock_avg_price_till_date(stock_name):
    list_corresponding_to_stock=data[stock_name]
    price_list=[entry.get("price") for entry in list_corresponding_to_stock if "price" in entry]
    avg_till_time=sum(price_list)/len(price_list)
    return (avg_till_time)



# adjust base price after 15days on the basis of avg
def base_price_adjuster(stock_name): # modifies stock_data.json file but only the base price
    data[stock_name][0]["datetime"]
    data[stock_name][0]["base_price"]=stock_avg_price_till_date(stock_name) # make the base price the avg price
    with open(stock_data_file, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
