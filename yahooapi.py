try:
    import yfinance
except ModuleNotFoundError:
    print("Yahoo API not available")

class YahooAPI:
    def __pandasSeriesToList(self, series) -> list:
        return list(series.values)
        
    def getHighLowData(self, symbol: str) -> list[float]:
        """ Returns list containing high and low prices of the share for last 10 days. When error occures, returns None. """

        # load stock data
        try:
            stock = yfinance.Ticker(symbol)
        except NameError:
            # user is trying to use Yahoo API, but yfinance not installed
            return None
        tenDays = stock.history(period="1mo")
        if len(tenDays) == 0:
            # no data found, so the symbol must be incorrect
            return None

        # turn separate high and low lists into one
        highs = self.__pandasSeriesToList(tenDays["High"][-10:])
        lows = self.__pandasSeriesToList(tenDays["Low"][-10:])
        highLowList = []
        for i in range(10):
            highLowList.append(highs[i])
            highLowList.append(lows[i])
        return highLowList
        