# -*- coding: utf-8 -*-
"""
    telemundo.subtitles
    ~~~~~~~~~~~~~~~~~~~

    These classes are used to parse subtitle files.

    :copyright: (c) 2012 by Telemundo Digital Media
    :license: MIT, see LICENSE for more details.
"""

from HTMLParser import HTMLParser
from xml.sax import saxutils
from os import path
import re

class parser():
    ''' Subtitle Parser '''
    filename  = None
    subtitles = None
    def __init__(self):
        self.subtitles = []
    def export(self, filename):
        ''' This method returns an array of subtitles '''
        if not path.exists(filename):
            raise ValueError('The file "%s" does not exist.' % filename)
        self.filename = filename
        matches = self.__parse_subtitles()
        for match in matches:
            subtitle = self.__create_subtitle(match)
            if subtitle:
                parser = html_parser()
                parser.feed(subtitle['text'])
                subtitle['text'] = parser.render_output();
                self.subtitles.append(subtitle)
        return self.subtitles
    def __parse_subtitles(self):
        lines = open(self.filename).read().decode('utf-8')
        return re.findall(r'(?P<data>.*?)\r?\n\r?\n', lines, re.MULTILINE + re.DOTALL)
    def __create_subtitle(self, caption):
        lines = caption.splitlines()
        lines.pop(0)
        timecodes = map(lambda x: x.replace(',', '.'), lines.pop(0).split(' --> '))
        return {
            'begin': timecodes[0],
            'end': timecodes[1],
            'text': '\n'.join(lines)
        }

class html_parser(HTMLParser):
    ''' Custom HTML Parser '''
    stack = None
    def __init__(self):
        self.stack = []
        self.reset()
    def handle_data(self, data):
        self.stack.append(saxutils.escape(data))
    def render_output(self):
        return ''.join(self.stack)