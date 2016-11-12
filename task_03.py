#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):

    def __init__(self, logfilename): #Creates customlogger
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None): # logs changes
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self): #Looks for errors and handles them
        handled = []

        try:

            fhandler = open(self.logfilename, 'a')
        except IOError:
            self.log('Unable to open logfile.')
            raise IOError
        for index, entry in enumerate(self.msgs):
            try:
                fhandler.write(str(entry) + '\n')
                handled.append(index)
            except IOError:
                self.log('Unable to write logfile')
                handled.append('Error')
                break

        fhandler.close()

        for index in handled[::-1]:
            if handled[::-1] is 'Error':
                pass
            else:
                del self.msgs[index]
