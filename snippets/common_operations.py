"""
Common Python operations: file reading, JSON loading, parallel processing
"""

import json
import concurrent.futures
from pathlib import Path
from multiprocessing import Pool, cpu_count
import time


# ============================================
# FILE READING
# ============================================

def read_file_basic(filepath):
    """Read entire file as string"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def read_file_lines(filepath):
    """Read file line by line"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def read_file_iterate(filepath):
    """Iterate over file lines (memory efficient for large files)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


def read_file_with_pathlib(filepath):
    """Read file using pathlib (modern approach)"""
    path = Path(filepath)
    content = path.read_text(encoding='utf-8')
    return content


def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def append_to_file(filepath, content):
    """Append content to file"""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content)


# ============================================
# JSON LOADING
# ============================================

def load_json_file(filepath):
    """Load JSON data from file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def load_json_lines(filepath):
    """Load JSON Lines (one JSON object per line)"""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def save_json_file(data, filepath, indent=2):
    """Save data to JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def parse_json_string(json_string):
    """Parse JSON from string"""
    return json.loads(json_string)


def to_json_string(data, indent=2):
    """Convert object to JSON string"""
    return json.dumps(data, indent=indent, ensure_ascii=False)


# ============================================
# PARALLEL PROCESSING
# ============================================

def process_with_threadpool(func, items, max_workers=None):
    """Run function in parallel using ThreadPoolExecutor (I/O bound tasks)"""
    if max_workers is None:
        max_workers = min(32, (cpu_count() or 1) * 4)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(func, items))
    return results


def process_with_processpool(func, items, max_workers=None):
    """Run function in parallel using ProcessPoolExecutor (CPU bound tasks)"""
    if max_workers is None:
        max_workers = cpu_count()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(func, items))
    return results


def process_with_multiprocessing_pool(func, items, processes=None):
    """Run function in parallel using multiprocessing.Pool"""
    if processes is None:
        processes = cpu_count()
    
    with Pool(processes=processes) as pool:
        results = pool.map(func, items)
    return results


def process_async_with_threadpool(func, items, max_workers=None):
    """Run function asynchronously using ThreadPoolExecutor"""
    if max_workers is None:
        max_workers = min(32, (cpu_count() or 1) * 4)
    
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        for item in items:
            future = executor.submit(func, item)
            futures.append(future)
        
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return results


# ============================================
# EXAMPLE USAGE
# ============================================

if __name__ == "__main__":
    # Example: File reading
    print("=== File Reading ===")
    sample_file = Path(__file__).parent / "sample.txt"
    if sample_file.exists():
        content = read_file_basic(sample_file)
        print(f"File content length: {len(content)}")
    
    # Example: JSON operations
    print("\n=== JSON Operations ===")
    sample_data = {"name": "Alice", "age": 30, "skills": ["Python", "Java"]}
    json_str = to_json_string(sample_data)
    print(f"JSON string: {json_str}")
    
    # Example: Parallel processing
    print("\n=== Parallel Processing ===")
    
    def square(x):
        time.sleep(0.1)  # Simulate work
        return x * x
    
    numbers = list(range(1, 11))
    
    # Sequential
    start = time.time()
    sequential_results = [square(x) for x in numbers]
    seq_time = time.time() - start
    
    # Parallel with ThreadPool
    start = time.time()
    parallel_results = process_with_threadpool(square, numbers)
    parallel_time = time.time() - start
    
    print(f"Sequential time: {seq_time:.3f}s")
    print(f"Parallel time: {parallel_time:.3f}s")
    print(f"Speedup: {seq_time/parallel_time:.2f}x")
