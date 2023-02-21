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


def get_info_from_plyr_page(data_list: list):
	info_to_search = [player_fullname_css, birthdate_css, profile_item_5_css, profile_item_6_css]
	info_as_strings = ['fullname', 'birthdate', 'fivbID', 'nationality']
	player_details = []

	# for item in info_to_search, check for each of those player details and try to add to player_details
	for css in info_to_search:
		try:
			string = wait_clickable_then_find(css).text
			player_details.append(string)
		except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
			print(f'Could not find {info_as_strings[info_to_search.index(css)]}')
			player_details.append("NA")

	# create names for each player detail
	fullname, birthdate, fivbID, nationality = player_details

	# if first char of fivbID is a string, then that person has 7 profile items and we need to re-arrange them...
	if fivbID[0].isalpha():
		fivbID = player_details[3]
		try:
			nationality = wait_clickable_then_find(profile_item_7_css).text
		except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
			missing_player = [name, "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]
			data_list.append(missing_player)
			return

	tournaments = wait_clickable_then_find(tournament_info_css)
	tournaments = tournaments.text.splitlines()[1:]

	# clean up details from tournament table
	for t in tournaments:
		split_info = t.split(" ", 2)
		details = split_info[2].split(" ")
		rank = details[-2]
		date = " ".join(details[:2])
		event_type = details[2]
		details = details[3:]
		year = split_info[1]
		location = "NA"

		# if there are locations, they will have brackets and use this function to remove them
		for string in details:
			if "(" in string:
				location = string.replace("(", '').replace(")", '')

		tournament_info = [player_details[0], birthdate, year, date, event_type, location, rank, fivbID, nationality]
		data_list.append(tournament_info)
	print(name)


# set time for printing csv files
now = datetime.now().strftime("%H-%M_on_%d-%m-%Y")

# check if correct chromedriver version is installed, otherwise install the correct version to this script's path
chromedriver_autoinstaller.install()

# convert csv datafile to list of rows
with open('player_list.csv', newline='', encoding="utf8") as f:
	clean_info = list(csv.reader(f))[1:]  # set removes any unique values

# items to be interacted with
reject_cookies_btn_css = "#onetrust-reject-all-handler"
searchbar_valid_css = "#PlayersDatabase > div.row > div > div.ranking-filters.hidden-xs > div.custom-input-search > form > input.ng-pristine.ng-valid"
searchbar_dirty_css = "#PlayersDatabase > div.row > div > div.ranking-filters.hidden-xs > div.custom-input-search > form > input.ng-valid.ng-dirty"
more_details_css = '#PlayersDatabase > div.row > div > div.row.no-gutters-md > div > div > ul > li.ranking-list-item.ng-scope > div > div.ranking-list-item-table.hidden-xs > div > div > div > div > span.ranking-button > a'
player_fullname_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details-header > p"
birthdate_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(1) > span"
profile_item_5_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(5) > span"
profile_item_6_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(6) > span"
profile_item_7_css = "#AngularPanel > article > section.section-content > div > div > div > div.container.container-with-space.player-detail-wrapper > div.row > div.col-md-7 > div.player-details > div:nth-child(7) > span"
tournament_info_css = "#player-partners-table > div > div > div > ul"

# build chromedriver -- comment out the --headless and --disable-gpu lines if you want to view the browser in action
srv = Service("\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--headless')
op.add_argument('--disable-gpu')

data = []
with webdriver.Chrome(service=srv, options=op) as drv:
	drv.get("https://www.fivb.com/en/beachvolleyball/beachplayersdatabase")

	for name in clean_info:
		# check if cookies window pops up and if so, click accept cookies button
		try:
			wait_clickable_then_find(reject_cookies_btn_css, 1).click()
		except:
			pass

		# check which version of the searchbar is shown (valid or dirty), then send player's name into it
		try:
			searchbar = wait_clickable_then_find(searchbar_valid_css, 5)
		except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
			searchbar = wait_clickable_then_find(searchbar_dirty_css, 10)

		searchbar.send_keys(name)

		# check if the more_details_btn is available, if so then load the player's page
		try:
			more_details_btn = wait_clickable_then_find(more_details_css)
			more_details_btn.click()

			# pull all info according to the function
			get_info_from_plyr_page(data)

			# go back to the search for player page
			drv.back()

		# timeout on the More Details btn -- say player couldn't be found and continue
		except selenium.common.exceptions.TimeoutException:
			print("No Player Found - " + str(name))
			missing_player = [name, "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA"]
			data.append(missing_player)
			searchbar.clear()

		# clear the text from the searchbar, whether it is the valid or dirty version
		try:
			wait_clickable_then_find(searchbar_valid_css, 5).clear()
		except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
			wait_clickable_then_find(searchbar_dirty_css, 10).clear()

# create output csv with the data
with open(f'outputs\output_{now}.csv', 'w', newline='') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(
		["Player Name", "Date of Birth", "Event Year", "Event Date", "Event Type", "Location", "Rank", "fivbID",
		 "Nationality"])
	for row in data:
		writer.writerow(row)

os.startfile(f'outputs\output_{now}.csv')
