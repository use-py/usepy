from usepy import useNotify, useNotifyChannels

notify = useNotify()
notify.add(
    useNotifyChannels.Bark({"token": "jtgTe64kJAtq4iyj6DaepQ"}),
)

notify.publish(content="usepy")
