import requests
import json
import base64
import webbrowser
import time

# response = requests.get(r'https://random.dog/doggos')
#
# print (response.text)
#
# image_string = "data:image/{{ img_format }};base64,{{ encode_image }}"

# import base64
#
# file_format = image_string.split(';')[0].split('/')[1]
# image_data = image_string.split('base64,')[1]
#
# with open("<YOUR_FILE_NAME>" + "." + file_format, "wb") as fh:
#     fh.write(base64.decodebytes(bytes(image_data, "utf-8")))

def doggie():
    f = r"https://random.dog/woof.json"
    page = requests.get(f)
    data = json.loads(page.text)
    webbrowser.open(data["url"])
# doggie()

skaicius = 30

while skaicius > 1:

  doggie()
  time.sleep(7)
  skaicius -= 1

# def doggiee():
#     f = r"https://random.dog/woof.json"
#     page = requests.get(f)
#     print (json.loads(page.text))
#
# doggiee()




