# jigger
Dead-simple, zero-dependency, structured JSON logging for python. Named for "the last lumberjack",
[Jigger Johnson](https://en.wikipedia.org/wiki/Jigger_Johnson).

## Getting Started
Install jigger:
```bash
pip install jigger
```
Import and use:
```python
import jigger as log
log.info('test') # {"timestamp": 1724129120, "message": "test", "level": "info"}
```
