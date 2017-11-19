from queue import Queue
import wikipedia
import logging

ORIGIN = 'Gandhi'
FINAL_ITERATION = 10

bfs_queue = Queue()
link_dictionary = {}

iteration = 0
bfs_queue.put(ORIGIN)
while iteration < FINAL_ITERATION:
    if bfs_queue.empty():
        logging.info('Queue is empty, search is complete.')
        break

    current_subject = bfs_queue.get()

    if current_subject in link_dictionary:
        logging.error('Dictionary already contains ' + current_subject + ', grabbing next item in queue.')
        continue

    current_page = wikipedia.page(current_subject)
    links = current_page.links

    link_dictionary[current_subject] = links

    for link in links:
        if link not in link_dictionary:
            bfs_queue.put(link)

    iteration += 1

for page in link_dictionary:
    print(page)
    links = link_dictionary[page]

    for i in range(0, len(links)):
        print(links[i] + ', ', end='')

    print('\n')
