import os
from glob import glob
from types import ModuleType

from usepy.core.useImport import useImport

__all__ = [
    # core
    'useAdDict',
    'useBloomFilter',
    'useCachedProperty',
    'useCatchError',
    'useCleanHtml',
    'useCounter',
    'useDateTime',
    'useDict',
    'useImport',
    'useLazyImport',
    'useIsToken',
    'useIsString',
    'useIsRegexp',
    'useList',
    'useListFilter',
    'useListFlatten',
    'useListDifference',
    'useListEvery',
    'useListSome',
    'useListSort',
    'useListUnique',
    'useListify',
    'usePath',
    'useRandomString',
    'useRandomUUID',
    'useRetry',
    'useRunInThread',
    'useSingleton',
    'useStringMiddle',
    'useStringMiddleBatch',
    'useStringLeft',
    'useStringRight',
    'useStringDecode',
    'useStringEncode',
    'useStringReverse',
    'useThread',
    'useThreadPool',
    'useTimeIt',
    'useTimeout',
    'useTimeoutFn',
    'useTimer',
    'useTimerManager',
    'useToString',
    'useToBytes',
    'useToMD5',
    'useToSHA1',
    'useToCamel',
    'useToSnake',
    'useToBoolean',

    # crawl
    'useCookieToDict',
    'useCURL',
    'useDataToDict',
    'useHeaderToDict',
    'useURL',
    'useUserAgent',

    # utils
    'useFormatSizeof',
    'useFuncName',
]

export_modules = ['core', 'crawl', 'utils']


def find_module_alias():
    _alias = {}
    for module in export_modules:
        path = os.path.join(os.path.dirname(__file__), module)
        for file in glob(os.path.join(path, '*.py')):
            name, _ = os.path.basename(file).split('.')
            _alias[name] = f"usepy.{module}.{name}:{name}"
    return _alias


override_alias = {
    'useAdDict': 'usepy.core.useAddict:useAdDict',
    'useLazyImport': 'usepy.core.useImport:useLazyImport',
    'useIsToken': 'usepy.core.useIs:useIsToken',
    'useIsString': 'usepy.core.useIs:useIsString',
    'useIsRegexp': 'usepy.core.useIs:useIsRegexp',
    'useListFilter': 'usepy.core.useList:useListFilter',
    'useListFlatten': 'usepy.core.useList:useListFlatten',
    'useListDifference': 'usepy.core.useList:useListDifference',
    'useListEvery': 'usepy.core.useList:useListEvery',
    'useListSome': 'usepy.core.useList:useListSome',
    'useListSort': 'usepy.core.useList:useListSort',
    'useListUnique': 'usepy.core.useList:useListUnique',
    'useRandomString': 'usepy.core.useRandom:useRandomString',
    'useRandomUUID': 'usepy.core.useRandom:useRandomUUID',
    'useStringMiddle': 'usepy.core.useString:useStringMiddle',
    'useStringMiddleBatch': 'usepy.core.useString:useStringMiddleBatch',
    'useStringLeft': 'usepy.core.useString:useStringLeft',
    'useStringRight': 'usepy.core.useString:useStringRight',
    'useThreadPool': 'usepy.core.useThread:useThreadPool',
    'useTimeoutFn': 'usepy.core.useTimeout:useTimeoutFn',
    'useTimerManager': 'usepy.core.useTimer:useTimerManager',
    'useToString': 'usepy.core.useTo:useToString',
    'useToBytes': 'usepy.core.useTo:useToBytes',
    'useToMD5': 'usepy.core.useTo:useToMD5',
    'useToSHA1': 'usepy.core.useTo:useToSHA1',
    'useToCamel': 'usepy.core.useTo:useToCamel',
    'useToSnake': 'usepy.core.useTo:useToSnake',
    'useToBoolean': 'usepy.core.useTo:useToBoolean',
}

alias = {
    **find_module_alias(),
    **override_alias,
}


def __getattr__(module_name: str) -> ModuleType:
    if module_name in alias:
        module, function = useImport(alias[module_name])
        if function:
            return function
    else:
        raise ModuleNotFoundError(f"module `{__name__}` has no function `{module_name}`")


def __dir__():
    return __all__
