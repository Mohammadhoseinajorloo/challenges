from instream import InStream
import sys

def _readHtml(stockSymbol):
    website = 'https://finance.yahoo.com/quote/'
    end = '?.tsrc=fin-srch'
    page = InStream(website + stockSymbol + end)
    html = page.readAll()
    return html

def priceOf(stockSymbol):
    html = _readHtml(stockSymbol)
    print(dir(html))


if __name__ == '__main__':
    stockSymbol = sys.argv[1]
    price = priceOf(stockSymbol)
    print(price)
