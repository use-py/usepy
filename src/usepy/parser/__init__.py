from .curl import CURL as useCURL
from .url import URL as useURL


class Parser:
    curl = useCURL
    url = useURL


useParser = Parser
