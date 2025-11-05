#!/usr/bin/env python3
"""
Test runner for Python KACTL stress tests.
Discovers and runs all test_*.py files in python/stress-tests/ subdirectories.
"""

import sys
import os
import importlib.util
import traceback
from pathlib import Path
import time

def discover_tests(base_dir):
    """Discover all test_*.py files in the stress-tests directory."""
    test_files = []
    stress_test_dir = Path(base_dir) / "stress-tests"

    if not stress_test_dir.exists():
        print(f"Error: Stress tests directory not found: {stress_test_dir}")
        return []

    for test_file in stress_test_dir.rglob("test_*.py"):
        test_files.append(test_file)

    return sorted(test_files)

def run_test_file(test_file, base_dir):
    """Run a single test file and return the result."""
    test_name = test_file.stem
    category = test_file.parent.name

    try:
        # Add content directory to Python path for imports
        content_dir = base_dir / "content"
        old_path = sys.path[:]

        # Add the content directory and all subdirectories to sys.path
        if str(content_dir) not in sys.path:
            sys.path.insert(0, str(content_dir))

        # Also add the category-specific subdirectories
        for subdir in content_dir.iterdir():
            if subdir.is_dir() and str(subdir) not in sys.path:
                sys.path.insert(0, str(subdir))

        # Load the module
        spec = importlib.util.spec_from_file_location(test_name, test_file)
        if spec is None or spec.loader is None:
            return False, "Failed to load module spec", 0

        module = importlib.util.module_from_spec(spec)

        # Add test file's directory to module's search path
        sys.modules[test_name] = module

        # Execute the module
        start_time = time.time()
        spec.loader.exec_module(module)
        elapsed = time.time() - start_time

        # Restore path
        sys.path = old_path

        return True, "Passed", elapsed

    except AssertionError as e:
        sys.path = old_path
        return False, f"Assertion failed: {str(e)}", 0
    except Exception as e:
        sys.path = old_path
        error_msg = traceback.format_exc()
        return False, f"Error: {type(e).__name__}: {str(e)}\n{error_msg}", 0

def main():
    """Main test runner function."""
    script_dir = Path(__file__).parent

    print("=" * 70)
    print("KACTL Python Stress Test Runner")
    print("=" * 70)
    print()

    # Discover tests
    test_files = discover_tests(script_dir)

    if not test_files:
        print("No test files found!")
        sys.exit(1)

    print(f"Discovered {len(test_files)} test file(s)")
    print()

    # Run tests
    results = []
    passed = 0
    failed = 0

    for test_file in test_files:
        test_name = test_file.stem
        category = test_file.parent.name
        rel_path = test_file.relative_to(script_dir)

        print(f"Running {category}/{test_name}...", end=" ", flush=True)

        success, message, elapsed = run_test_file(test_file, script_dir)

        if success:
            print(f"✓ PASS ({elapsed:.2f}s)")
            passed += 1
            results.append((test_name, category, True, message, elapsed))
        else:
            print(f"✗ FAIL")
            failed += 1
            results.append((test_name, category, False, message, 0))

    # Print summary
    print()
    print("=" * 70)
    print("Test Summary")
    print("=" * 70)
    print()

    if failed > 0:
        print("Failed tests:")
        print()
        for test_name, category, success, message, _ in results:
            if not success:
                print(f"  {category}/{test_name}:")
                # Print first few lines of error
                lines = message.split('\n')
                for line in lines[:10]:
                    print(f"    {line}")
                if len(lines) > 10:
                    print(f"    ... ({len(lines) - 10} more lines)")
                print()

    print(f"Total: {len(test_files)} tests")
    print(f"Passed: {passed} ({100*passed//len(test_files) if test_files else 0}%)")
    print(f"Failed: {failed}")

    # Calculate total time
    total_time = sum(elapsed for _, _, success, _, elapsed in results if success)
    print(f"Total time: {total_time:.2f}s")

    print()

    if failed == 0:
        print("All tests passed!")
        sys.exit(0)
    else:
        print(f"{failed} test(s) failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
