# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

import os
import sys
import logging
import subprocess

class Logging:
    def __init__(self):
        self.logger = logging.getLogger('python-byzantium')
        if 'BYZ_DEBUG' in os.environ and os.environ['BYZ_DEBUG']:
            self.log_level = logging.DEBUG
        else:
            self.log_level = logging.ERROR
        self.__set_file_logging(self.logger, '/tmp/byantium.log', self.log_level)#const.get('global-log-file'), self.log_level)
        self.__set_stderr_logging(self.logger, self.log_level)
        self.logger.debug('end __init__')

    def __set_file_logging(self, logger, filename, level):
        log_file_handler = logging.FileHandler(filename)
        log_file_handler.setLevel(level)
        logger.addHandler(log_file_handler)

    def __set_stderr_logging(self, logger, level):
        log_stream_handler = logging.StreamHandler(sys.stderr)
        log_stream_handler.setLevel(level)
        logger.addHandler(log_stream_handler)

    def get_logger(self, name=None, level=None, filename=None, new=False):
        self.logger.debug('got logger')
        if not new: return self.logger
        if name:
            logger = logging.getLogger(name)
        else:
            logger = logging.getLogger()
        if not level: level = self.log_level
        logger.setLevel(level)
        if filename: self.__set_file_logging(logger, filename, level)
        return logger
