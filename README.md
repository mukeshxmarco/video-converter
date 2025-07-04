# 🎥 MOV to MP4 Converter (Lossless)

This Python script converts all `.mov` video files from the `input/` folder to `.mp4` format in the `output/` folder **without any loss of quality**, using `ffmpeg`.

---

## ✨ Features

- 🔁 Batch conversion of `.mov` to `.mp4`
- 💯 No quality loss (streams are copied, not re-encoded)
- 🛠️ Auto-creates `output/` directory if it doesn’t exist
- 🧾 Simple and clean structure

---

## 🔧 Requirements

- Python 3.x
- FFmpeg (must be installed and available in system PATH)

### ✅ Install FFmpeg

#### On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

#### On macOS (using Homebrew):

```bash
brew install ffmpeg
```

#### On Windows:

Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin/` folder to your system’s PATH.

---

## 🚀 How to Use

1. Place all your `.mov` files inside the `input/` folder.
2. Run the script:
   ```bash
   python convert.py
   ```
3. Converted `.mp4` files will be available in the `output/` folder.

---

## 📂 Project Structure

```
project/
├── convert.py
├── input/
│   └── sample.mov
├── output/
```

---

## 🧠 How It Works

```python
ffmpeg -i input.mov -c:v copy -c:a copy output.mp4
```

- `-c:v copy`: Copies the video stream as-is
- `-c:a copy`: Copies the audio stream as-is

This avoids re-encoding, ensuring fast and **lossless** conversion.

---

## 💡 Suggestions for Improvement

- Add support for other formats (e.g., `.avi`, `.mkv`)
- Integrate a progress bar using `tqdm`
- Build a simple GUI using Tkinter or PyQt

---

## 📄 License

This project is open-source and free to use. Contributions are welcome!
# video-converter
