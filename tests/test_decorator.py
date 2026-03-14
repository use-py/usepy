import pytest
from usepy.decorator import retry, catch_error, singleton, throttle
import time
import asyncio


class TestRetry:
    """Tests for retry decorator"""

    def test_retry_success_after_failures(self):
        """Test retry succeeds after initial failures"""
        count = 0

        @retry(max_attempts=3, retry_interval=0.1)
        def failing_function():
            nonlocal count
            count += 1
            if count < 3:
                raise ValueError("Test error")
            return "Success"

        assert failing_function() == "Success"
        assert count == 3

    def test_retry_max_attempts_exceeded(self):
        """Test retry raises MaxRetryError when max attempts exceeded"""
        from usepy.decorator.retry import MaxRetryError

        @retry(max_attempts=2, retry_interval=0.1)
        def always_failing():
            raise ValueError("Always fails")

        with pytest.raises(MaxRetryError, match="Max retry 2 times"):
            always_failing()

    def test_retry_specific_exceptions(self):
        """Test retry only retries specified exceptions"""
        call_count = 0

        @retry(max_attempts=3, retry_interval=0.1, retry_exceptions=(ValueError,))
        def specific_error():
            nonlocal call_count
            call_count += 1
            raise TypeError("Not a ValueError")

        # TypeError is not in retry_exceptions, should fail immediately
        with pytest.raises(TypeError):
            specific_error()
        assert call_count == 1

    def test_retry_async_function(self):
        """Test retry works with async functions"""
        call_count = 0

        @retry(max_attempts=3, retry_interval=0.1)
        async def async_failing_function():
            nonlocal call_count
            call_count += 1
            if call_count < 2:
                raise ValueError("Async error")
            return "Async Success"

        result = asyncio.run(async_failing_function())
        assert result == "Async Success"
        assert call_count == 2


class TestCatchError:
    """Tests for catch_error decorator"""

    def test_catch_error_returns_default_on_exception(self):
        """Test catch_error returns default value on exception"""

        @catch_error(return_val="Default")
        def error_function():
            raise ValueError("Test error")

        assert error_function() == "Default"

    def test_catch_error_returns_result_on_success(self):
        """Test catch_error returns actual result when no exception"""

        @catch_error(return_val="Default")
        def success_function():
            return "Success"

        assert success_function() == "Success"

    def test_catch_error_default_none(self):
        """Test catch_error returns None by default"""

        @catch_error()
        def error_function():
            raise ValueError("Test error")

        assert error_function() is None


class TestSingleton:
    """Tests for singleton decorator"""

    def test_singleton_returns_same_instance(self):
        """Test singleton returns same instance for multiple calls"""

        @singleton
        class SingletonClass:
            pass

        instance1 = SingletonClass()
        instance2 = SingletonClass()
        assert instance1 is instance2

    def test_singleton_with_init_params(self):
        """Test singleton with initialization parameters"""

        @singleton
        class ConfigClass:
            def __init__(self, value):
                self.value = value

        instance1 = ConfigClass(42)
        instance2 = ConfigClass(99)  # Second call with different param

        assert instance1 is instance2
        # First init value is preserved
        assert instance1.value == 42

    def test_singleton_thread_safety(self):
        """Test singleton is thread-safe"""
        import threading

        @singleton
        class ThreadSafeClass:
            pass

        instances = []

        def create_instance():
            instances.append(ThreadSafeClass())

        threads = [threading.Thread(target=create_instance) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # All instances should be the same
        assert all(inst is instances[0] for inst in instances)


class TestThrottle:
    """Tests for throttle decorator"""

    def test_throttle_limits_calls(self):
        """Test throttle limits function calls within delay period"""
        call_count = 0

        @throttle(delay=0.1)
        def throttled_function():
            nonlocal call_count
            call_count += 1

        throttled_function()
        throttled_function()  # Should be throttled
        time.sleep(0.15)
        throttled_function()  # Should execute

        assert call_count == 2

    def test_throttle_returns_none_for_throttled_call(self):
        """Test throttled call returns None"""

        @throttle(delay=0.5)
        def returns_value():
            return "value"

        result1 = returns_value()
        result2 = returns_value()  # Throttled

        assert result1 == "value"
        assert result2 is None

    def test_throttle_async_function(self):
        """Test throttle works with async functions"""
        call_count = 0

        @throttle(delay=0.1)
        async def async_throttled():
            nonlocal call_count
            call_count += 1
            return "async_result"

        # First call should execute
        result1 = asyncio.run(async_throttled())
        assert result1 == "async_result"
        assert call_count == 1

        # Immediate second call should be throttled
        result2 = asyncio.run(async_throttled())
        assert result2 is None
        assert call_count == 1  # Still 1, not incremented