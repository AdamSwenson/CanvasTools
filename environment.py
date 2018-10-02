"""
Created by adam on 9/14/18
"""
__author__ = 'adam'

import os
import sys
import configparser

############################ Locations  ############################
ROOT = os.getenv( "HOME" )
# The folder containing environment.py
PROJ_BASE = os.path.abspath(os.path.dirname(__file__))
# Folders outside of the project foler
enclosing = os.path.abspath(os.path.dirname(PROJ_BASE))

############### Credentials
# All login credentials are defined in files here.
# THIS CONTENTS OF THIS FOLDER MUST NOT BE COMMITTED TO VERSION CONTROL!
CREDENTIALS_FOLDER_PATH = "%s/private" % PROJ_BASE
CREDENTIALS_FILE = "%s/canvas-credentials.ini" % CREDENTIALS_FOLDER_PATH

print("Reading credentials and settingsfrom %s" % CREDENTIALS_FILE)
config = configparser.ConfigParser()
config.read(CREDENTIALS_FILE)

TOKEN = config['credentials'].get('TOKEN')
URL_BASE = config['url'].get('BASE')

TEMP_DATA_PATH = "%s/temp" % PROJ_BASE
ARCHIVE_FOLDER = "%s/%s" % (ROOT, config['folders'].get('STUDENT_WORK_ARCHIVE_FOLDER'))
DATA_FOLDER = '%s/data' % PROJ_BASE

