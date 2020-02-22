import mido
import sys
if len(sys.argv) < 3:
    file = 'song.mid'
    BPM = int(sys.argv[1])
else:
    file = sys.argv[1]
    BPM = int(sys.argv[2])
mid = mido.MidiFile(file)

for note in mid.play():
    print(note)