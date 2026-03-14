import pytest
import time
import asyncio
from usepy.decorator import debounce, memoize


class TestDebounce:
    """Tests for debounce decorator"""

    def test_debounce_delays_execution(self):
        """Test that debounce delays execution"""
        results = []

        @debounce(delay=0.1)
        def add_result(value):
            results.append(value)

        add_result(1)
        add_result(2)
        add_result(3)
        
        # Immediately, no results yet
        assert results == []
        
        # Wait for debounce
        time.sleep(0.15)
        assert results == [3]  # Only last call executed

    def test_debounce_multiple_calls(self):
        """Test multiple debounced calls"""
        results = []

        @debounce(delay=0.1)
        def record(value):
            results.append(value)

        record('a')
        time.sleep(0.15)
        assert results == ['a']

        record('b')
        time.sleep(0.15)
        assert results == ['a', 'b']


class TestMemoize:
    """Tests for memoize decorator"""

    def test_memoize_caches_result(self):
        """Test that memoize caches results"""
        call_count = 0

        @memoize
        def expensive(n):
            nonlocal call_count
            call_count += 1
            return n * n

        # First call computes
        result1 = expensive(5)
        assert result1 == 25
        assert call_count == 1

        # Second call uses cache
        result2 = expensive(5)
        assert result2 == 25
        assert call_count == 1  # Not incremented

    def test_memoize_different_args(self):
        """Test memoize with different arguments"""
        call_count = 0

        @memoize
        def compute(n):
            nonlocal call_count
            call_count += 1
            return n * 2

        compute(1)
        compute(2)
        compute(1)  # Cached
        
        assert call_count == 2  # Only 2 computations

    def test_memoize_with_kwargs(self):
        """Test memoize with keyword arguments"""
        call_count = 0

        @memoize
        def greet(name, greeting='Hello'):
            nonlocal call_count
            call_count += 1
            return f"{greeting}, {name}!"

        result1 = greet('World')
        result2 = greet('World')
        result3 = greet('World', greeting='Hi')
        
        assert result1 == "Hello, World!"
        assert result2 == "Hello, World!"
        assert result3 == "Hi, World!"
        assert call_count == 2  # Two different argument sets

    def test_memoize_clear_cache(self):
        """Test clearing memoize cache"""
        call_count = 0

        @memoize
        def compute(n):
            nonlocal call_count
            call_count += 1
            return n

        compute(1)
        compute(1)
        assert call_count == 1

        # Clear cache
        compute.cache_clear()

        compute(1)
        assert call_count == 2  # Recomputed after clear

    def test_memoize_async(self):
        """Test memoize with async function"""
        call_count = 0

        @memoize
        async def async_compute(n):
            nonlocal call_count
            call_count += 1
            return n * n

        result1 = asyncio.run(async_compute(5))
        result2 = asyncio.run(async_compute(5))
        
        assert result1 == 25
        assert result2 == 25
        assert call_count == 1