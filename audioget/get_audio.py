import moviepy.editor

video = moviepy.editor.VideoFileClip(input("Enter video's name + format."))
audio = video.audio
audio.write_audiofile('audio.mp3')
