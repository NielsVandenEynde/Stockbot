from forex_python.converter import CurrencyRates
import urllib, bs4, requests
def convertToEuro(amount):
    c=CurrencyRates()
    rate=c.get_rate('USD','EUR')
    return amount*rate

### commands
def get_stock_price(name):

    url = requests.get('https://finance.yahoo.com/quote/'+name)
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    price = float(soup.find_all("div", {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text)
    return price
