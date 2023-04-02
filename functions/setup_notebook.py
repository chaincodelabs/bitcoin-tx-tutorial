import configparser
import sys

# Read configuration from config.ini
config = configparser.ConfigParser()
configfile = "config.ini"
config.read_file(open(configfile, encoding="utf8"))

SOURCE_DIRECTORY = config["path"]["SOURCE_DIRECTORY"]

assert not SOURCE_DIRECTORY == '', 'SOURCE_DIRECTORY not configured! Edit config.ini to configure SOURCE_DIRECTORY.'

# Make functional framework scripts available 
sys.path.insert(0, f"{SOURCE_DIRECTORY}/test/functional")

try:
    from test_framework.test_shell import TestShell

    print(f"Source directory configured as {SOURCE_DIRECTORY}")
except ModuleNotFoundError:
    print(f"Error: {SOURCE_DIRECTORY} is not a Bitcoin Core source directory.")
    print(f"Edit config.ini to configure SOURCE_DIRECTORY.")
