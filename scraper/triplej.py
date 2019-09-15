import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Timeout for loading additional components on page
WEBDRIVER_WAIT_TIMEOUT_S = 15
PAGE_LOAD_TIMEOUT_S = 5


class TripleJ:
    def scrape(url):
        '''
        Scrape the most played list page from tripleJ website to get full playlist as an array
        '''
        playlist = []
        # Initialize driver
        driver = webdriver.Chrome()
        # Wait to load additional generated elements
        driver.implicitly_wait(WEBDRIVER_WAIT_TIMEOUT_S)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT_S)
        driver.get(url)
        # Leave time for JS to generate additional elements (webdriver not enough)
        time.sleep(1)
        page_playlist = WebDriverWait(driver, WEBDRIVER_WAIT_TIMEOUT_S).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#most-played-list5 > ul > li"))
        )
        for song in page_playlist:
            title = song.find_element_by_css_selector(
                "div.info > div.title").text
            artist = song.find_element_by_css_selector(
                "div.info > div.artist").text
            release = song.find_element_by_css_selector(
                "div.info > div.release").text
            playlist.append(
                {'title': title, 'artist': artist, 'release': release})

        return playlist


if __name__ == "__main__":
    url = 'https://www.abc.net.au/triplej/featured-music/most-played/'
    playlist = TripleJ.scrape(url)
    print(playlist)
