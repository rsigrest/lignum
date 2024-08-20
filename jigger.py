import time
import json
import sys

def _log(message: str, extra: dict, stream, level: str):
    contents = {'timestamp':int(time.time()), 'message': message, 'level': level} | extra
    stream.write(json.dumps(contents))

def debug(message: str, extra: dict={}, stream=sys.stderr):
    _log(message, extra, stream, 'debug')

def error(message: str, extra: dict={}, stream=sys.stderr):
    _log(message, extra, stream, 'error')

def fatal(message: str, extra: dict={}, stream=sys.stderr):
    _log(message, extra, stream, 'fatal')

def info(message: str, extra: dict={}, stream=sys.stderr):
    _log(message, extra, stream, 'info')

def warn(message: str, extra: dict={}, stream=sys.stderr):
    _log(message, extra, stream, 'warn')

def trace(message: str, extra: dict={}, stream=sys.stderr):
    _log(message, extra, stream, 'trace')
