@echo off

ffprobe -v error -select_streams v:0 -show_entries stream=duration -of csv=p=0 ../input.mp4