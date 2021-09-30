import requests
import settings


class StockTimesSeries:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY

    def _build_url(self, path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"

    def send_request(self, url):
        resp = requests.get(url)
        if resp.status_code == 200:
            showData = int(input('Consult realized sucessfully!\nPress 1 for view JSON\nPress 0 exit\n'))
            if showData != 1:
                return print('Exit...')
            else:
                return print(resp.json())

    def intraday_series(self, function, symbol, interval, **kwargs):
        """
        This API returns the most recent 1-2 months of intraday data and is best suited for short-term/medium-term
        charting and trading strategy development.
        :more info: https://www.alphavantage.co/documentation/#intraday


        :param function: str (required)
        :param symbol: str   (required)
        :param interval: str (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}&interval={interval}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def daily_series(self, function, symbol, **kwargs):
        """
        This API returns raw daily time series of the global equity specified, covering 20+ years of historical data.
        :more info: https://www.alphavantage.co/documentation/#daily

        :param function: str (required)
        :param symbol: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def daily_adjusted_series(self, function, symbol, **kwargs):
        """
        This API returns raw daily open/high/low/close/volume values, daily adjusted close values, and historical
        split/dividend events of the global equity specified, covering 20+ years of historical data.
        :more info: https://www.alphavantage.co/documentation/#dailyadj


        :param function: str (required)
        :param symbol: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def weekly_series(self, function, symbol, **kwargs):
        """
        This API returns weekly time series (last trading day of each week, weekly open, weekly high, weekly low, weekly
        close, weekly volume) of the global equity specified, covering 20+ years of historical data.
        :more info: https://www.alphavantage.co/documentation/#weekly


        :param function: str (required)
        :param symbol: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def weekly_adjusted_series(self, function, symbol, **kwargs):
        """
        This API returns weekly adjusted time series of the global equity specified,
        covering 20+ years of historical data.
        :more info: https://www.alphavantage.co/documentation/#weeklyadj

        :param function: str (required)
        :param symbol: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def monthly_series(self, function, symbol, **kwargs):
        """
        This API returns monthly time series (last trading day of each month, monthly open, monthly high, monthly low,
        monthly close, monthly volume) of the global equity specified, covering 20+ years of historical data.
        :more info: https://www.alphavantage.co/documentation/#monthly

        :param function: str (required)
        :param symbol: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def monthly_adjusted_series(self, function, symbol, **kwargs):
        """
        This API returns monthly adjusted time series (last trading day of each month, monthly open, monthly high,
        monthly low, monthly close, monthly adjusted close, monthly volume, monthly dividend) of the equity specified,
        covering 20+ years of historical data.
        :more info: https://www.alphavantage.co/documentation/#monthlyadj

        :param function: str (required)
        :param symbol: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def choice_endpoint(self, function, symbol, **kwargs):
        """
        A lightweight alternative to the time series APIs, this service returns the price and volume information for a
        security of your choice.
        :more info: https://www.alphavantage.co/documentation/#latestprice

        :param function: str (required)
        :param symbol: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&symbol={symbol}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)

    def search_endpoint(self, function, keywords, **kwargs):
        """
         The Search Endpoint returns the best-matching symbols and market information based on keywords of your choice.
        :more info: https://www.alphavantage.co/documentation/#symbolsearch

        :param function: str (required)
        :param keywords: str   (required)
        :param kwargs: dict  (optional)
        """
        path = f"function={function}&keywords={keywords}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path
        url = self._build_url(path)
        self.send_request(url)


test = StockTimesSeries()

# TIME_SERIES_INTRADAY
# test.intraday_series('CASH_FLOW', 'IBM', '5min', outputsize='compact', adjusted='true', datatype='json')

# TIME_SERIES_DAILY
# test.daily_series('TIME_SERIES_DAILY', 'IBM', outputsize='full', datatype='json')

# TIME_SERIES_DAILY_ADJUSTED
# test.daily_adjusted_series('TIME_SERIES_DAILY_ADJUSTED', 'IBM', outputsize='compact', datatype='csv')

# TIME_SERIES_WEEKLY
# test.weekly_series('TIME_SERIES_WEEKLY', 'IBM', datatype='json')

# TIME_SERIES_WEEKLY_ADJUSTED
# test.weekly_adjusted_series('TIME_SERIES_WEEKLY_ADJUSTED', 'IBM', datatype='json')

# TIME_SERIES_MONTHLY_ADJUSTED
# test.monthly_series('TIME_SERIES_MONTHLY', 'IBM', datatype='json')

# TIME_SERIES_MONTHLY_ADJUSTED
# test.monthly_adjusted_series('TIME_SERIES_MONTHLY_ADJUSTED', 'IBM', datatype='json')

# QUOTE ENDPOINT
# test.choice_endpoint('GLOBAL_QUOTE', 'IBM', datatype='json')

# SEARCH ENDPOINT
# test.search_endpoint('SYMBOL_SEARCH', 'microsoft', datatype='json')


