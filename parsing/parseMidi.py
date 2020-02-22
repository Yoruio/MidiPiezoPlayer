import mido
import sys
from NoteDic import *

if int(sys.argv[1] == 'help'):
    print("COMMANDLINE FORMATTING FOR parseMidi: ")
    print("~~~PROGRAM REQUIRES MIDO LIBRARY TO BE INSTALLED.")
    print("use 'pip install mido' to install mido on your computer.")
    print("USAGE: python parseMidi.py [midi file name] [BPM]")
    print("if [midi file name] is not given, song.mid will be used.")
    exit()

tuplesPerLine = 8
tupleCount = 0

sys.stdout.write("[")


if len(sys.argv) < 3:
    file = 'song.mid'
    BPM = int(sys.argv[1])
else:
    file = sys.argv[1]
    BPM = int(sys.argv[2])
mid = mido.MidiFile(file)
first = True

for msg in mid.play():
    if msg.type == 'note_on' and not first:
        sys.stdout.write(', ')
        if msg.time != 0:
            sys.stdout.write("('r', '" + beats + "'), ")


    if first and msg.type == 'note_on':
        first = False

    if msg.type == 'note_off':
        if tupleCount == 0:
            sys.stdout.write("\n")
        note = noteName[msg.note]
        beats = noteLen[round(msg.time / 60 * BPM, 3)]

        sys.stdout.write("('" + note + "', '" + beats + "')")

        tupleCount = (tupleCount + 1) % tuplesPerLine


sys.stdout.write("\n]")
