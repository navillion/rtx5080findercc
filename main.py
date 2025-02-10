import requests
import os
from time import sleep

# Set ? to your desired store pickup location (set it on CC and look at url)
CC_WEBSITE_URL = "https://www.canadacomputers.com/en/search?s=5080&pickup=?"

WEBHOOK_URL = os.environ["WEBHOOK_PERSONAL"] # set your own webhook in env or paste it here

def checkAvailability():
  response = requests.get(CC_WEBSITE_URL)
  return response.text.count("No matches were found for your search") != 2 # this should be 2 if its not available.

def RunAvailabilityChecker():
  print("The Auto Ping system is online.")
  seconds = 0
  while True:
    sleep(1)
    if seconds % 180 == 0:
      if checkAvailability():
        print("The RTX 5080 is available!")
        data = {
          "username" : "RTX 5080 Informer",
          "content" : "Greetings sire. Your desired card is available: https://www.canadacomputers.com/en/search?s=5080&pickup=?"
        }
        requests.post(WEBHOOK_URL, data)

    seconds += 1
