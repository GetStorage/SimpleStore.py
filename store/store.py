import sys
import requests
import configparser
from os.path import expanduser

url = 'http://api.stor.ag/v1/object'
home = expanduser("~")


def run(key):
    args = sys.argv
    if args[1]:
        new_file = {'file': open(args[1], 'rb')}

        r = requests.post(url, data={'key': key, 'return': 'text'}, files=new_file)
        if r.status_code == 200:
            thing = r.json()

            print 'http://stor.ag/e/' + thing['id']
    else:
        print "stdin isn't currently supported. Coming soon."


def first_run(config):
    key = raw_input('Your Stor.ag/e/ Key: ')

    config.add_section('storage')
    config.set('storage', 'key', key)

    with open(home + '/.storage.ini', 'w+') as configfile:    # save
        config.write(configfile)

    run(key)


def get_key():
    return False


def start():
    config = configparser.ConfigParser()
    config.read(home + '/.storage.ini')

    if not config.has_section('storage'):
        first_run(config)
    else:
        key = config.get('storage', 'key')
        run(key)


start()