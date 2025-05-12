@echo off

:: Путь к видео
set train_video_path=../train.mp4
set validation_video_path=../validation.mp4

:: Папки для train и validation
set train_folder=../selected_images/train
set val_folder=../selected_images/validation

:: Создание папок, если их нет
if not exist "%train_folder%" mkdir "%train_folder%"
if not exist "%val_folder%" mkdir "%val_folder%"

:: Раскадровки видео
ffmpeg -i "%train_video_path%" -vf fps=1/5 "%train_folder%\frame_%%04d.jpg"
ffmpeg -i "%validation_video_path%" -vf fps=1/5 "%val_folder%\frame_%%04d.jpg"