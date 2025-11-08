# Python Decorators Project

This folder contains Python scripts that demonstrate the use of decorators to enhance database operations such as logging, connection handling, transaction management, retries, and caching.

## Tasks

### 0. Log Queries
- Decorator `log_queries` logs SQL queries before execution.

### 1. Handle DB Connections
- Decorator `with_db_connection` manages opening and closing connections.

### 2. Transaction Management
- Decorator `transactional` wraps operations in commit/rollback logic.

### 3. Retry on Failure
- Decorator `retry_on_failure` retries failed DB operations.

### 4. Cache Queries
- Decorator `cache_query` caches query results to avoid redundant calls.
