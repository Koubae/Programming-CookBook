Redis
=====

QuickStart
----------

Start Redis:
```bash
make redis-up
```

### Makefile Commands

- `make redis-up` - Start Redis container in detached mode
- `make redis-down` - Stop and remove Redis container
- `make redis-terminal` - Connect to Redis CLI terminal
- `make help` - Show available commands

### Usage

Start Redis:
```bash
make redis-up
```

Connect to Redis CLI:
```bash
make redis-terminal
```

Stop Redis:
```bash
make redis-down
```



Redis Mental Model
------------------



```bash
                    Redis
                      │
        ┌─────────────┼─────────────┐
        │             │             │
     Strings        Hashes        Lists
        │             │             │
     counters        objects        queues
     cache
     tokens
        │
        ├───────────────┐
        │               │
      Sets         Sorted Sets
        │               │
     unique          ranking /
     values          timestamps
```



### Redis AOF Persistence

Normally, Redis keeps data primarily in memory. That makes it very fast, but memory is volatile: if Redis crashes or the machine restarts, RAM contents disappear.
AOF solves that by writing every data-changing command to disk.

The Docker Compose configuration enables **AOF (Append Only File)** persistence with the `--appendonly yes` flag. AOF is a persistence method that logs every write operation received by the server.

**How AOF works:**
- Every write command (SET, LPUSH, SADD, etc.) is appended to the AOF file
- When Redis restarts, it replays all write operations from the AOF file to reconstruct the dataset
- Provides better durability than RDB snapshots with minimal data loss (configurable fsync policy)

**Benefits:**
- Higher durability - can survive crashes with at most 1 second of data loss (default fsync policy)
- More reliable data recovery
- Human-readable log file (can be edited if needed)

**Trade-offs:**
- AOF files are typically larger than RDB snapshots
- May be slightly slower than RDB for the same dataset size
- Redis periodically rewrites the AOF in the background to keep it compact
