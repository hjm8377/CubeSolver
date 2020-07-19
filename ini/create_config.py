from configparser import ConfigParser
import os


def run():
    config = ConfigParser()
    config['settings'] = {
        'rotation_speed': '50',
        'language': 'English'
    }
    try:
        with open('setting.ini', 'w') as f:
            config.write(f)
    except FileNotFoundError:
        os.mkdir('')
        with open('setting.ini', 'w') as f:
            config.write(f)
