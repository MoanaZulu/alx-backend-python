# Python Decorators Project

This folder contains Python scripts that demonstrate how decorators can be used to enhance database operations in Python. Each task explores a different use case for decorators, including logging, connection management, transactions, retries, and caching.

## Tasks Overview

### 0. Log Queries
- Decorator `log_queries` logs SQL queries before execution.

### 1. Handle DB Connections
- Decorator `with_db_connection` manages opening and closing MySQL connections.

### 2. Transaction Management
- Decorator `transactional` wraps operations in commit/rollback logic.

### 3. Retry on Failure
- Decorator `retry_on_failure` retries failed DB operations up to a set number of times.

### 4. Cache Queries
- Decorator `cache_query` stores query results to avoid redundant database calls.

## Setup Instructions

- Requires MySQL and a populated `user_data` table (see `seed.py` from `python-generators-0x00`)
- All decorators assume access to a valid MySQL connection object
- Logging is done via `print()` for simplicity; can be extended to use Python's `logging` module

## How to Run

Each script can be run independently to test its decorator behavior. Example:

```bash
python3 0-log_queries.py
