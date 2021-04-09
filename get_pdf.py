import urllib.request
import datetime
import requests
from io import BytesIO, StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader

f = BytesIO()

month = datetime.datetime.now().strftime("%B")
day = datetime.datetime.now().strftime("%#d")

def get_pdf():
  response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2019/03/{month}-Higher.pdf")
  input_file = PdfFileReader(BytesIO(response.content))
  output_file = PdfFileWriter()
  output_file.addPage(input_file.getPage(int(day)))
  output_file.write(f)
  f.seek(0)
  return f

  # output is File object that contains the pdf
  # Should be able to be sent using something like this
  # await channel.send(file=discord.File(output))