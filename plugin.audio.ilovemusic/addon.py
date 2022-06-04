#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path').decode('utf-8')
icons_path = os.path.join(addon_path,'resources','senderlogos')
senderliste = os.path.join(addon_path,'resources','senderliste.txt')
xbmcplugin.setContent(handle=int(sys.argv[1]), content='songs')
				
def add_item(url,infolabels,img=''):
    listitem = xbmcgui.ListItem(infolabels['title'])
    listitem.setInfo('audio',infolabels)
    listitem.setArt({ 'thumb': img , 'icon' : img })
    listitem.setProperty('IsPlayable','true')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]),url,listitem)    

datei = open(senderliste,'r')
for zeile in datei:
    sender2 = zeile.split(',')
    add_item(sender2[0],{'title':sender2[1]},os.path.join(icons_path,sender2[2]))

xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True, updateListing=False, cacheToDisc=True)
