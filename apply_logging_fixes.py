#!/usr/bin/env python3
"""
Apply logging fixes to deribit-wrapper package.
Replaces all print() statements with appropriate logging calls.
"""

def fix_authentication_py():
    """Fix print statements in authentication.py"""
    with open('deribit_wrapper/authentication.py', 'r') as f:
        content = f.read()
    
    # Replace error handling prints
    content = content.replace(
        "            print(f'Error code {error_code} for request {uri} with params {sanitized_params}.')\n            print(error_data)",
        "            logger.warning(f'Error code {error_code} for request {uri} with params {sanitized_params}.')\n            logger.debug(f'Error data: {error_data}')"
    )
    
    # Replace too many requests print and progress
    content = content.replace(
        "        print(f'Too many requests for URI {uri}. Waiting {seconds_to_hms(wait)}...')\n        for i in range(wait):\n            time.sleep(1)\n            print(f\"Wait {seconds_to_hms(wait - i)}...\", end='\\r', flush=True)\n        print()",
        "        logger.warning(f'Too many requests for URI {uri}. Waiting {seconds_to_hms(wait)}...')\n        for i in range(wait):\n            time.sleep(1)\n            # Progress updates suppressed for cleaner logs"
    )
    
    # Replace invalid token print
    content = content.replace(
        "                print(f'Invalid token. Trying to get a new one. Attempt {i + 1} of {max_attempts}...')",
        "                logger.debug(f'Invalid token detected (attempt {i + 1}/{max_attempts}), refreshing...')"
    )
    
    # Replace temporarily unavailable print
    content = content.replace(
        "            print(f'Temporarily unavailable. Waiting 1 minute [{i + 1}/{max_attempts}]...')",
        "            logger.warning(f'Service temporarily unavailable. Retry {i + 1}/{max_attempts} in 60s...')"
    )
    
    # Replace invalid params print
    content = content.replace(
        "        print(f'Invalid params for request {uri}: param={param}, reason={reason}')",
        "        logger.error(f'Invalid params for request {uri}: param={param}, reason={reason}')"
    )
    
    with open('deribit_wrapper/authentication.py', 'w') as f:
        f.write(content)
    print("✅ Fixed authentication.py")


def fix_account_management_py():
    """Fix print statements in account_management.py"""
    with open('deribit_wrapper/account_management.py', 'r') as f:
        content = f.read()
    
    # Add logging import if not present
    if 'import logging' not in content:
        content = content.replace(
            'import time\nfrom datetime import datetime',
            'import logging\nimport time\nfrom datetime import datetime'
        )
    
    # Add logger instance if not present
    if 'logger = logging.getLogger(__name__)' not in content:
        content = content.replace(
            'from .utilities import DEFAULT_END, DEFAULT_START, MarginModelType, MarketOrderType, from_dt_to_ts, seconds_to_hms\n\n\nclass AccountManagement',
            'from .utilities import DEFAULT_END, DEFAULT_START, MarginModelType, MarketOrderType, from_dt_to_ts, seconds_to_hms\n\n# Create module logger\nlogger = logging.getLogger(__name__)\n\n\nclass AccountManagement'
        )
    
    # Replace waiting message and progress
    content = content.replace(
        '                print(f"Waiting {seconds_to_hms(wait)} before removing subaccount {subaccount_id}.")\n                for i in range(wait):\n                    time.sleep(1)\n                    print(f"Wait {seconds_to_hms(wait - i)}...", end=\'\\r\', flush=True)\n                print()',
        '                logger.info(f"Waiting {seconds_to_hms(wait)} before removing subaccount {subaccount_id}...")\n                for i in range(wait):\n                    time.sleep(1)\n                    # Progress updates suppressed for cleaner logs'
    )
    
    with open('deribit_wrapper/account_management.py', 'w') as f:
        f.write(content)
    print("✅ Fixed account_management.py")


def fix_trading_py():
    """Fix print statements in trading.py"""
    with open('deribit_wrapper/trading.py', 'r') as f:
        content = f.read()
    
    # Add logging import if not present
    if 'import logging' not in content:
        content = content.replace(
            'import time\nfrom datetime import datetime',
            'import logging\nimport time\nfrom datetime import datetime'
        )
    
    # Add logger instance if not present
    if 'logger = logging.getLogger(__name__)' not in content:
        content = content.replace(
            'from .utilities import DEFAULT_END, DEFAULT_START, OrdersType\n\n\nclass Trading',
            'from .utilities import DEFAULT_END, DEFAULT_START, OrdersType\n\n# Create module logger\nlogger = logging.getLogger(__name__)\n\n\nclass Trading'
        )
    
    # Replace not enough funds prints
    content = content.replace(
        "                print('Not enough funds. Already tried as reduce only.')",
        "                logger.warning('Not enough funds. Already tried as reduce only.')"
    )
    content = content.replace(
        "                print('Not enough funds. Attempt as reduce only...')",
        "                logger.info('Not enough funds. Attempting as reduce only...')"
    )
    
    # Replace settlement in progress print
    content = content.replace(
        "                print('Settlement in progress. Waiting 1 second...')",
        "                logger.info('Settlement in progress. Waiting 1 second...')"
    )
    
    # Replace unhandled error code print
    content = content.replace(
        "            print(f'Error code {code} not handled yet.')",
        "            logger.warning(f'Error code {code} not handled yet.')"
    )
    
    with open('deribit_wrapper/trading.py', 'w') as f:
        f.write(content)
    print("✅ Fixed trading.py")


def fix_market_data_py():
    """Fix print statement in market_data.py"""
    with open('deribit_wrapper/market_data.py', 'r') as f:
        content = f.read()
    
    # The logging import should already be there (check first)
    if 'import logging' not in content:
        content = content.replace(
            'from datetime import datetime\n\nimport pandas',
            'from datetime import datetime\nimport logging\n\nimport pandas'
        )
    
    # Replace no data found print
    content = content.replace(
        "            print(status, 'no data found for asset', asset)",
        "            logging.warning(f'{status}: no data found for asset {asset}')"
    )
    
    with open('deribit_wrapper/market_data.py', 'w') as f:
        f.write(content)
    print("✅ Fixed market_data.py")


if __name__ == '__main__':
    print("Applying logging fixes to deribit-wrapper...")
    print()
    
    fix_authentication_py()
    fix_account_management_py()
    fix_trading_py()
    fix_market_data_py()
    
    print()
    print("✅ All fixes applied successfully!")
    print()
    print("Verifying no print() statements remain (except in __main__ blocks)...")
    
    import subprocess
    result = subprocess.run(
        ['grep', '-n', 'print(', 'deribit_wrapper/authentication.py', 
         'deribit_wrapper/account_management.py', 'deribit_wrapper/trading.py', 
         'deribit_wrapper/market_data.py'],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("✅ No print() statements found in main code!")
    else:
        print("⚠️  Found remaining print() statements:")
        print(result.stdout)
