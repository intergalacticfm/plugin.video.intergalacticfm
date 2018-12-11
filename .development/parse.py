#!/usr/bin/env python3

from json import load
from datetime import datetime
from pprint import pprint

now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

markdown = open('overview.md', 'w')
markdown.write('# Intergalactic FM streams for Kodi plugin\n\n')
markdown.write('Below are the specific texts and images required by Kodi. '
               'Please, try to meet the requirements as close as possible. '
               'Kodi has many different views and we do not know which view '
               'for navigating and playing streams is used by the user. '
               'So using this format as described by Kodi itself gives the '
               'best result for all. '
               'This overview has been automatically generated on {}.\n\n'.format(now))

streams = load(open('../resources/streams.json'))
for key, values in sorted(streams.items()):
    markdown.write('## {} ({})\n\n'.format(values['label'], key))
    markdown.write('**Tagline** (two to five words): *{}*\n\n'.format(values['tagline']))
    markdown.write('**Genre** (one to three genres): *{}*\n\n'.format(values['genre']))
    markdown.write('**Plot** (twenty to thirty words): *{}*\n\n'.format(values['plot']))
    markdown.write('**Poster** (1000 x 1500 PNG, main logo in center):\n')
    markdown.write('![Poster](../resources/{}-poster.png "Poster")\n\n'.format(key))
    markdown.write('**Fanart** (1920 x 1080 JPG, only for background):\n')
    markdown.write('![Fanart](../resources/{}-fanart.jpg "Fanart")\n\n'.format(key))
    markdown.write('**Clear logo** (810 x 310 PNG with transparency):\n')
    markdown.write('![Clear logo]({}-clearlogo.png "Fanart")\n\n'.format(key))

markdown.close()