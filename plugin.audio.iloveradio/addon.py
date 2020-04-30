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
add_item('http://stream01.iloveradio.de/iloveradio2.mp3',{'title':'I Love 2 Dance'})
add_item('https://streams.ilovemusic.de/iloveradio23.mp3',{'title':'I Love Chill Nation'})
add_item('https://streams.ilovemusic.de/iloveradio103.mp3',{'title':'I Love Dance First'})
add_item('https://streams.ilovemusic.de/iloveradio6.mp3',{'title':'I Love Deutschrap Beste'})
add_item('https://streams.ilovemusic.de/iloveradio104.mp3',{'title':'I Love Deutschrap First!'})
add_item('https://streams.ilovemusic.de/iloveradio16.mp3',{'title':'I Love Greatest Hits'})
add_item('https://streams.ilovemusic.de/iloveradio21.mp3',{'title':'I Love Hardstyle'})
add_item('https://streams.ilovemusic.de/iloveradio3.mp3',{'title':'I Love Hip Hop'})
add_item('https://streams.ilovemusic.de/iloveradio109.mp3',{'title':'I Love Hits 2020'})
add_item('https://streams.ilovemusic.de/iloveradio12.mp3',{'title':'I Love Hits History'})
add_item('https://streams.ilovemusic.de/iloveradio22.mp3',{'title':'I Love Mainstage'})
add_item('https://streams.ilovemusic.de/iloveradio5.mp3',{'title':'I Love Mashup'})
add_item('https://streams.ilovemusic.de/iloveradio10.mp3',{'title':'I Love Music and Chill'})



xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True, updateListing=False, cacheToDisc=False)