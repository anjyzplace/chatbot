# import logging
from textblob import Word
# logging.basicConfig(filename='chatbot.log',level=logging.DEBUG)


s = "It's not safe to go alone. Take this."
if s.find('to') != -1:
    print('This message is safe.')

# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # add formatter to ch
# ch.setFormatter(formatter)

# # add ch to logger
# logger.addHandler(ch)

# logger.info('info message')