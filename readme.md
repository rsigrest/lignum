# lignum
A teensy structured JSON logger for python.

## Usage
Install lignum with `pip`:

```bash
pip install lignum
```

Initialize the logger and use the level functions to start logging messages:

```python
import lignum
log = lignum.Logger()
log.info('Application started.') # Prints {"timestamp":1724129120,"message":"Application started.","level":"info"} to STDERR
```

By default, lignum prints to `sys.stderr`. You can use another stream type by specifying it in the
arguments:

```python
import lignum
log = lignum.Logger(sys.stdout)
log.error('The system is down.') # Prints {"timestamp":17241236120,"message":"The system is down.","level":"error"} to STDOUT
```

You can use a `File` as a stream to log to files on disk:

```python
import lignum
with open('log.log','w') as f:
  log = lignum(f)
  log.warn('I will haunt your dreams.') # Prints {"timestamp":17241336120,"message":"I will haunt your dreams.","level":"warn"} to ./log.log
```

Add additional fields using `extra` dictionaries:

```python
import lignum
log = lignum()
log.debug('Unknown value.', { 'value': mystery }) # Prints {"timestamp":1724149120,"message":"Unknown value.","level":"debug","value":-32768} to STDERR
```
