# Copyright 2021 Ash Hellwig <ash@ashwigltd.com> (https://ash.ashwigltd.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from bs4 import BeautifulSoup
import requests


class BargenInstance(object):
    """Configuration for source of what is used to generate the lyrics.

    Args:
        object (dict): Configuration object consisting of information
        required to generate the lyrics.
    """
    def __init__(self, artistname):
        self._artist = artistname.replace(' ', '-')
        self._url_artist = 'https://genius.com/artists/' + self._artist.replace(
            ' ', '-')
        self._html_artist = self.set_html_artist()
        self._url_songs = self.set_songs_url()
        self._html_songs = self.set_songs_html()

    @property
    def artistname(self):
        """Artist to scrape from lyric database.

        Returns:
            str: Name of the artist to use as model for lyric generation.
        """
        return self._artist

    @property
    def url_artist(self):
        """Artist URL to scrape from lyric database.

        Returns:
            str: URl of the artist to use as model for lyric generation.
        """
        return self._url_artist

    def set_html_artist(self):
        # ---- Get List of Songs from Artist Page ----
        artistpage_page = requests.get(self._url_artist)
        artistpage_soup = BeautifulSoup(artistpage_page.content, 'html.parser')
        artistpage_results = artistpage_soup.find_all(
            'div', class_='mini_card_grid-song')

        return artistpage_results

    def set_songs_url(self):
        artistpage_songcard = []
        for card in self._html_artist:
            for link in card.find_all('a'):
                artistpage_songcard.append(link['href'])

        return artistpage_songcard

    def set_songs_html(self):
        songpage_lyrics = []
        for song in self._url_songs:
            songlink_page = requests.get(song)
            songlink_soup = BeautifulSoup(songlink_page.content, 'html.parser')
            songlink_results = songlink_soup.find_all('div',
                                                      class_='lyrics-root')
            for i in songlink_results:
                songpage_lyrics.append(i)

        return songpage_lyrics

    def printconfig(self):
        print('==============================================')

        # ---- Log Artist Name ----
        # print('----------------------------------------------')
        # print('Artist Name:')
        # print('----------------------------------------------')
        # print(self._artist.replace('-', ' '))
        # print('----------------------------------------------')

        # ---- Log Artist URL ----
        # print('----------------------------------------------')
        # print('Artist URL:')
        # print('----------------------------------------------')
        # print(self._url_artist)
        # print('----------------------------------------------')

        # ---- Log Artist HTML ----
        # print('----------------------------------------------')
        # print('Artist Page HTML:')
        # print('----------------------------------------------')
        # print(self._html_artist)
        # print('----------------------------------------------')

        # ---- Log Song Links ----
        print('----------------------------------------------')
        print('Song Links:')
        print('----------------------------------------------')
        for i in self._url_songs:
            print(i)
        print('----------------------------------------------')
        print('==============================================')
