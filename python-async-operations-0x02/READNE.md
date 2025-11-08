# Python Async Operations Project

This folder contains Python scripts that demonstrate advanced techniques using context managers and asynchronous programming with SQLite and aiosqlite.

## Tasks

- `0-databaseconnection.py`: Custom context manager for DB connections
- `1-execute.py`: Reusable query executor with context manager
- `3-concurrent.py`: Concurrent async queries using asyncio.gather()

## Setup

- Requires Python 3.8+
- Install aiosqlite: `pip install aiosqlite`
- Ensure `users.db` exists with a `users` table
