# -*- coding: utf-8 -*-

# python data pipeline to file

import os
import gzip
import json
from datetime import datetime


class PythonPipeline(object):

    def process_item(self, item, spider):

        dest_file = os.path.join('scrape', 'python', 'python-{}.json.gz'.format(datetime.utcnow().isoformat()))
        
        with gzip.open(dest_file, 'a') as open_file:
            line = json.dumps(dict(item)) + "\n"
            open_file.write(line)

        return item
