import pytest
import uuid
from usepy.converter import to_int, to_float, to_json, from_json, to_uuid


class TestToInt:
    """Tests for to_int() function"""

    def test_to_int_string(self):
        """Test converting string to int"""
        assert to_int('123') == 123
        assert to_int('-456') == -456

    def test_to_int_float(self):
        """Test converting float to int"""
        assert to_int(45.67) == 45
        assert to_int(-78.9) == -78

    def test_to_int_invalid_string(self):
        """Test converting invalid string returns default"""
        assert to_int('abc', default=0) == 0
        assert to_int('not a number') is None

    def test_to_int_none(self):
        """Test converting None returns default"""
        assert to_int(None) is None
        assert to_int(None, default=0) == 0

    def test_to_int_already_int(self):
        """Test converting int returns same value"""
        assert to_int(123) == 123


class TestToFloat:
    """Tests for to_float() function"""

    def test_to_float_string(self):
        """Test converting string to float"""
        assert to_float('123.45') == 123.45
        assert to_float('-67.89') == -67.89

    def test_to_float_int(self):
        """Test converting int to float"""
        assert to_float(123) == 123.0

    def test_to_float_invalid_string(self):
        """Test converting invalid string returns default"""
        assert to_float('abc', default=0.0) == 0.0
        assert to_float('not a number') is None

    def test_to_float_none(self):
        """Test converting None returns default"""
        assert to_float(None) is None
        assert to_float(None, default=0.0) == 0.0

    def test_to_float_already_float(self):
        """Test converting float returns same value"""
        assert to_float(123.45) == 123.45


class TestToJson:
    """Tests for to_json() function"""

    def test_to_json_dict(self):
        """Test converting dict to JSON"""
        result = to_json({'a': 1, 'b': 2})
        assert result == '{"a": 1, "b": 2}'

    def test_to_json_list(self):
        """Test converting list to JSON"""
        result = to_json([1, 2, 3])
        assert result == '[1, 2, 3]'

    def test_to_json_unicode(self):
        """Test converting dict with unicode"""
        result = to_json({'name': '张三'}, ensure_ascii=False)
        assert result == '{"name": "张三"}'

    def test_to_json_indent(self):
        """Test converting with indentation"""
        result = to_json({'a': 1}, indent=2)
        assert '{\n  "a": 1\n}' == result

    def test_to_json_string(self):
        """Test converting string to JSON"""
        result = to_json('hello')
        assert result == '"hello"'


class TestFromJson:
    """Tests for from_json() function"""

    def test_from_json_dict(self):
        """Test parsing JSON dict"""
        result = from_json('{"a": 1, "b": 2}')
        assert result == {'a': 1, 'b': 2}

    def test_from_json_list(self):
        """Test parsing JSON list"""
        result = from_json('[1, 2, 3]')
        assert result == [1, 2, 3]

    def test_from_json_invalid(self):
        """Test parsing invalid JSON returns default"""
        result = from_json('invalid json', default={})
        assert result == {}

    def test_from_json_none(self):
        """Test parsing None returns default"""
        result = from_json(None, default=[])
        assert result == []

    def test_from_json_unicode(self):
        """Test parsing JSON with unicode"""
        result = from_json('{"name": "张三"}')
        assert result == {'name': '张三'}


class TestToUuid:
    """Tests for to_uuid() function"""

    def test_to_uuid_v4(self):
        """Test generating UUID v4"""
        result = to_uuid()
        assert len(result) == 36
        # Validate it's a valid UUID
        uuid.UUID(result)

    def test_to_uuid_v1(self):
        """Test generating UUID v1"""
        result = to_uuid(version=1)
        assert len(result) == 36
        uuid.UUID(result)

    def test_to_uuid_v3(self):
        """Test generating UUID v3"""
        result = to_uuid(version=3, namespace=uuid.NAMESPACE_DNS, name='example.com')
        assert len(result) == 36
        # UUID v3 is deterministic
        result2 = to_uuid(version=3, namespace=uuid.NAMESPACE_DNS, name='example.com')
        assert result == result2

    def test_to_uuid_v5(self):
        """Test generating UUID v5"""
        result = to_uuid(version=5, namespace=uuid.NAMESPACE_DNS, name='example.com')
        assert len(result) == 36
        # UUID v5 is deterministic
        result2 = to_uuid(version=5, namespace=uuid.NAMESPACE_DNS, name='example.com')
        assert result == result2

    def test_to_uuid_v3_missing_params(self):
        """Test UUID v3 without namespace/name raises error"""
        with pytest.raises(ValueError):
            to_uuid(version=3)

    def test_to_uuid_invalid_version(self):
        """Test invalid version raises error"""
        with pytest.raises(ValueError):
            to_uuid(version=6)