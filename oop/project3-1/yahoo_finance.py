from instream import InStream
import stdio

url = 'https://finance.yahoo.com/quote/GOOG?.tsrc=fin-srch'

website = InStream(url)
stdio.writeln(website.readAllFloats())
