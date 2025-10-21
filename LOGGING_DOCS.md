# Logging Configuration

## Adding to README.md

Add this section after the "Configuration" section:

---

## Logging

The `deribit-wrapper` library uses Python's standard `logging` module for all output. This gives you complete control over log levels, formats, and destinations.

### Default Behavior

By default, the library will not output any logs unless you configure a logging handler. This prevents unwanted output in production environments.

### Basic Logging Setup

To see logs from the library, configure Python's logging module:

```python
import logging
from deribit_wrapper import DeribitClient

# Basic configuration - logs to console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

# Create client - you'll now see INFO level logs and above
client = DeribitClient(client_id='your_id', client_secret='your_secret')
```

### Advanced Logging Configuration

For more control, configure specific loggers:

```python
import logging

# Configure the root logger
logging.basicConfig(level=logging.WARNING)

# Configure deribit_wrapper to be more verbose
logging.getLogger('deribit_wrapper').setLevel(logging.INFO)

# Or configure specific modules
logging.getLogger('deribit_wrapper.authentication').setLevel(logging.DEBUG)
logging.getLogger('deribit_wrapper.trading').setLevel(logging.INFO)

# Suppress noisy libraries
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)
```

### Log Levels Used

The library uses these log levels appropriately:

- **DEBUG**: Detailed information for diagnosing issues (e.g., token refresh attempts)
- **INFO**: Confirmation that things are working as expected (e.g., order execution, retries)
- **WARNING**: Something unexpected happened, but the library is handling it (e.g., rate limits, temporary service issues)
- **ERROR**: A serious problem occurred that prevented an operation (e.g., invalid parameters, authentication failure)

### Logging to File

To log to a file instead of console:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('deribit_trading.log'),
        logging.StreamHandler()  # Also log to console
    ]
)
```

### Production Best Practices

For production deployments:

```python
import logging
from logging.handlers import RotatingFileHandler

# Create rotating log file handler
handler = RotatingFileHandler(
    'deribit_wrapper.log',
    maxBytes=10_000_000,  # 10MB
    backupCount=5
)
handler.setFormatter(logging.Formatter(
    '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
))

# Configure library to use WARNING level in production
logger = logging.getLogger('deribit_wrapper')
logger.setLevel(logging.WARNING)
logger.addHandler(handler)

# Suppress debug libraries completely
logging.getLogger('urllib3').setLevel(logging.CRITICAL)
logging.getLogger('requests').setLevel(logging.CRITICAL)
```

### Suppressing All Library Logs

If you want complete silence from the library:

```python
import logging

# Disable all logs from deribit_wrapper
logging.getLogger('deribit_wrapper').setLevel(logging.CRITICAL)
```

---

## Changes from Version 0.4.0

**Version 0.4.1** replaces all `print()` statements with proper `logging` calls. This provides:

- **Better control**: Configure log levels per module
- **Cleaner output**: No unwanted messages in production
- **Better integration**: Works with existing logging infrastructure
- **Improved debugging**: Use DEBUG level to see detailed operation flow

If you relied on `print()` statements being visible, you'll need to configure logging as shown above.
