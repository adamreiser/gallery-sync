#!/usr/bin/env python3

import os
import logging
import bs4
from PIL import Image
import magic

logging.basicConfig(level=logging.INFO)

# gallery directory - should contain idir and tdir
gdir = '.'

# images directory - add files here
idir = os.path.join(gdir, 'images')

# thumbnails directory - contents will be automatically generated
tdir = os.path.join(gdir, 'thumbnails')

# max thumbnail width/height
tsize = 128

image_fnames = [f for f in os.listdir(idir)
                if os.path.isfile(os.path.join(idir, f))]

with open("index.html.template") as inf:
    soup = bs4.BeautifulSoup(inf.read(), "lxml")

links = soup.find('div', id='links')
m = magic.Magic(mime=True)

for i in image_fnames:
    if not os.path.exists(os.path.join(gdir, 'thumbnails', i)):
        try:
            im = Image.open(os.path.join(idir, i))
        except IOError as e:
            logging.warning("Reading: %s: %s", i, e)
            continue

        logging.debug("Generating thumbnail for %s", i)

        im.thumbnail((tsize, tsize))
        try:
            im.save(os.path.join(tdir, i))
        except IOError as e:
            logging.warning("Saving thumbnail %s: %s", i, e)
            try:
                os.unlink(os.path.join(tdir, i))
            except OSError:
                pass
            continue
    else:
        logging.debug("Thumbnail exists for %s", i)

    logging.debug("Adding link for %s", i)

    new_link = soup.new_tag("a", title=os.path.splitext(i)[0],
                            href="images/{}".format(i))

    new_img = soup.new_tag("img", src="thumbnails/{}".format(i),
                           type=magic.from_file(os.path.join(idir, i),
                                                mime=True), alt=i)

    new_link.append(new_img)
    links.append(new_link)

with open(os.path.join(gdir, 'index.html'), "w") as outf:
    outf.write(soup.prettify(formatter='html'))
