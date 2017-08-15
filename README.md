# Gallery Sync

This script generates a [blueimp Gallery](https://github.com/blueimp/Gallery) index.html from a template using the contents of an images directory. Thumbnails will be automatically generated and placed in a directory defined by the script. The template file is simply the standard blueimp index.html with `<script src="js/demo/demo.js"></script>` removed.

## Note

This script uses the python-magic module available from pypi - note that this is distinct from and conflicts with an identically named module that may exist in your package manager. See https://github.com/ahupp/python-magic#name-conflict.

