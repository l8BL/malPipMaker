import time
import sys

def standardFunction():
          pass

def __getattr__(name):
          pass
          return standardFunction

def catch_exception(exc_type, exc_value, tb):
      while True:
          time.sleep(1000)

sys.excepthook = catch_exception