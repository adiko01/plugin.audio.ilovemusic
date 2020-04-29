#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path').decode('utf-8')
xbmcplugin.setContent(handle=int(sys.argv[1]), content='songs')
				
def add_item(url,infolabels,):
    listitem = xbmcgui.ListItem(infolabels['title'])
    listitem.setInfo('audio',infolabels)
    listitem.setProperty('IsPlayable','true')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]),url,listitem)

add_item('http://stream01.iloveradio.de/iloveradio1.mp3',{'title':'I Love Radio'})
add_item('http://stream01.iloveradio.de/iloveradio2.mp3',{'title':'I Love 2 Dance Radio'})
add_item('https://streams.ilovemusic.de/iloveradio23.mp3',{'title':'I Love Chill Nation'})
add_item('https://streams.ilovemusic.de/iloveradio103.mp3',{'title':'I Love Dance First'})
add_item('https://streams.ilovemusic.de/iloveradio6.mp3',{'title':'I Love Deutschrap Beste'})
add_item('https://streams.ilovemusic.de/iloveradio104.mp3',{'title':'I Love Deutschrap First!'})


xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.getSetting('view-mode'))
xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True, updateListing=False, cacheToDisc=False)