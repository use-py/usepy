import pytest

from usepy import useSnowflakeId
from usepy.core.useSnowflakeId import _generate_timestamp


def test_snowflake_id_generation():
    generator = useSnowflakeId(1, 2)

    # Generate multiple IDs and ensure they are unique
    ids = set()
    for _ in range(1000):
        new_id = generator.generate_id()
        assert new_id not in ids
        ids.add(new_id)

    # Manually set the timestamp to a past value and ensure an error is raised
    generator.last_timestamp = _generate_timestamp() + 1000
    with pytest.raises(ValueError):
        generator.generate_id()
