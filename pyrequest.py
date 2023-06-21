import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path_header = "/html/body/app-root/app-header/header/div"
path_explore = "/app-root/div/main/app-explore/div[2]"

def vars():
    global driver

ser = Service(r"C:/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

def open_AppEEARS(delay = 3):
    print(" - opening AppEARS")
    driver.maximize_window()
    driver.get("https://appeears.earthdatacloud.nasa.gov")
    time.sleep(delay)
    print(" - opened AppEARS")

def login_with_cred (user, pwd, delay = 2):
    xpath = f"{path_header}/div/ul[2]/li/a"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(pwd)
    driver.find_element(By.NAME, "commit").click()
    time.sleep(delay)
    print(" - logged in to AppEARS")

def go_to_extract_area(delay = 2):
    time.sleep(delay)
    xpath = '//*[@id="navbarSupportedContent"]/ul[1]/li[1]/a'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)
    xpath = f"{path_header}/div/ul[1]/li[1]/div/a[1]"
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)
    xpath = '//*[@id="navbarSupportedContent"]/ul[1]/li[2]/a'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(delay)

def add_product (product, product_num = 1, delay = 2):
    driver.find_element(By.ID, "product").send_keys((product))
    time.sleep(delay)
    xpath = "//button[@class='dropdown-item active ng-star-inserted']"
    button = driver.find_element(By.XPATH, (xpath))
    button.click()
    time.sleep(delay)
    product_path = f'//*[@id="top"]/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[3]/div[1]/div[2]/div[{product_num+1}]'    
    button = driver.find_element(By.XPATH, (product_path))
    button.click()
    time.sleep(delay)
    xpath = '//*[@id="top"]/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[3]/div[1]/div[1]/app-product-selector/span/span/div[1]'
    button = driver.find_element(By.XPATH, (xpath))
    button.click()
    time.sleep(delay)

def enter_dates_from_list(years_list, delay = 2):
    driver.find_element(By.ID, "startDate").send_keys(years_list[0])
    time.sleep(delay)
    driver.find_element(By.ID, "endDate").send_keys(years_list[1])
    time.sleep(delay)

def add_projection (projection_num = 0, delay = 2):
    projection = driver.find_element(By.ID, "projection")
    projection.click()
    time.sleep(delay)
    xpath = f'//*[@id="ngb-typeahead-1-{projection_num}"]'
    #xpath = f'/html/body/app-root/div/main/app-task/div[2]/form/div[2]/div/app-area-selector/div/div[4]/div/div/div/div[3]/div[2]/app-projection-selector/ngb-typeahead-window/button[{projection_num}]'
    projection_dropdown = driver.find_element(By.XPATH, xpath)
    projection_dropdown.click()
    time.sleep(delay)   

def add_area_sample_name(name, delay = 2):
    driver.find_element(By.ID, "taskName").send_keys(name)
    time.sleep(delay)

def add_file(filepath, delay = 2):
    file = driver.find_element(By.ID, "shapeFileUpload")
    file.send_keys(filepath)
    time.sleep(delay)

def submit(delay = 15):
    text = driver.find_element(By.ID, "taskName")
    text.send_keys(Keys.ENTER)
    time.sleep(delay)
    clear("taskName")
    clear("startDate")
    clear("endDate")

def clear(element_ID, delay = 2):
    driver.find_element(By.ID, element_ID).clear()
    time.sleep(delay)

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


def contents_row(row = 1, delay = 0):

    xpath = f'/html/body{path_explore}/table/tbody/tr[{row}]/td[7]/a[2]/i'
    button = driver.find_element(By.XPATH, xpath)
    button.click()
    time.sleep(delay)

def contents_name_in_dictionary(dict, name, index = 0, delay = 0):
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


def get_all_requests(delay=2):
    page(1)
    pages = get_num_of_pages(delay)
    names_by_page = []
    for i in range(pages):
        names_by_page.append(get_row_names())
        next()
    return names_by_page

def get_element_by_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)
