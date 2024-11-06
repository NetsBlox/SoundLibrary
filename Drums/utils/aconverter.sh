#!/bin/bash

# Get the current working directory
current_dir=$(pwd)

# Define the output directory within the current working directory
output_dir="$current_dir/OUTPUT"

# Ensure the output directory exists
mkdir -p "$output_dir"

# Convert each .wav file in the current directory to .mp3 and place it in the output directory
for f in "$current_dir"/*.wav; do
    # Check if there are no .wav files
    [ -e "$f" ] || { echo "No .wav files found in $current_dir"; exit 1; }

    # Extract the base filename without extension
    filename=$(basename "$f" .wav)
    
    # Convert the .wav to .mp3 with specified parameters
    ffmpeg -i "$f" -vn -ar 44100 -ac 2 -b:a 192k "$output_dir/${filename}.mp3"
    echo "Converted $f to $output_dir/${filename}.mp3"
done

# Move to the output directory
cd "$output_dir" || exit

# Rename files to remove any .wav or redundant .mp3 extensions
rename 's/\.wav\z//' *.mp3 2>/dev/null
rename 's/\.mp3\.mp3\z/.mp3/' *.mp3 2>/dev/null

echo "All files have been converted and renamed in the $output_dir directory!"
