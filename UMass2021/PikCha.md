#PikCha


Once we visit the page we get this:


![PikCha](https://user-images.githubusercontent.com/29373869/112759986-53bf5000-8fed-11eb-9b48-8d97d903cc41.png)


I started looking around and saw something interesting with the cookies :D


![PikCha2](https://user-images.githubusercontent.com/29373869/112760002-5e79e500-8fed-11eb-8c7b-a1f40b304965.png)


I wonder what are those values?!
After googling, I discovered that each of those values represent the ID of one pokemon and if you look at the values,they match the pokemons on the picture!
So I created a python script.

```
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

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get(url)

time.sleep(1) # Let the user actually see something!

rPokemon = requests.get(api)



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



```


FLAG=UMASS{G0tt4_c4tch_th3m_4ll_17263548}
