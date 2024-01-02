import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions as ex

path_header = "/html/body/app-root/app-header/header/div"
path_explore = "/app-root/div/main/app-explore/div[2]"

def init():
    global ser
    global op
    global driver

    ser = Service(r"C:/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)

init()

def open_AppEEARS(delay = 3):
    print(" - opening AppEARS")
    driver.maximize_window()
    driver.get("https://appeears.earthdatacloud.nasa.gov")
    time.sleep(delay)
    print(" - opened AppEARS")

def close_AppEEARS():
    print(" - closing AppEEARS")
    driver.close()
    print(" - closed AppEEARS")

def quit_AppEEARS():
    print(" - closing all AppEEARS windows")
    driver.quit()
    print(" - closed all AppEEARS windows")

def login_with_cred (user, pwd, delay = 2):
    try:
        xpath = f"{path_header}/div/ul[2]/li/a"
        driver.find_element(By.XPATH, xpath).click()
    except ex.NoSuchElementException:
        print(" - unable to find login button\n -- will attempt to login")
    except Exception as e:
        print(f" - error : {type(e)}")
    try:
        print(" - logging in to AppEARS")
        time.sleep(delay)
        driver.find_element(By.ID, "username").send_keys(user)
        driver.find_element(By.ID, "password").send_keys(pwd)
        driver.find_element(By.NAME, "commit").click()
        time.sleep(delay)
        print(" - logged in to AppEARS")
    except ex.NoSuchElementException:
        print(" - unable to login\n -- user may not be on login page")
    except Exception as e:
        print(f" - error : {type(e)}")

def go_to_extract_area(delay = 5):
    try:
        time.sleep(delay)
        xpath = '//*[@id="navbarSupportedContent"]/ul[1]/li[1]/a'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(delay)
        xpath = f"{path_header}/div/ul[1]/li[1]/div/a[1]"
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(delay)
        xpath = '/html/body/app-root/div/main/app-task/div[2]/div/div/div/div[1]/div[2]/a/img'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to go to extract area\n -- user may not be logged in")
    except Exception as e:
        print(f" - error : {type(e)}")

def add_product (product, product_num = 1, delay = 2):
    try:
        driver.find_element(By.ID, "product").send_keys((product))
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to find product text\n -- user may not be on extract area page")
    except Exception as e:
        print(f" - error : {type(e)}")
    try:
        xpath = "//button[@class='dropdown-item active ng-star-inserted']"
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(delay)
        product_path = f'//*[@id="top"]/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[3]/div[1]/div[2]/div[{product_num+1}]'    
        driver.find_element(By.XPATH, product_path).click()    
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to find product\n -- user may not have entered a valid product")
    except Exception as e:
        print(f" - error : {type(e)}")
    try:
        xpath = '//*[@id="top"]/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[3]/div[1]/div[1]/app-product-selector/span/span/div[1]'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(delay)
    except:
        print(" - unable to remove product\n -- a product may not have been added")

def enter_dates_from_list(years_list, delay = 2):
    try:
        driver.find_element(By.ID, "startDate").send_keys(years_list[0])
        time.sleep(delay)
        driver.find_element(By.ID, "endDate").send_keys(years_list[1])
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to find dates\n -- user may be on extract area page")
    except Exception as e:
        print(f" - error : {type(e)}")

def add_projection (projection_num = 0, delay = 2):
    try:
        projection = driver.find_element(By.ID, "projection")
        projection.click()
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to find projection\n -- user may be on extract area page")
    except Exception as e:
        print(f" - error : {type(e)}")
    try:
        xpath = f'//*[@id="ngb-typeahead-1-{projection_num}"]'
        #xpath = f'/html/body/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[4]/div/div/div/div[3]/div[2]/app-projection-selector/ngb-typeahead-window/button[{projection_num}]'
        projection_dropdown = driver.find_element(By.XPATH, xpath)
        projection_dropdown.click()
        time.sleep(delay) 
    except ex.NoSuchElementException:
        print(" - unable to find projection\n -- user may have entered invalid projection")
    except Exception as e:
        print(f" - error : {type(e)}")  

def add_area_sample_name(name, delay = 2):
    try:
        driver.find_element(By.ID, "taskName").send_keys(name)
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to sample name\n -- user may be on extract area page")
    except Exception as e:
        print(f" - error : {type(e)}")

def add_file(filepath, delay = 2):
    try:
        file = driver.find_element(By.ID, "shapeFileUpload")
        file.send_keys(filepath)
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to find dates\n -- user may be on extract area page")
    except ex.InvalidArgumentException:
        print(f" - could not find file '{filepath}'\n -- this file may not exist in current or given working directory")
    except Exception as e:
        print(f" - error : {type(e)}")

def submit(delay = 15):
    try:
        text = driver.find_element(By.ID, "taskName")
        text.send_keys(Keys.ENTER)
        time.sleep(delay)
        clear("taskName")
        clear("startDate")
        clear("endDate")
    except ex.NoSuchElementException:
        print(" - unable to sumbit\n -- user may be on extract area page")
    except Exception as e:
        print(f" - error : {type(e)}")

def clear(element_ID, delay = 2):
    try:
        driver.find_element(By.ID, element_ID).clear()
        time.sleep(delay)
    except ex.NoSuchElementException:
        print(" - unable to sumbit\n -- user may be on extract area page")
    except Exception as e:
        print(f" - error : {type(e)}")

def go_to_explore(delay = 3):
    time.sleep(delay)
    xpath = '//*[@id="navbarSupportedContent"]/ul[1]/li[2]/a'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)

def prev(delay = 2):
    xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[1]/a'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)

def page(page_number, delay = 2):
    xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[{page_number+1}]/a'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)

def next(delay = 2):
    page = 1
    while True:
        xpath = xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[{page}]/a'
        try:
            button = driver.find_element(By.XPATH, xpath)
            time.sleep(delay)
        except:
            page -= 1
            xpath = xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[{page}]/a'
            driver.find_element(By.XPATH, xpath).click()
            time.sleep(delay)
            break
        page+=1

def last(delay = 2):
    page = 1
    while True:
        xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[{page}]/a'
        try:
            button = driver.find_element(By.XPATH, xpath)
            time.sleep(delay)
        except:
            page -= 2
            xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[{page}]/a'
            driver.find_element(By.XPATH, xpath).click()
            time.sleep(delay)
            break
        page+=1

def get_num_of_rows(delay = 0):
    i=1
    while True:
        xpath = f'/html/body{path_explore}/table/tbody/tr[{i}]/td[7]/a[2]/i'
        try:
            button = driver.find_element(By.XPATH, xpath)
            time.sleep(delay)
            #time.sleep(1)
        except:
            print(f" - found {i-1} rows")
            return i-1
        i+=1

def get_row_names(p = 0, delay = 0):
    if p!=0:
        page(p)
    row_names = {}
    name_list = []
    num_of_rows = (get_num_of_rows(delay))
    print(f" - creating dictionary of row names and rows")
    for i in range(num_of_rows):
        xpath = f'/html/body{path_explore}/table/tbody/tr[{i+1}]/td[1]/span/span/a'
        text = driver.find_element(By.XPATH, xpath).text
        time.sleep(delay)
        if text in name_list:
            row_names[text].append(i+1)
        else:
            name_list.append(text)
            row_names[text] = [i+1]

    return row_names

def download_area_sample_row(row = 1, delay = 0):

    xpath = f'/html/body{path_explore}/table/tbody/tr[{row}]/td[7]/a[2]/i'
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    time.sleep(delay)

def download_area_sample_name_in_dictionary(dict, name, index = 0, delay = 0):
    row = dict[name]
    if type(row) is not list:
        row = list(row)
    xpath = f'/html/body{path_explore}/table/tbody/tr[{row[index]}]/td[7]/a[2]/i'
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    time.sleep(delay)

def get_num_of_pages (delay = 2):
    page = 1
    while True:
        xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[{page}]/a'
        try:
            button = driver.find_element(By.XPATH, xpath)
            time.sleep(delay)
        except:
            page -= 2
            xpath = f'//*[@id="top"]{path_explore}/table/thead/tr[1]/td/app-pagination-control/div/ul/li[{page}]/a'
            time.sleep(delay)
            print(f" - found {page-1} pages")
            return page -1
        page +=1

def get_all_requests (delay=2):
    page(1)
    pages = get_num_of_pages(delay)
    names_by_page = []
    for i in range(pages):
        names_by_page.append(get_row_names())
        next()
    return names_by_page

def delete_request_by_row (row = 1, delay = 0):
    try:
        xpath = f'//*[@id="top"]/app-root/div/main/app-explore/div[2]/table/tbody/tr[{row}]/td[7]/app-task-delete-confirm/span/a'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(delay)
        xpath = f'//*[@id="top"]/app-root/div/main/app-explore/div[2]/table/tbody/tr[{row}]/td[7]/app-task-delete-confirm/span/a[2]'
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(delay)
    except Exception as e:
        print(f" - error : {type(e)}")

def get_num_supporting_files (delay = 0):
    items = 1
    while True:
        xpath = f'/html/body/app-root/div/main/app-download-task/div[2]/div/div[2]/table/tbody/tr[{items}]/td[1]/a'
        try:
            button = driver.find_element(By.XPATH, xpath)
            time.sleep(delay)
            items+=1  
        except:
            return items
        
def get_all_supporting_files (delay = 0):
    items = get_num_supporting_files(delay)
    files = {}
    for i in range (1,items):
        xpath = f'/html/body/app-root/div/main/app-download-task/div[2]/div/div[2]/table/tbody/tr[{i}]/td[1]/a'
        text = driver.find_element(By.XPATH, xpath).text
        time.sleep(delay)
        files[text] = i
    return files

def download_supporting_file_row (row, delay = 6):
    xpath = f'/html/body/app-root/div/main/app-download-task/div[2]/div/div[2]/table/tbody/tr[{row}]/td[1]/a'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)

def download_supporting_file_name_in_dictionary (dict, name, delay = 6):
    row = dict[name]
    xpath = f'/html/body/app-root/div/main/app-download-task/div[2]/div/div[2]/table/tbody/tr[{row}]/td[1]/a'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)