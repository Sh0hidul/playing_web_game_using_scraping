# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome webdriver options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Open the cookie clicker game website
driver.get('https://orteil.dashnet.org/experiments/cookie/')

# Set the end time for the script to run
t_end = time.time() + 60 * 5
# Set the interval for checking and buying items
check_interval = 10
# Set the next check interval
next_check_interval = time.time() + check_interval

# Initialize variables for different items and the total money
money = 0
time_machine = 0
portal = 0
alchemy_lab = 0
shipment = 0
mine = 0
factory = 0
grandma = 0
cursor = 0

# Main loop to run until the end time
while time.time() < t_end:
    # Click on the cookie to earn money
    driver.find_element(By.ID, 'cookie').click()

    # Extract the cost of different items and convert them to integers
    buy_time_machine = driver.find_element(By.ID, 'buyTime machine').text.strip().split('\n')[0].split('-')[1]
    time_machine = int(buy_time_machine.replace(',', ''))

    buy_portal = driver.find_element(By.ID, 'buyPortal').text.strip().split('\n')[0].split('-')[1]
    portal = int(buy_portal.replace(',', ''))

    buy_alchemy = driver.find_element(By.ID, 'buyAlchemy lab').text.strip().split('\n')[0].split('-')[1]
    alchemy_lab = int(buy_alchemy.replace(',', ''))

    buy_shipment = driver.find_element(By.ID, 'buyShipment').text.strip().split('\n')[0].split('-')[1]
    shipment = int(buy_shipment.replace(',', ''))

    buy_mine = driver.find_element(By.ID, 'buyMine').text.strip().split('\n')[0].split('-')[1]
    mine = int(buy_mine.replace(',', ''))

    buy_factory = driver.find_element(By.ID, 'buyFactory').text.strip().split('\n')[0].split('-')[1]
    factory = int(buy_factory)

    buy_grandma = driver.find_element(By.ID, 'buyGrandma').text.strip().split('\n')[0].split('-')[1]
    grandma = int(buy_grandma)

    buy_cursor = driver.find_element(By.ID, 'buyCursor').text.strip().split('\n')[0].split('-')[1]
    cursor = int(buy_cursor)

    # Get the current money available
    money = driver.find_element(By.ID, 'money').text
    money = int(money.replace(',', ''))

    # Check if it's time to make the next purchase
    if time.time() > next_check_interval:
        # Buy the item if its cost is less than or equal to the available money
        if time_machine <= money:
            driver.find_element(By.ID, 'buyTime machine').click()

        elif portal <= money:
            driver.find_element(By.ID, 'buyPortal').click()

        elif alchemy_lab <= money:
            driver.find_element(By.ID, 'buyAlchemy lab').click()
        elif shipment <= money:
            driver.find_element(By.ID, 'buyShipment').click()
        elif mine <= money:
            driver.find_element(By.ID, 'buyMine').click()
        elif factory <= money:
            driver.find_element(By.ID, 'buyFactory').click()
        elif grandma <= money:
            driver.find_element(By.ID, 'buyGrandma').click()
        elif cursor <= money:
            driver.find_element(By.ID, 'buyCursor').click()


        # Set the next check interval and wait for 1 second
        next_check_interval = time.time() + check_interval
        time.sleep(1)
