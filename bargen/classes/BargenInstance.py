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


class BargenInstance(object):
    """Configuration for source of what is used to generate the lyrics.

    Args:
        object (dict): Configuration object consisting of information
        required to generate the lyrics.
    """
    def __init__(self):
        self._artistname = None

    @property
    def artistname(self):
        """Artist to scrape from lyric database.

        Returns:
            str: Name of the artist to use as model for lyric generation.
        """
        return self._artistname

    @artistname.setter
    def artistname(self, value):
        self._artistname = value

    @artistname.deleter
    def artistname(self):
        del self._artistname

    def printInfo(self):
        print('Using artist name: ' + self.artistname)
