import stock
import helperFunctions
class user:

    def __init__(self, stocks=[]):
        self.stocks=stocks
    
    def addStock(self, ticker, amount, price):
        for s in self.stocks:
            if s.ticker ==ticker:
                s.add(price, amount)
                return
        self.stocks.append(stock.stock(ticker,amount,price))
    
    def as_dict(self):
        if self.stocks:
            return {'stocks':[stok.__dict__ for stok in self.stocks]}
        else:
            return{'stocks': []}

    def sellStock(self,ticker,amount):
        for s in self.stocks:
            if s.ticker==ticker:
                s.sell(amount)
                if s.amount==0:
                    self.stocks.remove(s)
                return 0
        return 1

    def getTotalValue(self):
        value=0
        for stock in self.stocks:
            value+=stock.amount*helperFunctions.convertToEuro(helperFunctions.get_stock_price(stock.ticker))
        return round(value,2)
