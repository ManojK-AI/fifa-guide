#!/bin/sh
cd "$(dirname "$0")"
python3 test_replays_play.py $1 > log_play_$1.txt 2>&1
python3 test_replays_play.py $2 > log_play_$2.txt 2>&1
