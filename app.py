import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown(''' Don't take the fck taxi, take the bus''')



'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_date=st.date_input(label='select the time of your ride ')
pickup_time=st.time_input(label='select the time of your ride ')
pickup_longitude = st.number_input(label='pickup longitude')
pickup_latitude =st.number_input(label='pickup latitude')
dropoff_longitude = st.number_input(label='dropoff longitude')
dropoff_latitude = st.number_input(label='dropoff latitude')
passenger_count = st.number_input(label='nb of passengers')
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

   parameters={'pickup_datetime': str(pickup_date) + " " + str(pickup_time),
        'pickup_longitude':pickup_longitude,
        'pickup_latitude':pickup_latitude,
        'dropoff_longitude':dropoff_longitude,
        'dropoff_latitude':dropoff_latitude,
        'passenger_count':int(passenger_count)}

   response = requests.get(url,params=parameters).json()

   st.write('Here is the price:')
   st.json(response)


'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
