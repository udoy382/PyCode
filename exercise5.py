# Python exercise7 solution #78

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    exercise = 20

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drankk Water at")

        if time() - init_eyes > exsecs:
            print("Eye exercise time. Enter 'doneeye' to stop the alarm.")
            musiconloop('water.mp3', 'doneeye')
            init_eyes = time()
            log_now("eyes relex at")

        if time() - init_exercise > exercise:
            print("Exercide time. Enter 'doneex' to stop the alarm.")
            musiconloop('water.mp3', 'doneex')
            init_exercise = time()
            log_now("exercise at")
            break