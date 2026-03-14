import pytest
from usepy.dict import pick, omit, get, deep_merge, map_keys, map_values, invert


class TestPick:
    """Tests for pick() function"""

    def test_pick_existing_keys(self):
        """Test picking existing keys"""
        assert pick({'a': 1, 'b': 2, 'c': 3}, ['a', 'c']) == {'a': 1, 'c': 3}

    def test_pick_non_existing_keys(self):
        """Test picking non-existing keys"""
        assert pick({'a': 1, 'b': 2}, ['x', 'y']) == {}

    def test_pick_mixed_keys(self):
        """Test picking mixed existing and non-existing keys"""
        assert pick({'a': 1, 'b': 2}, ['a', 'x']) == {'a': 1}

    def test_pick_empty_dict(self):
        """Test picking from empty dict"""
        assert pick({}, ['a']) == {}

    def test_pick_empty_keys(self):
        """Test picking with empty keys"""
        assert pick({'a': 1, 'b': 2}, []) == {}


class TestOmit:
    """Tests for omit() function"""

    def test_omit_existing_keys(self):
        """Test omitting existing keys"""
        assert omit({'a': 1, 'b': 2, 'c': 3}, ['b']) == {'a': 1, 'c': 3}

    def test_omit_non_existing_keys(self):
        """Test omitting non-existing keys"""
        assert omit({'a': 1, 'b': 2}, ['x', 'y']) == {'a': 1, 'b': 2}

    def test_omit_all_keys(self):
        """Test omitting all keys"""
        assert omit({'a': 1, 'b': 2}, ['a', 'b']) == {}

    def test_omit_empty_dict(self):
        """Test omitting from empty dict"""
        assert omit({}, ['a']) == {}

    def test_omit_empty_keys(self):
        """Test omitting with empty keys"""
        assert omit({'a': 1, 'b': 2}, []) == {'a': 1, 'b': 2}


class TestGet:
    """Tests for get() function"""

    def test_get_nested_value(self):
        """Test getting nested value with dot path"""
        assert get({'a': {'b': {'c': 1}}}, 'a.b.c') == 1

    def test_get_with_list_path(self):
        """Test getting value with list path"""
        assert get({'a': {'b': {'c': 1}}}, ['a', 'b', 'c']) == 1

    def test_get_non_existing_path(self):
        """Test getting non-existing path returns None"""
        assert get({'a': {'b': 1}}, 'a.x.y') is None

    def test_get_with_default(self):
        """Test getting with default value"""
        assert get({'a': {'b': 1}}, 'a.x.y', default=0) == 0

    def test_get_root_key(self):
        """Test getting root level key"""
        assert get({'a': 1, 'b': 2}, 'a') == 1

    def test_get_empty_path(self):
        """Test getting with empty path"""
        assert get({'a': 1}, '') is None


class TestDeepMerge:
    """Tests for deep_merge() function"""

    def test_deep_merge_nested(self):
        """Test deep merging nested dicts"""
        result = deep_merge({'a': {'b': 1}}, {'a': {'c': 2}})
        assert result == {'a': {'b': 1, 'c': 2}}

    def test_deep_merge_overwrite(self):
        """Test deep merge overwrites non-dict values"""
        assert deep_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 3, 'c': 4}

    def test_deep_merge_empty(self):
        """Test deep merge with empty dict"""
        assert deep_merge({'a': 1}, {}) == {'a': 1}
        assert deep_merge({}, {'a': 1}) == {'a': 1}

    def test_deep_merge_multiple(self):
        """Test deep merge with multiple dicts"""
        result = deep_merge({'a': 1}, {'b': 2}, {'c': 3})
        assert result == {'a': 1, 'b': 2, 'c': 3}

    def test_deep_merge_preserves_original(self):
        """Test deep merge doesn't modify original"""
        original = {'a': {'b': 1}}
        deep_merge(original, {'a': {'c': 2}})
        assert original == {'a': {'b': 1}}


class TestMapKeys:
    """Tests for map_keys() function"""

    def test_map_keys_upper(self):
        """Test mapping keys to uppercase"""
        assert map_keys({'a': 1, 'b': 2}, str.upper) == {'A': 1, 'B': 2}

    def test_map_keys_transform(self):
        """Test transforming keys"""
        assert map_keys({1: 'a', 2: 'b'}, lambda x: x * 2) == {2: 'a', 4: 'b'}

    def test_map_keys_empty(self):
        """Test mapping empty dict"""
        assert map_keys({}, str.upper) == {}


class TestMapValues:
    """Tests for map_values() function"""

    def test_map_values_double(self):
        """Test mapping values to double"""
        assert map_values({'a': 1, 'b': 2}, lambda x: x * 2) == {'a': 2, 'b': 4}

    def test_map_values_upper(self):
        """Test mapping values to uppercase"""
        assert map_values({'a': 'x', 'b': 'y'}, str.upper) == {'a': 'X', 'b': 'Y'}

    def test_map_values_empty(self):
        """Test mapping empty dict"""
        assert map_values({}, lambda x: x) == {}


class TestInvert:
    """Tests for invert() function"""

    def test_invert_simple(self):
        """Test inverting simple dict"""
        assert invert({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}

    def test_invert_duplicate_values(self):
        """Test inverting with duplicate values (last key wins)"""
        assert invert({'a': 1, 'b': 1}) == {1: 'b'}

    def test_invert_empty(self):
        """Test inverting empty dict"""
        assert invert({}) == {}