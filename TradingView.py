from tradingview_ta import TA_Handler, Exchange, Interval

Stock = TA_Handler(
    symbol='META',
    screener='america',
    interval=Interval.INTERVAL_1_MONTH,
    exchange='NASDAQ'
)

print(Stock.get_analysis().summary)