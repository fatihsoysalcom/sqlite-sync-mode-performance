import sqlite3
import time
import os

DB_NAME = "performance_demo.db"
NUM_RECORDS = 10000

def run_benchmark(synchronous_mode):
    # Clean up previous database file if it exists
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Apply the synchronous PRAGMA.
    # This setting controls how aggressively SQLite flushes writes to disk.
    # 'FULL' (default) ensures maximum durability but can be slower.
    # 'OFF' provides the fastest writes but risks data loss on power failure.
    # In a self-managed environment, you have full control over such settings
    # and the underlying OS/filesystem tuning. In managed services like RDS,
    # these low-level controls are often abstracted or limited, impacting
    # extreme performance tuning capabilities.
    cursor.execute(f"PRAGMA synchronous = {synchronous_mode};")
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT);")

    start_time = time.time()
    for i in range(NUM_RECORDS):
        cursor.execute("INSERT INTO data (value) VALUES (?);", (f"test_value_{i}",))
    conn.commit()
    end_time = time.time()

    conn.close()
    return end_time - start_time

print(f"Benchmarking {NUM_RECORDS} inserts...")

# Benchmark with PRAGMA synchronous = FULL (default, highest durability)
time_full = run_benchmark("FULL")
print(f"Time with PRAGMA synchronous = FULL (high durability): {time_full:.4f} seconds")

# Benchmark with PRAGMA synchronous = OFF (lowest durability, fastest)
time_off = run_benchmark("OFF")
print(f"Time with PRAGMA synchronous = OFF (low durability, high speed): {time_off:.4f} seconds")

print("\n--- Analysis ---")
print("This example demonstrates a fundamental trade-off in database performance:")
print("durability vs. speed, controlled by settings like PRAGMA synchronous.")
print("In a self-managed database setup, you have direct control over such low-level")
print("configurations and the underlying operating system/filesystem, allowing for")
print("fine-tuned optimizations. Managed services like Amazon RDS abstract away")
print("much of this control, providing ease of management but potentially limiting")
print("the ability to achieve extreme performance gains through such specific tuning.")
print(f"For this workload, 'OFF' mode was {time_full / time_off:.2f} times faster than 'FULL' mode.")

# Clean up the database file
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
