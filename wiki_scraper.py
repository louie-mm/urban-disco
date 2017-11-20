import wikipedia
import scraper_utils
import logging
from bfs import Bfs

logging.basicConfig(level=logging.INFO)
ORIGIN = 'Gandhi'
FINAL_ITERATION = 10
NUM_THREADS = 1

bfs = Bfs()
scraper_utils.setup(bfs, ORIGIN)


thread_list = scraper_utils.do_search_threads(bfs, FINAL_ITERATION, NUM_THREADS)
for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

bfs.print_dictionary()
