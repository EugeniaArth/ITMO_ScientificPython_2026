# Instructions how to convert images to base64 text and back.

#How It Works
Base64 encoding converts binary image data to ASCII text. Each 3 bytes are converted to  4 ASCII characters.
It is safe for text storage/transmission and fully reversible

#Requirements

Python 3.x
No external packages needed


# Usage
There are two python scripts:

## Scripts

| Script | Purpose |
|--------|---------|
| `img2txt.py` | Image  Base64 text |
| `txt2img.py` | Base64 text  Image |

## Example

### Image to Text
```bash
python img2txt.py screenshot.png
# Creates: screenshot.txt

