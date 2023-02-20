# The Locker Scrape
import chromedriver_autoinstaller
import csv
from datetime import datetime
import os
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

def wait_clickable_then_find(path, wait_time: int = 10):
	WebDriverWait(drv, wait_time).until(
		ec.element_to_be_clickable((By.CSS_SELECTOR, path)))
	return drv.find_element(By.CSS_SELECTOR, path)


def get_info_from_plyr_page(data: list):
	info_to_search = [player_fullname_css, birthdate_css, profile_item_5_css, profile_item_6_css]
	info_as_strings = ['fullname', 'birthdate', 'fivbID', 'nationality']
	player_details = []
	for css in info_to_search:
		try:
			string = wait_clickable_then_find(css).text
			player_details.append(string)
		except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
			if player_details[0]:
				warning = f'Could not find {info_as_strings[info_to_search.index(css)]} ' \
						  f'for {player_details[0]}'
			else:
				warning = f'Could not find {info_as_strings[info_to_search.index(css)]}'
			print(warning)
			player_details.append("NA")

	fullname, birthdate, fivbID, nationality = player_details

	# if fivbID ends up being a string, then that person has 7 profile items and we need to re-insert them
	if fivbID[0].isalpha():
		fivbID = player_details[3]
		nationality = wait_clickable_then_find(profile_item_7_css).text

	tournaments = wait_clickable_then_find(tournament_info_css)
	tournaments = tournaments.text.splitlines()[1:]

	for i in tournaments:
		split_info = i.split(" ", 2)
		details = split_info[2].split(" ")
		rank = details[-2]
		date = " ".join(details[:2])
		event_type = details[2]
		details = details[3:]
		year = split_info[1]
		location = "NA"

		for text in details:
			if "(" in text:
				location = text.replace("(", '').replace(")", '')

		tournament_info = [player_details[0], birthdate, year, date, event_type, location, rank, fivbID, nationality]

		data.append(tournament_info)
		print(name)

now = datetime.now().strftime("%H-%M_on_%d-%m-%Y")

# check if correct chromedriver version is installed, otherwise install the correct version to this script's path
chromedriver_autoinstaller.install()

raw_info = []
# convert csv datafile to list of rows
with open('player_list.csv', newline='', encoding="utf8") as f:
	clean_info = list(csv.reader(f))[1:]  # set removes any unique values

# build chromedriver
srv = Service("\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--headless')
op.add_argument('--disable-gpu')

# items to be interacted with
accept_cookies_btn_css = "#onetrust-accept-btn-handler"
searchbar_valid_css = "#PlayersDatabase > div.row > div > div.ranking-filters.hidden-xs > div.custom-input-search > form > input.ng-pristine.ng-valid"
searchbar_dirty_css = "#PlayersDatabase > div.row > div > div.ranking-filters.hidden-xs > div.custom-input-search > form > input.ng-valid.ng-dirty"
more_details_css = '#PlayersDatabase > div.row > div > div.row.no-gutters-md > div > div > ul > li.ranking-list-item.ng-scope > div > div.ranking-list-item-table.hidden-xs > div > div > div > div > span.ranking-button > a'
player_fullname_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details-header > p"
birthdate_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(1) > span"
profile_item_5_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(5) > span"
profile_item_6_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(6) > span"
profile_item_7_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(7) > span"
tournament_info_css = "#player-partners-table > div > div > div > ul"

data = []
with webdriver.Chrome(service=srv, options=op) as drv:
	drv.get("https://www.fivb.com/en/beachvolleyball/beachplayersdatabase")
	
	cookie_count = 0
	cookies = wait_clickable_then_find(accept_cookies_btn_css)
	cookies.click()

	for name in clean_info:
		try:
			searchbar = wait_clickable_then_find(searchbar_valid_css, 5)
		except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
			searchbar = wait_clickable_then_find(searchbar_dirty_css, 5)

		searchbar.click()
		searchbar.send_keys(name)

		try:
			more_details_btn = wait_clickable_then_find(more_details_css)
			more_details_btn.click()

			get_info_from_plyr_page(data)

			drv.back()

		# timeout on the More Details btn -- say player couldn't be found and continue
		except selenium.common.exceptions.TimeoutException:
			print("No Player Found - " + str(name))
			missing_player = [name, "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]
			data.append(missing_player)
			searchbar.clear()

		try:
			wait_clickable_then_find(searchbar_valid_css, 3).clear()
		except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
			wait_clickable_then_find(searchbar_dirty_css, 3).clear()


print(data)

# create output csv with the data
with open(f'output_{now}.csv', 'w', newline='') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(["Player Name", "Date of Birth", "Event Year", "Event Date", "Event Type", "Location", "Rank", "fivbID", "Nationality"])
	for row in data:
		writer.writerow(row)

os.startfile(f'output_{now}.csv')
