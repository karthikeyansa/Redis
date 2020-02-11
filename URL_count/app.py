from redis import Redis
from rq import Queue
from module import count_words_at_url

q = Queue(connection=Redis())

result = q.enqueue(count_words_at_url, 'https://karthikeyansa.pythonanywhere.com')
