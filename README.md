# Instructions how to convert images to base64 text and back.

# How It Works
Base64 encoding converts binary image data to ASCII text. Each 3 bytes are converted to  4 ASCII characters.
It is safe for text storage/transmission and fully reversible

# Requirements

Python 3.x

No external packages needed


# Usage
There are two python scripts:

## Scripts

| Script | Purpose |
|--------|---------|
| `img2txt.py` | Image  to Base64 text |
| `txt2img.py` | Base64 text  to Image |

## Example

### Image to Text
```bash
python img2txt.py screenshot.png
# Saved: screenshot.txt

### Text to Image

```bash
python txt2img.py screenshot.txt
# Restored: screenshot.restored.png
