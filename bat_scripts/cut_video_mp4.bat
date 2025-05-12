@echo off

:: Путь к исходному видео
set "input_video=../input.mp4"

:: Путь к выходной папке
set "output_folder=../clips"

:: Создать папку, если её нет
if not exist "%output_folder%" mkdir "%output_folder%"

:: Вырезать с 1:00 до 2:00 (1 минута)
ffmpeg -ss 00:01:00 -to 00:02:00 -i "%input_video%" -c copy "%output_folder%/clip_01.mp4" -y

:: Вырезать с 11:00 до 12:00
ffmpeg -ss 00:11:00 -to 00:12:00 -i "%input_video%" -c copy "%output_folder%/clip_02.mp4" -y

:: Вырезать с 21:00 до 22:00
ffmpeg -ss 00:21:00 -to 00:22:00 -i "%input_video%" -c copy "%output_folder%/clip_03.mp4" -y

:: Вырезать с 31:00 до 32:00
ffmpeg -ss 00:31:00 -to 00:32:00 -i "%input_video%" -c copy "%output_folder%/clip_04.mp4" -y

:: Вырезать с 41:00 до 42:00
ffmpeg -ss 00:41:00 -to 00:42:00 -i "%input_video%" -c copy "%output_folder%/clip_05.mp4" -y

echo Нарезка завершена!
pause