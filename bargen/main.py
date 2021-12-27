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

import click

from .classes.BargenInstance import BargenInstance


@click.command()
@click.option('-a', '--artist-name', 'artistname')
def cli(artistname):
    # ---- Select Artist ----
    sourceconfig = BargenInstance(artistname)

    # ---- Output Config ----
    sourceconfig.printconfig()


if __name__ == '__main__':
    cli()
