import time
from colorama import Fore, Back, Style
from urllib.request import urlopen
import json
from datetime import date




today = date.today()
begin = input("Advice or Case counter?\n")
begin_lower = begin.lower()
if begin_lower == 'advice':
  check = False
elif begin_lower == 'case counter':
  check = True
if check == True:
  html = urlopen("https://api.covid19api.com/summary").read()
  wjdata = json.loads(html)
  print('Total US Cases to date',today,':')
  print(wjdata['Countries'][216]['TotalConfirmed'])
  print('Total US deaths:')
  print(wjdata['Countries'][216]['TotalDeaths'])
elif check == False:
  print(Fore.BLUE + "Hello")
  time.sleep(1.2)
  print(Style.RESET_ALL)
  daynumber = int(input("What is your day number?\n"))

  if daynumber == 1:
    time.sleep(1.2)
    print(Fore.YELLOW + "I will give you advice for each day that you are in isolation")
    time.sleep(3.5)
    print(Fore.RED + "To avoid possibly getting the coronavirus, remember to wash your hands periodically for 20 seconds")

  if daynumber == 2:
    time.sleep(1.2)
    print(Fore.RED + "Avoid touching objects or people if you go out in public. Remember it is always ok to go outside and get exercise. Just be sure and practice social distancing and stay at least 7 ft away from others.")

  if daynumber == 3:
    time.sleep(1.2)
    print(Fore.RED + "Symptoms of coronavirus include coughing, fever or fatigue.")

  if daynumber == 4:
    time.sleep(1.2)
    print(Fore.RED + "Be sure to clean frequently touched surfaces in your home such as tables, countertops, light switches and doorknobs using a regular household detergent and water.")

  if daynumber == 5:
    time.sleep(1.2)
    print(Fore.RED + "People of all ages can be infected by the coronavirus. Older people, and people with pre-existing medical conditions (such as asthma, diabetes and heart disease) appear to be more vulnerable to becoming severely ill with the virus.")

  if daynumber == 6: 
    time.sleep(1.2)
    print(Fore.RED + "After contracting the coronavirus, it is possible you may lose smell or taste.")

  if daynumber == 7:
    time.sleep(1.2)
    print(Fore.RED + "Cover your nose and mouth with a disposable tissue or flexed elbow when you cough or sneeze.")

  if daynumber == 8:
    time.sleep(1.2)
    print(Fore.RED + "If you, or someone you know has tested positive for coronavirus, self-isolate for a minimum of 14 days.")

  if daynumber == 9:
    time.sleep(1.2)
    print(Fore.RED + "Coronavirus can have severe complications, such as pneumonia. Pneumonia occurs if the virus causes infection of one or both lungs. The tiny air sacs inside the lungs can fill with fluid or pus, making it harder to breathe.")

  if daynumber == 10:
    time.sleep(1.2)
    print(Fore.RED + "Antiviral drugs are a common method of treating viruses. These drugs kill or prevent the spread of viruses through cells in the body. However, there are currently no antiviral drugs for treating coronavirus.")

  if daynumber == 11:
    time.sleep(1.2)
    print(Fore.RED + "People at risk of severe illness should seek immediate medical attention for signs of COVID-19. These include sudden cough, high temperature, and shortness of breath.")

  if daynumber == 12:
    time.sleep(1.2)
    print(Fore.RED + "Don’t touch your face. Coronaviruses can live on surfaces you touch for several hours. If they get on your hands and you touch your eyes, nose, or mouth, they can get into your body.")

  if daynumber == 13:
    time.sleep(1.2)
    print(Fore.RED + "If you have gone out in public, do not sleep in the same clothes. Because many people asparate in their sleep, they may be breathing in the virus from their clothes.")

  if daynumber == 14:
    time.sleep(1.2)
    print(Fore.RED + "Choose a room (or rooms) where you can keep someone who’s sick or who’s been exposed separate from the rest of you.")