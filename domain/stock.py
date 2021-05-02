class stock:
    def __init__(self, ticker, amount, price):
        self.ticker=ticker
        self.amount=int(amount)
        self.costbase=float(price)
    def add(self,price,amount):
        original_investment=self.amount*self.costbase
        new_investment=price*amount
        self.amount+=amount
        self.costbase=(original_investment+new_investment)/self.amount
    def sell(self,amount):
        if self.amount>=amount:
            self.amount-=amount
            if self.amount<0:
                self=None
            print(self.amount)