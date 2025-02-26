import xbmcaddon
import xbmcplugin
import xbmcgui
import sys
import urllib.parse
import os

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_ICON = os.path.join(ADDON.getAddonInfo('path'), 'resources', 'media', 'ico.png')

STREAMS = [
    ('https://ilm.stream18.radiohost.de/ilm_iloveradio_mp3-192', 'I LOVE RADIO', 'i_love_radio.png'),
    ('https://ilm.stream18.radiohost.de/ilm_ilove2dance_mp3-192', 'I LOVE 2 DANCE', 'i_love_2_dance.png')
]

def main():
    for url, title, img in STREAMS:
        add_item(url, title, img)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def add_item(url, title, img=''):
    item_url = build_url({'action': 'play', 'url': url})
    li = xbmcgui.ListItem(title)
    li.setInfo('music', {'title': title})
    img_path = os.path.join(ADDON.getAddonInfo('path'), 'resources', 'media', img) if img else ADDON_ICON
    li.setArt({'thumb': img_path, 'icon': img_path})
    li.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=item_url, listitem=li, isFolder=False)

def play():
    params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    stream_url = params.get('url', STREAMS[0][0])
    li = xbmcgui.ListItem(path=stream_url)
    li.setInfo('music', {'title': "Playing Stream"})
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem=li)

def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def router():
    params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    if params:
        if params['action'] == 'play':
            play()
    else:
        main()

if __name__ == '__main__':
    router()
