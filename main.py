# -*- coding: utf-8 -*-
# Module: default
# Author: dreamer
# Created on: 07.10.2018
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
import os
import requests

from urllib import urlencode
from urlparse import parse_qsl


import xbmcgui
import xbmcplugin
import xbmcaddon

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
#        stream: 'MAGIC WAVES',
        'url': 'show/mw/',
        'image':  'magicwaves.png',
        'channel': 'Magic Waves',
    },
    'shipwrec': {
#        stream: 'SHIPWREC',
        'url': 'show/shipwrec/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Shipwrec',
    },
    'vunk': {
#        stream: 'VUNK',
        'url': 'live/vunk/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Vunk',
    },
    'submit': {
#        stream: 'SUBMIT',
        'url': 'show/submit/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Submit',
    },
    'discotto': {
#        stream: 'DISCOTTO',
        'url': 'show/discotto/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Discotto',
    },
    'clone': {
#        stream: 'CLONE',
        'url': 'show/clone/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Clone'
    },
    'zahara': {
#        stream: 'ZAHARA',
        'url': 'show/zahara/',
        'image': 'image_zahara.png',
        'channel': 'Zahara',
    },
    'neon': {
#        stream: 'NEON',
        'url': 'show/neon/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Neon',
    },
    'onderwereld': {
#        stream: 'ONDERWERELD',
        'url': 'show/onderwereld/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Onderwereld',
    },
    'cbstv': {
#        stream: 'CBS TV',
        'url': 'live/cbstv/',
        'image': 'cbstv.jpg',
        'channel': 'CBS TV',
    },
    'prc': {
#        stream: 'INTERGALACTIC TV',
        'url': 'live/smil:tv.smil/',
        'image': 'IFMTVBG2.jpg',
        'channel': 'Intergalactic TV',
    }    
}

def now_videos(streams):
    """
    Create list of available streams
    """
    
    r = requests.get('{}{}'.format(fm, pn))
    print(r.json())

    try:
        nowplay = r.json()
        npvids = nowplay['11']
        print(npvids)
    except requests.ValueError as e:
        npvids = []
        print(e)

    listvids = []

    for key in streams.keys():
        if key in set(npvids):
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
        list_item = xbmcgui.ListItem(label=video['channel'])
        
        if video['image']:
            image = video['image']
            image = '{}{}{}'.format(fm, ip, image)
            print(image)
            list_item.setArt({'thumb': image, 'icon': image, 'fanart': image})
        
        list_item.setProperty('IsPlayable', 'true')

        url = '{}{}{}'.format(tv, video['url'], pl)
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
