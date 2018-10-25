#!/usr/bin/python3
## Find random unlisted videos

import random
import string
import time
from urllib.request import urlopen

out_file = 'urllist.txt'
tries = 100000
delay = 3

fh = open(out_file,'a+')

print("-" * 25)
print("Finding random unlisted videos for {} tries".format(tries))
for x in range(tries):
    ran = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(11)])
    out = "https://youtu.be/{}".format(ran)
    found = 0
    live = 1
    with urlopen(out) as html:
        for line in html:
            line = html.read().decode('utf-8')
            if 'This video is unlisted' in line:
                print("Found in try {} -  {}".format(x,out))
                fh.write(out)
                found = 1
                break
            if 'This video is unavailable' in line:
                live = 0
                break

    if found == 0:
        print("Nothing in try {} - {}".format(x,out))
    if live == 1:
        print("Live video: {}".format(out))
        fh.write("LIVE:{}".format(out))

    time.sleep(delay)
fh.close()

