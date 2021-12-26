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
import click
import requests

from .classes.BargenInstance import BargenInstance


@click.command()
@click.option('-a', '--artist-name', 'artistname')
def cli(artistname):
    # ---- Select Artist ----
    sourceconfig = BargenInstance()
    sourceconfig.artistname = artistname
    click.echo(
        '==============================================================')
    click.echo('Running CLI from scripts/cli.py')
    click.echo('Using config:')
    click.echo(sourceconfig.printconfig())

    # ---- Generate Artist Page Endpoint URL ----
    artistpage_url = 'https://genius.com/artists/' + sourceconfig.artistname
    click.echo('Using artist page URL: ' + artistpage_url)
    click.echo(
        '==============================================================')

    # ---- Get List of Songs from Artist Page ----
    artistpage_page = requests.get(artistpage_url)
    artistpage_soup = BeautifulSoup(artistpage_page.content, 'html.parser')
    artistpage_results = artistpage_soup.find_all('div',
                                                  class_='mini_card_grid-song')

    artistpage_songcard = []
    for card in artistpage_results:
        for link in card.find_all('a'):
            artistpage_songcard.append(link['href'])

    click.echo('Song Links')
    for i in artistpage_songcard:
        print(i)
    click.echo(
        '--------------------------------------------------------------')

    # ---- Get Song Lyrics ----
    songpage_lyrics = []
    for song in artistpage_songcard:
        songlink_page = requests.get(song)
        songlink_soup = BeautifulSoup(songlink_page.content, 'html.parser')
        songlink_results = songlink_soup.find_all('div', class_='lyrics-root')
        for i in songlink_results:
            songpage_lyrics.append(i)

    for i in songpage_lyrics:
        print(i)


if __name__ == '__main__':
    cli()
