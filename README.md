## Python Generators Project

This folder contains Python scripts that demonstrate advanced generator usage for streaming, batching, and aggregating data from a MySQL database.

Tasks

0. Stream Users
- Generator function `stream_users()` yields rows one by one from `user_data`.

1. Batch Processing
- `stream_users_in_batches(batch_size)` yields batches.
- `batch_processing(batch_size)` filters users over age 25.

 2. Lazy Pagination
- `lazy_pagination(page_size)` simulates paginated data loading.

 4. Average Age
- `stream_user_ages()` yields ages.
- `calculate_average_age()` computes average without loading all data.

Setup
- Requires MySQL and `user_data.csv`
- Run `seed.py` to create and populate the database
Updated on November 9, 2025.
