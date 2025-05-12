@echo off

FOR /F "usebackq delims=" %%i IN (`get_duration_of_video.bat`) DO (
    echo Длина видео: %%i секунд
    set duration=%%i
)
:: from 0 to %duration%
if not exist "../train.mp4" (
    ffmpeg -i ../input.mp4 -t %duration% -c copy ../train.mp4
)
:: from 3651.840000 to end
if not exist "../validation.mp4" (
    ffmpeg -i ../input.mp4 -ss %duration% -c copy ../validation.mp4
)