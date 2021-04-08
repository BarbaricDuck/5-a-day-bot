import urllib.request
import datetime
import requests
from io import BytesIO

output = BytesIO()

today = datetime.datetime.now().strftime("%B-%#m").lower()


def get_pdf():
  response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2015/09/{today}-pdf1.pdf")
  output.write(response.content)
  return output
  # output is File object that contains the pdf
  # Should be able to be sent using something like this
  # await channel.send(file=discord.File(output))

print(get_pdf())