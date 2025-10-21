# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.1] - 2025-10-21

### Changed
- **BREAKING (minor)**: Replaced all `print()` statements with proper `logging` calls
  - Users who relied on print output will need to configure Python logging
  - See README.md for logging configuration examples
  
### Added
- Proper logging infrastructure using Python's standard `logging` module
- Module-level loggers in `authentication.py`, `account_management.py`, `trading.py`
- Comprehensive logging documentation in README.md and LOGGING_DOCS.md
- Appropriate log levels: DEBUG for diagnostics, INFO for operations, WARNING for issues, ERROR for failures

### Fixed
- Token refresh messages now use DEBUG level instead of printing to stdout
- Rate limit messages now use WARNING level with cleaner formatting
- Service unavailability messages now use WARNING level
- Error messages properly categorized by severity
- Progress indicators suppressed (were causing log spam)

### Improved
- Better integration with application logging infrastructure
- Users can now control log verbosity per module
- Production deployments can suppress all library logs
- Debugging is easier with granular log level control

## [0.4.0] - 2024-XX-XX

### Added
- Initial release with basic functionality
- Support for market data, account management, and trading operations
- Environment switching between test and production
- Comprehensive API coverage for Deribit endpoints
