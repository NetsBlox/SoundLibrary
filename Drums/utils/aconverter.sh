for f in *.wav; do ffmpeg -i $f -vn -ar 44100 -ac 2 -b:a 192k cd Claps/$f.mp3; done
rename 's/\.mp3\z//' *
rename 's/\.wav\z//' *
rename s/$/.mp3/ *    