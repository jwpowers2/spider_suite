# this is the controller program for the anet spider suite

import argparse
import os
import shutil
import logging
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
from spiders.python_spider import PythonSpider
from spiders.scientificlinux_spider import ScientificLinuxSpider

# ############################ Arg Parse CLI user input #############################

parser = argparse.ArgumentParser(
        prog="Spider Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('''\
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                    Hello, I am the Spider Suite controller program.

    List available spiders:          python main.py -l

    Example syntax to run spiders:         python main.py ruby

    This means:

        scrape using the ruby spider 

    The Python spider scrapes python.org and Ruby scrapes ruby-lang.org

    '''))

parser.add_argument("-l", "--list_spiders", action="store_true", default=False,
                    help="list the available spiders")

parser.add_argument("choice", nargs='*',
                    help='The name of the spider you want to run: Need the spider list? \
                    python main.py list')

parser.add_argument("-d", "--delete_old_scrape_files", action="store_true",
                    help="delete old scrape files for all input spiders")

parser.add_argument("--debug", help="enable full logging for debug to standard output",
                    action="store_true")

parser.add_argument("--log", help="send logging to log file at /var/log/scrapyDebug",
                    action="store_true")

args = parser.parse_args()

# ################################## Spider Dictionary #######################################

spiderDict = {
    'python': PythonSpider,
    'scientificlinux': ScientificLinuxSpider}

# ####################### Logging Configuration for the entire Project ########################

if (args.log):
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='/var/log/scrapyDebug',
        level=logging.DEBUG
    )

if (args.debug):
    pass
else:
    logging.disable(logging.INFO)

# ######################## List Spiders #######################################################

if (args.list_spiders):
    for spider in spiderDict:
        logging.basicConfig(format='')
        logging.warning('Spider name:\t{}'.format(spider))
    exit()

# #################### File checks and delete old scrape if user dictates ####################

for spider in args.choice:
    spiderClass = spiderDict.get(spider)
    if spiderClass:

        if (args.delete_old_scrape_files):
            if os.path.exists(os.path.join('scrape', spider)):
                shutil.rmtree(os.path.join('scrape', spider))

        if not os.path.exists(os.path.join('scrape', spider)):
            os.makedirs(os.path.join('scrape', spider))

if not args.choice:

    for spider in spiderDict:

        if (args.delete_old_scrape_files):
            if os.path.exists(os.path.join('scrape', spider)):
                shutil.rmtree(os.path.join('scrape', spider))

        if not os.path.exists(os.path.join('scrape', spider)):
            os.makedirs(os.path.join('scrape', spider))

# ## Loop with spider name argument and sending user limit and item input to spider instance ##

process = CrawlerProcess()
for spider in (args.choice or spiderDict.keys()):
    spiderClass = spiderDict.get(spider)
    if spiderClass:
        process.crawl(spiderClass)
process.start()
