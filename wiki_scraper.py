import wikipedia
from wikipedia.exceptions import DisambiguationError
import logging
from bfs import Bfs

logging.basicConfig(level=logging.INFO)

ORIGIN = 'Gandhi'
FINAL_ITERATION = 10

bfs = Bfs()

iteration = 0
current_page = wikipedia.page(ORIGIN)
links = current_page.links
bfs.add(ORIGIN, links)

while not bfs.is_empty() and iteration < FINAL_ITERATION:
    current_subject = bfs.get()

    try:
        current_page = wikipedia.page(current_subject)
        logging.info('Getting new page: ' + current_subject)
    except DisambiguationError:
        continue

    links = current_page.links
    bfs.add(current_subject, links)
    iteration += 1

bfs.print_dictionary()
