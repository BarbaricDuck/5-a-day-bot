import urllib.request
import requests
from io import BytesIO, StringIO
from PyPDF2 import PdfFileWriter, PdfFileReader

f = BytesIO()

def get_pdf(month,day):

  if month in ['January']:
    response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2019/02/{month}-Higher.pdf")
  
  elif month in ['February']:
    response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2020/02/{month}-Higher.pdf")

  elif month in ['March','April','May','June']:
    response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2019/03/{month}-Higher.pdf")
  
  elif month in ['July','August','November','December']:
    response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2019/08/{month}-Higher.pdf")

  elif month in ['September','October']:
    response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2019/07/{month}-Higher.pdf")

  else:
    response = requests.get(f"https://corbettmaths.com/wp-content/uploads/2019/03/{month}-Higher.pdf")
  
  input_file = PdfFileReader(BytesIO(response.content))



  output_file = PdfFileWriter()
  output_file.addPage(input_file.getPage(int(day)-1))
  output_file.write(f)
  f.seek(0)
  return f

  # output is File object that contains the pdf
  # Should be able to be sent using something like this
  # await channel.send(file=discord.File(output))