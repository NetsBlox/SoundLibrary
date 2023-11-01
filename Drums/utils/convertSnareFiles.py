#!/usr/bin/env python

import os
import errno
import uuid


def path_hierarchy(path):
    fileName = os.path.basename(path)
    parts = fileName.split('_')
    # print(parts)
    hierarchy = {}
    if(len(parts) > 2):
        hierarchy = {
            'soundName': fileName.replace('.mp3', ''),
            'packName': parts[0],
            'Instrument': 'SNARE',
            'Path': path,
        }
    
    try:
        hierarchy['drumSoundLibrary'] = [
            path_hierarchy(os.path.join(path, contents))
            for contents in os.listdir(path)
        ]
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise

    return hierarchy

if __name__ == '__main__':
    import json
    import sys

    try:
        directory = sys.argv[1]
    except IndexError:
        directory = "."

    f = open("drumSoundLibrarySnares.json", "a")
    f.write(json.dumps(path_hierarchy(directory), indent=2, sort_keys=True))
    f.close()
    
