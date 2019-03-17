#
# System checks
#
# author: Steve Lenz
#
import os
import sys
import yaml
from tools import colors

#
# Declarations
#
configFilePath = './config.yml'

#
# Check environment
#
if os.path.isfile(configFilePath) is False:
    print(colors.text['red'])
    print('Missing configuration file "' + configFilePath + '"!')
    print('Please create file from "config.yml.dist".')
    print(colors.remove)
    sys.exit(1)

#
# Load configuration
#
config = yaml.safe_load(open(configFilePath))

#
# Run commands
#
for groupName, checks in config['systemChecks'].items():

    print(colors.text['blue'] + groupName + colors.remove)

    for cmdTitle, cmd in checks.items():
        print(colors.text['yellow'] + '-> ' + cmdTitle + ' (cmd: ' + cmd + ')' + colors.remove)
        os.system(cmd)
        print('')

print(colors.text['green'] + 'DONE' + colors.remove)
