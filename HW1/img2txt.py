import base64
import sys

if len(sys.argv) != 2:
    print("Running")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.rsplit('.', 1)[0] + ".txt"

# read png & encode to base64
with open(input_file, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# save to txt
with open(output_file, "w") as text_file:
    text_file.write(encoded_string)

print(f"Saved: {output_file}")
