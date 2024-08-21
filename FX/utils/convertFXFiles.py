#!/usr/bin/env python

import os
import errno
import uuid


def path_hierarchy(path):
    fileName = os.path.basename(path)
    parts = fileName.split('_')
    hierarchy = {}
    if(len(parts) > 1):
        hierarchy = {
            'soundName': fileName.replace('.mp3', ''),
            'Path': path,
        }
    
    try:
        hierarchy['fxSoundLibrary'] = [
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

    f = open("fxSoundLibrary.json", "a")
    f.write(json.dumps(path_hierarchy(directory), indent=2, sort_keys=True))
    f.close()
    
