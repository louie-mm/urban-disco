import scraper_utils
import logging
from bfs import Bfs

logging.basicConfig(level=logging.INFO)
ORIGIN = 'Gandhi'
NUM_ITERATION = 10
NUM_THREADS = 5

bfs = Bfs()
scraper_utils.setup(bfs, ORIGIN)


thread_list = scraper_utils.do_search_threads(bfs, NUM_ITERATION / NUM_THREADS, NUM_THREADS)
for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

bfs.print_dictionary()
