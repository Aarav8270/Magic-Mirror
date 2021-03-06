from bs4 import BeautifulSoup as bs
import requests

# https://www.thepythoncode.com/article/extract-weather-data-python
file = open("weather.txt", "w")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"


def get_weather_data(url):
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    session.headers["Accept-Language"] = LANGUAGE
    session.headers["Content-Language"] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")

    result = {}
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    result["temp_now"] = soup.find("span", attrs={"id": "wob_tm"}).text
    return result


if __name__ == "__main__":
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    import argparse

    parser = argparse.ArgumentParser(
        description="Quick Script for Extracting Weather data using Google Weather"
    )
    parser.add_argument(
        "region",
        nargs="?",
        help="""Region to get weather for, must be available region.
                                        Default is your current location determined by your IP Address""",
        default="",
    )
    # parse arguments
    args = parser.parse_args()
    region = args.region
    URL += region
    # get data
    data = get_weather_data(URL)
    file.write(f"Currently: {data['weather_now']}\n")
    file.write(f"Temperature now: {data['temp_now']}")
