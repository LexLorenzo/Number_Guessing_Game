import requests

key = '30d4741c779ba94c470ca1f63045390a'
city = input("Enter your city: ")

data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={key}")

if data.json()['cod'] == '404':
    print("The inputted city is not found.")
else:
    weather = data.json()['weather'][0]['main']
    temperature = round(data.json()['main']['temp'])
    feel = round(data.json()['main']['feels_like'])
    humidity = round(data.json()['main']['humidity'])
    while True:
        choice = input("Would you like it to be displayed in Celsius or Fahrenheit? (Type C or F): ")
        if choice.capitalize() == 'F':
            print(
                f"The current weather right now in {city} is {weather} with a temperature of {temperature}°F "
                f"but it feels like "
                f"{feel}°F and a humidity of {humidity}%")
            break
        elif choice.capitalize() == 'C':
            temperature = round((temperature - 32) * 5 / 9)
            feel = round((feel - 32) * 5 / 9)
            print(
                f"The current weather right now in {city} is {weather} with a temperature of {temperature}°C "
                f"but it feels like "
                f"{feel}°C and a humidity of {humidity}%")
            break
        else:
            print("You've inputted an invalid input. Please try again.")
