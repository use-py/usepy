from ._datetime import useDateTime
from ._path import usePath
from ._thread import useThread
from .data import (
    useDict,
    useList,
    useString,
    useAdDict
)
from .decorator import (
    useDecorator,
    useSingleton,
    useTimeIt,
    useRunInThread,
    useCatchError,
    useExceptDebug,
    useListify,
    useCachedProperty,
    useRetry
)
from .logger import (
    useLogger,
    useLoggerIntercept,
    useLoggerInterceptUvicorn,
    # default_handler,
    # logstash_handler,
    # JsonFormatter
)
from .parser import (
    useParser,
    useCURL,
    useURL
)
from .utils import (
    useTimer,
    useTimerManager,
    useUserAgent,
    useImport,
    useLazyImport,
    useUniqueId,
    useDataToDict,
    useCookieToDict,
    useHeadersToDict,
    useCleanHtml,
    useBloomFilter,
    useTo,
    useIs
)
from .utils.bloom_filter import BloomFilter as useBloomFilter

try:
    from notify import useNotify, channels as useNotifyChannels
except ImportError:
    raise ModuleNotFoundError(
        "You need install the 'usepy_plugin_notify' module before use 'useNotify'"
    )

__all__ = [
    # data
    'useDict',
    'useList',
    'useString',
    'useAdDict',
    # decorator
    'useDecorator',
    'useSingleton',
    'useTimeIt',
    'useRunInThread',
    'useCatchError',
    'useExceptDebug',
    'useListify',
    'useCachedProperty',
    'useRetry',
    # logger
    'useLogger',
    'useLoggerIntercept',
    'useLoggerInterceptUvicorn',
    # parser
    'useParser',
    'useCURL',
    'useURL',
    # utils
    'useIs',
    'useTo',
    'useTimer',
    'useTimerManager',
    'useUserAgent',
    'useImport',
    'useLazyImport',
    'useUniqueId',
    'useDataToDict',
    'useCookieToDict',
    'useHeadersToDict',
    'useCleanHtml',
    'useBloomFilter',
    'useDateTime',
    'usePath',
    'useThread',

    # plugins
    'useNotify',
    'useNotifyChannels',
]
