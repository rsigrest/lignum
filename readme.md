# lignum
A teensy structured JSON logger for python.

## Getting Started
Install lignum:
```bash
pip install lignum
```
Import and use:
```python
import lignum as log
log.info('test') # {"timestamp": 1724129120, "message": "test", "level": "info"}
```
Change streams:
```python
import lignum as log
import sys
log.info('test',stream=sys.stdout)
```
Log to a file:
```python
import lignum as log
with open('log.log','w',encoding='utf-8') as f:
  log.info('test',stream=f) 
```
