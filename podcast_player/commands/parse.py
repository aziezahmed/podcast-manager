"""The parse command. Used to get a specific podcast episode. """

from json import dumps

from .base import Base

from podcast_player.datastore import DataStore

import feedparser

import os
import sys

class Parse(Base):

    def run(self):
        dataStore = DataStore()
        podcast_urls = dataStore.get_podcast_urls()
        podcast_names = dataStore.get_podcast_names()
        
        for index, name in enumerate(podcast_names):
            print(str(index+1) + " - " + name)
        
        choice = input('Which feed: ')
        
        feed = feedparser.parse(podcast_urls[int(choice)-1]) 
        feed.entries.reverse()
        
        for index, entry in enumerate(feed.entries):
            print(str(index+1) + " - " + entry['title'])
        
        choice = input('Which episode: ')
        url = feed.entries[int(choice)-1]["link"]
        
        os.system("mpv "+ url)
        sys.exit(0)