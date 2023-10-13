#1 What Amsterdam will receive from tourist tax if the event lasts a week and you will have 30.000 visitors?
#2 Plot the amount of AirBnB locations per neighbourhood.
#3 Which street in Amsterdam has the most AirBnB apartments?
#4 Try to cross reference the data from the AirBnB dataset with the BBGA. Can you figure out if all apartments of AirBnB are designated as housing? Which number of apartments are not rented out all the �me but are also used as normal housing?
#5 How many hotel rooms should be built if Amsterdam wants to accommodate the same number of tourists?
#6 How many different licenses are issued?

#import libraries
import pandas as pd
import os.path
import matplotlib.pyplot as plt
import plotly.express as px
pd.options.plotting.backend = "plotly"


#open files
bnb_csv = os.path.join(os.path.expanduser('~'), 'Downloads', 'listings.csv')
bnb_df = pd.read_csv(bnb_csv)

#q1: tourist tax, as per the Amsterdam Municipality is: hotels: 7% and  €3 per person per night
#holiday rentals, bed & breakfasts and short-stay accommodation: 10% of the turnover and €3 per person per night
#average hotel price in Amsterdam in May is €294 per night, according to https://www.statista.com/statistics/614061/overnight-accommodation-costs-amsterdam-city/
#average airbnb price is €150 per night, according to https://www.statista.com/statistics/643643/average-price-of-airbnbs-in-amsterdam-by-boroughs/#:~:text=As%20of%202018%2C%20the%20average,a%20shared%20room%20per%20rent.
#So, if 30.000 tourists would stay in hotels for 7 nights. the total revenue in tourist tax would be:
price = 294 * 7
seven_percent = price * 0.07 
tourist_tax_hotel = (seven_percent + (3*7))*30000
print (tourist_tax_hotel)
#tourist_tax_hotel = 4.951.800

#If all 30.000 would stay in Airbnb's, the total revenue in tourist tax would be:
price2 = 150 * 7
ten_percent = price2 * 0.10
tourist_tax_airbnb = (ten_percent + (3*7))*30000
print (tourist_tax_airbnb)
#tourist_tax_airbnb = 3.780.000

#q2: Plot the amount of AirBnB locations per neighbourhood.
