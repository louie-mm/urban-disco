import wikipedia
from wikipedia.exceptions import DisambiguationError
import logging
from threading import Thread


def setup(bfs, origin_page):
    current_page = wikipedia.page(origin_page)
    links = current_page.links
    bfs.add(origin_page, links)


def do_search_threads(bfs, max_iterations, number_of_threads):
    thread_list = []
    for i in range(number_of_threads):
        thread = Thread(target=do_search, args=(bfs, max_iterations,))
        thread.setDaemon(True)
        thread_list.append(thread)
    return thread_list


def do_search(bfs, max_iterations):
    iteration = 0
    while not bfs.is_empty() and iteration < max_iterations:
        current_subject = bfs.get()

        try:
            current_page = wikipedia.page(current_subject)
            logging.info('Getting new page: ' + current_subject)
        except DisambiguationError:
            continue

        links = current_page.links
        bfs.add(current_subject, links)
        iteration += 1