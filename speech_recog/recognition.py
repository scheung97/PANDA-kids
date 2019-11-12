from redislite import Redis
from constants import *

if __name__ == '__main__':
	r = Redis(REDIS_DB_FILE)