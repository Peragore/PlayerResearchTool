#!/usr/bin/env python

import sc2reader
from sc2reader.factories.plugins.replay import toJSON
import ReplayToJson

def main():
   replay = ReplayToJson.replay_to_json('C:/Users/pmulford/Documents/Replays/Test.SC2Replay')
   print(replay)


if __name__ == "__main__":
    main()
