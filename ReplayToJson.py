import sc2reader
from sc2reader.factories.plugins.replay import toJSON

factory = sc2reader.factories.SC2Factory()
try:
    factory.register_plugin(
        "Replay", toJSON()
    )  # legacy Python
except TypeError:
    factory.register_plugin("Replay", toJSON(indent=None))


def load_single_replay(replay):
    replay_json = factory.load_replay(replay)

    return replay_json


def load_replay_folder(directory):
    replay_json = factory.load_replays(directory)

    return replay_json
