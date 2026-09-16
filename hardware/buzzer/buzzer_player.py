#!/usr/bin/env python
#---------------------------------------------------
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org>
#---------------------------------------------------
# 
#		Passive buzzer 			   Pi 
#			VCC ----------------- 3.3V
#			GND ------------------ GND
#			SIG ---------------- Pin Gpio27
#
#		some notes for melodies were taken from:
#		http://www.astlessons.com/pianoforkids1.html
#		http://www.astlessons.com/pianoforkids2.html
#		where you can get more notes
#
#---------------------------------------------------

from time import sleep_ms
from hardware.buzzer.buzzer import buzz, quiet
from hardware.buzzer.songs import SONGS

def play(melody, tempo, pause=0.2, pace=0.8):
    for frequency, beats in zip(melody, tempo):
        note_duration = pace / beats  # Sekunden
        if frequency == 0:
            quiet()
        else:
            buzz(frequency, 1000)
        sleep_ms(int(note_duration * 1000))
        quiet()
        sleep_ms(int(note_duration * pause * 1000))

def play_song(title):
    title = title.lower()
    for song in SONGS:
        if title in song.title.lower():
            print("Spiele:", song.title)
            play(song.melody, song.tempo, song.pause, song.pace)
            quiet()
            return
    print("Song nicht gefunden:", title)

def play_songs(song_names):
    for name in song_names:
        play_song(name)
        sleep_ms(2000)
    quiet()

# Test:
play_songs(["Pink Panther Theme", "Star Wars Theme", "Nokia Tune (Gran Vals)", "The Final Countdown", "Tetris", "Crazy Frog",  "Super Mario Theme", "Super Mario Underworld Theme"])

# tetris ziemlich kurz
# nokia auch kurz, zufällig eins davon zur begrüßung?


# star wars -> wenn man verloren hat
# mario underworld evtl auch wenn verloren


# wenn man 10 geschafft hat -> mario theme
# -> dann gehts ins schwerere lvl, wider von vorne aber die farben kommen sehr viel schneller und kürzer


# crazy frog ist sehr lang -> wenn man sehr weit gekommen ist
# final countdown wenn man  geschafft hat