import requests


def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    return data


def get_news():
    url = 'https://gnews.io/api/v4/top-headlines?token=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    return data


def get_music(song):
    url = f'https://api.music.com/songs?title={song}&apikey=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    return data


def control_home(device, action):
    url = f'https://api.alexa.com/devices/{device}/control?action={action}&apikey=YOUR_API_KEY'
    response = requests.post(url)
    data = response.json()
    return data


def get_calendar_events():
    url = 'https://api.google.com/calendar/events?apikey=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    return data


def get_emails():
    url = 'https://api.google.com/gmail/emails?apikey=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    return data