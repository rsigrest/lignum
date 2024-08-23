# lignum
A teensy structured JSON logger for python.

## Getting Started
Install lignum (Note: this is not yet uploaded to PyPi so you'll have to install it from source):
```bash
pip install lignum
```
Import and log to default stream (`sys.stderr`):
```python
import lignum as log
log.info('test') # {"timestamp": 1724129120, "message": "test", "level": "info"}
```
Change streams to log to `sys.stdout`:
```python
import lignum as log
import sys
log.info('test',stream=sys.stdout)
```
Change streams to log to a file:
```python
import lignum as log
with open('log.log','w',encoding='utf-8') as f:
  log.info('test',stream=f) 
```
