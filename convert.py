import os
import subprocess


def convert_mov_to_mp4(input_path, output_path):
    # ffmpeg command to convert without re-encoding (lossless)
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c:v", "copy",  # copy video stream without re-encoding
        "-c:a", "copy",  # copy audio stream without re-encoding
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Conversion done: {output_path}")
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e)


# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Get all .MOV files from input directory
for file in os.listdir("input"):
    if file.lower().endswith('.mov'):
        input_path = os.path.join("input", file)
        output_path = os.path.join(
            "output", os.path.splitext(file)[0] + ".mp4")
        convert_mov_to_mp4(input_path, output_path)
