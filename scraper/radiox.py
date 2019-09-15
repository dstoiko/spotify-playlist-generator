from requests_html import HTMLSession


class RadioX:
    def scrape(url):
        '''
        Scrape the playlist page from radioX to get the full playlist as an array
        '''
        session = HTMLSession()
        page = session.get(url)
        sel = 'div.song_wrapper > div.song__text-content > h3 > span'
        tracks = page.html.find(sel)
        playlist = []
        i = 0
        while i < len(tracks):
            playlist.append(
                {'title': tracks[i].text, 'artist': tracks[i+1].text})
            i += 2
        return playlist


if __name__ == "__main__":
    url = 'https://www.radiox.co.uk/radio/playlist/'
    playlist = RadioX.scrape(url)
    print(playlist)
