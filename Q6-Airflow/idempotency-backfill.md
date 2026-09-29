### Idempotency, backfill

Idempotency means how much of the work can be done repeatedly without changing the result. In this case, we should run the same task multiple times and check if it gives the same resule every single time it it run.

Backfill means that we can run the same task multiple times, but only if the data has changed and check if it gives the same result every single time it it run.