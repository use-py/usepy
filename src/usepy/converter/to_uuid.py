import uuid
from typing import Optional


def to_uuid(version: int = 4, namespace: Optional[uuid.UUID] = None, name: Optional[str] = None) -> str:
    """
    Generates a UUID string.

    Args:
        version (int): The UUID version (1, 3, 4, or 5). Defaults to 4.
        namespace (Optional[uuid.UUID]): The namespace for UUID v3 and v5.
        name (Optional[str]): The name for UUID v3 and v5.

    Returns:
        str: The UUID string.

    Examples:
        >>> len(to_uuid())
        36
        >>> to_uuid(version=1)  # UUID v1 based on timestamp
        '...'
        >>> to_uuid(version=3, namespace=uuid.NAMESPACE_DNS, name='example.com')
        '...'
    """
    if version == 1:
        return str(uuid.uuid1())
    elif version == 3:
        if namespace is None or name is None:
            raise ValueError("UUID v3 requires namespace and name")
        return str(uuid.uuid3(namespace, name))
    elif version == 4:
        return str(uuid.uuid4())
    elif version == 5:
        if namespace is None or name is None:
            raise ValueError("UUID v5 requires namespace and name")
        return str(uuid.uuid5(namespace, name))
    else:
        raise ValueError(f"Unsupported UUID version: {version}")