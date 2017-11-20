from queue import Queue
import logging


class Bfs:
    def __init__(self):
        self.queue = Queue()
        self.dictionary = {}

    def is_empty(self):
        if self.queue.empty():
            logging.info('Queue is empty')
            return True
        return False

    def get(self):
        if self.queue.empty():
            logging.error('Attempting to \'get\' on an empty queue')
            return  # TODO: throw a home-made exception here
        queue_top = self.queue.get()
        if queue_top in self.dictionary:
            logging.error('Queue contains items which are already in the dictionary: ' + queue_top)
            logging.info('Skipping this item and going to the next one')
            self.get()
        return queue_top

    def add(self, subject, links):
        if subject in self.dictionary:
            logging.error('The subject ' + subject + ' is already in this dictionary')
            return  # TODO: good place for an exception that we define
        self.dictionary[subject] = links

        for link in links:
            if link not in self.dictionary:
                self.queue.put(link)

    def print_dictionary(self):
        for page in self.dictionary:
            print(page)
            links = self.dictionary[page]

            for i in range(0, len(links)):
                print(links[i] + ', ', end='')

            print('\n')
