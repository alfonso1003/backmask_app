# https://superuser.com/questions/421153/how-to-add-a-mp3-handler-to-sox/421168
# https://nhs.io/reverse/
# https://superuser.com/questions/332347/how-can-i-convert-mp4-video-to-mp3-audio-with-ffmpeg/354662

import os

# lame --decode music.mp3 music.wav
# sox -V music.wav backwards.wav reverse
# lame --decode music.mp3 - | sox -V - backwards.wav reverse
# sox -V "|lame --decode music.mp3 -" backwards.wav reverse

def reverse(audio_file):
    if audio_file.endswith('.wav'):
        os.system('sox -V %s backwards.wav reverse' % audio_file )
    else:
        pass
