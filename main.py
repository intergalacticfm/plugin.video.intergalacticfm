# -*- coding: utf-8 -*-
# Module: default
# Author: dreamer
# Created on: 07.10.2018
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from os.path import isfile
import requests

from urllib import urlencode
from urlparse import parse_qsl


import xbmcgui
import xbmcplugin
import xbmcaddon
from xbmc import log, LOGNOTICE, LOGERROR

__addonid__ = "plugin.video.intergalacticfm"

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

_addon = xbmcaddon.Addon()


fm = 'https://www.intergalactic.fm/'
tv = 'https://www.intergalactic.tv/'
pn = 'ifm-system/playingnow.json'
pl = 'playlist.m3u8'
ip = 'images/'


streams = {
    'mw': {
        'label': 'Magic Waves',
        'url': 'show/mw/',
        'image':  'magicwaves.png',
        'tagline': '',
        'plot': '',
        'genre': 'electronic music',
    },
    'shipwrec': {
        'label': 'Shipwrec',
        'url': 'show/shipwrec/',
        'image': 'IFMTVBG2.jpg',
        'tagline': '',
        'plot': '',
        'genre': 'electronic music',
    },
    'vunk': {
        'label': 'Vunk',
        'url': 'live/vunk/',
        'image': 'IFMTVBG2.jpg',
        'tagline': '',
        'plot': 'Music straight from the heart is what David Vunk is all about. Known for his label Moustace Records and envigorating dj sets and productions, this weekly stream on Wednesday evening from West Coast\'s Rotterdam aims straight for your heart.',
        'genre': 'electronic music',
    },
    'submit': {
        'label': 'Submit',
        'url': 'show/submit/',
        'image': 'IFMTVBG2.jpg',
        'tagline': '',
        'plot': 'Stream from the Berlin based producer named Gesloten Cirkel. Known to release on the label Murder Capital, you can experience his authentic non-compromising music and visuals created on instruments he monstly build himself.',
        'genre': 'electronic music',
    },
    'discotto': {
        'label': 'Discotto',
        'url': 'show/discotto/',
        'image': 'IFMTVBG2.jpg',
        'tagline': '',
        'plot': 'Discotto is located in London, but his sets are for an international audience. A dj with guts using special edits to creatively build a set from his home studio for all to enjoy.',
        'genre': 'electronic music',
    },
    'clone': {
        'label': 'Clone',
        'url': 'show/clone/',
        'image': 'IFMTVBG2.jpg',
        'tagline': '',
        'plot': 'In-store stream from Clone. This record shop, label and distributor focusses on electro, techno, house, soundtracks, (italo) disco and much more. Located in Rotterdam, the Netherlands, it is a lively part of the West Coast Sound of Holland as the owner is also an active dj and producer himself.',
        'genre': 'electronic music',
    },
    'zahara': {
        'label': 'Zahara',
        'url': 'show/zahara/',
        'image': 'image_zahara.png',
        'tagline': '',
        'plot': 'Live stream from Zahara cocktail bar which is located directly at the beach in Scheveningen, the Netherlands. A frequent location for Intergalactic FM djs and host for many of the IFM\'s infamous top 100. The most West you can go on Holland\'s West Coast.',
        'genre': 'electronic music',
    },
    'neon': {
        'label': 'Neon',
        'url': 'show/neon/',
        'image': 'IFMTVBG2.jpg',
        'tagline': 'Dreams of Neon, Berlin',
        'plot': 'Dreams of Neon transmits from Berlin offering streams from Neon studios and club nights by Lazercat, Naks and the Dreams of Neon residents.',
        'genre': 'electro, acid, italo',
    },
    'onderwereld': {
        'label': 'Onderwereld',
        'url': 'show/onderwereld/',
        'image': 'IFMTVBG2.jpg',
        'tagline': '',
        'plot': '',
        'genre': 'electronic music',
    },
    'cbstv': {
        'label': 'CBS TV',
        'url': 'live/cbstv/',
        'image': 'cbstv.jpg',
        'tagline': 'Nothing Beyond Our Reach',
        'plot': 'Cybernetic Broadcasting System dominates our galaxy for over a decade. This stream is non-commercial, non-conventional and nothing like it can be encountered on any planet. There is no escaping CBS TV.',
        'genre': 'electro, acid, italo, disco',
    },
    'prc': {
        'label': 'Intergalactic TV',
        'url': 'live/smil:tv.smil/',
        'image': 'IFMTVBG2.jpg',
        'tagline': 'No Station Such Dedication',
        'plot': 'This stream is Intergalactic FM\'s TV channel. Delivering a mix of live recordings from the Panama Racing Club, the best B movies and keeping you updated on UFO sighings.',
        'genre': 'electro, acid, italo, B movies',
    }    
}

def now_videos(streams):
    """
    Create list of available streams
    """
    
    r = requests.get('{}{}'.format(fm, pn))
    #log('JSON: ' + r.json(), NOTICE)

    try:
        nowplay = r.json()
        npvids = nowplay['11']
        #log('npvids: ' + npvids, NOTICE)
    except requests.ValueError as e:
        npvids = []
        log('Value error: ' + e, LOGERROR)

    listvids = []

    for key in streams.keys():
        if key in set(npvids):
            listvids.append(streams[key])
        else:
            #pass # Uncomment this line to hide offline streams
            listvids.append(streams[key])
    
    return listvids


def list_videos():
    """
    Create the list of playable streams in the Kodi interface.
    """

    listing = []

    xbmcplugin.setPluginCategory(_handle, 'Intergalactic TV')
    xbmcplugin.setContent(_handle, 'videos')

    videos = now_videos(streams)

    for video in videos:
        list_item = xbmcgui.ListItem(label=video['label'])
        list_item.setInfo(type='video', infoLabels={'genre': video['genre'], 'plot': video['plot'], 'tagline': video['tagline']})

        # see https://kodi.wiki/view/Movie_artwork
        # only poster, fanart and clearlogo is supported/needed
        # at the moment, artwork shipped in plugin has priority, this might change later
        art = {}
        base = xbmc.translatePath('special://home/addons/{}/resources/'.format(__addonid__))
        image = None
        if video['image']:
            image = '{}{}{}'.format(fm, ip, video['image'])
            log('image: ' + image, LOGNOTICE)
            #TODO check if image is available!

        # poster 1000x1500 1:1.5 PNG
        poster = base + video['label'].lower().replace(' ', '_') + '-poster.png'
        #log('poster: ' + poster, LOGNOTICE)
        if isfile(poster):
            art['poster'] = poster
        elif image:
            art['poster'] = image
        else:
            art['poster'] = base + 'poster.png'

        # fanart 1920x1080 16:9 JPG
        fanart = base + video['label'].lower().replace(' ', '_') + '-fanart.jpg'
        #log('fanart: ' + fanart, LOGNOTICE)
        if isfile(fanart):
            art['fanart'] = fanart
        elif image:
            art['fanart'] = image
        else:
            art['fanart'] = base + 'fanart.png'

        # clearlogo 800x310 1:0.388 transparent PNG (is top-left corner overlay)
        clearlogo = base + video['label'].lower().replace(' ', '_') + '-clearlogo.png'
        #log('clearlogo: ' + clearlogo, LOGNOTICE)
        if isfile(clearlogo):
            art['clearlogo'] = clearlogo
        elif image:
            art['clearlogo'] = image
        else:
            art['clearlogo'] = base + 'clearlogo.png'

        # depricated!
        # thumb 640x360 16:9 PNG
        #thumb = base + video['label'].lower().replace(' ', '_') + '-thumb.png'
        #log('thumb: ' + thumb, LOGNOTICE)
        #art['thumb'] = thumb

        list_item.setArt(art)
        list_item.setProperty('IsPlayable', 'true')

        url = '{}{}{}'.format(tv, video['url'], pl)
        log('url: ' + url, LOGNOTICE)
        url = '{}?action=play&video={}'.format(_url, url)
        is_folder = False

        listing.append((url, list_item, is_folder))

    xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.
    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring
    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring[1:]))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos()
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        list_videos()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring

    router(sys.argv[2])
