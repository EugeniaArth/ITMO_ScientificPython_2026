import base64
import sys

if len(sys.argv) != 2:
    print("Running")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.rsplit('.', 1)[0] + ".restored.png"

# reading txt txt
with open(input_file, "r") as text_file:
    encoded_string = text_file.read()

# decode & save png
with open(output_file, "wb") as image_file:
    image_file.write(base64.b64decode(encoded_string))

print(f"Восстановлено: {output_file}")
