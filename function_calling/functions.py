functions = [
    
    ######### Trend Detection #########
    {
        "name": "detect_trend",
        "description": "It is designed primarily for financial data analysis and to analyzes the trend of a specified financial instrument over a given time range , enabling users to gauge the general direction of a security or market index. \
Returns a number between -2 and 2 that represents the trend’s intensity and direction. The value is interpreted as follows: \
-2: Strong downward trend, -1: Weak downward trend, 0: No significant trend / Neutral, 1: Weak upward trend, 2: Strong upward trend",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "enum": ['NQ', 'ES', 'GC', 'YM', 'RTY', 'CL'],
                    "description": '''The ticker symbol of the financial instrument to be analyzed.'''
                },
                "timerange": {
                    "type": "string",
                    "format": "date-time",
                    # "enum": ["hours", "days", "weeks", "months", "years"],
                    "description": '''The period over which the analysis is done.  This value should have a start (e.g. 3/10/2023 15:45:30) and an end(e.g. 3/10/2023 17:25:20)'''
                }
            },
            "required": ["symbol"]
        }
    },


    ######### Trend Visualization #########
    {
        "name": "show_trend",
        "description": "The function shows the trend of a specified financial instrument over a given time range on the chart. \
The function returns a boolean value which is true if the chart visualization is done and false otherwise.",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "enum": ['NQ', 'ES', 'GC', 'YM', 'RTY', 'CL'],
                    "description": '''The ticker symbol of the financial instrument to be analyzed.'''
                },
                "timerange": {
                    "type": "string",
                    "format": "date-time",
                    # "enum": ["hours", "days", "weeks", "months", "years"],
                    "description": '''The period over which the analysis is done. This value should have a start (e.g. 3/10/2023 15:45:30) and an end(e.g. 3/10/2023 17:25:20)'''
                },
                "trend": {
                    "type": "integer",
                    # "enum": [],
                    "minimum": -2,
                    "maximum": 2,
                    "description": '''The trend to show on the chart which is an integer between -2 and 2.'''
                }
            },
            "required": ["symbol", "timerange", "trend"]
        }
    },
    
    
    ######### Order Entry #########
    {
        "name": "order_entry_risk_manager",
        "description": "Opens a long or short trade based on user defined risk parameters. It allows users to place orders for various financial instruments, specifying the trade’s direction, type, and other key parameters. \
Returns True if the operation is successful and False otherwise.",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "enum": ['NQ', 'ES', 'GC', 'YM', 'RTY', 'CL'],
                    "description": '''The ticker symbol of the financial instrument to be analyzed.'''
                },
                "direction": {
                    "type": "string",
                    "enum": ["short", "long"],
                    "description": '''Specifies the trade direction. Acceptable values are ‘long’ for buying with the expectation that the asset will rise in value, and ‘short’ for selling with the expectation of buying back at a lower price.'''
                },
                "order_type": {
                    "type": "string",
                    "enum": ["limit", "market"],
                    "description": '''The type of the order to be placed. It can either be ‘market’ (an order to be executed immediately at the current market price) or ‘limit’ (an order to be executed at a specific price or better).'''
                },
                "price": {
                    "type": "number",
                    "enum": ["dollars"],
                    "description": '''The specific price at which a limit order is to be executed. This parameter is required if the type is ‘limit’. For market orders, this parameter is not applicable.'''
                },
                "size": {
                    "type": "integer",
                    # "enum": [],
                    "description": '''The size of the position, often referred to as the lot size. This denotes the quantity of the instrument to be traded.'''
                },
                "sl": {
                    "title": "stop_loss",
                    "type": "number",
                    "enum": ["dollars"],
                    "description": '''The stop-loss order price. It’s the price at which the position should be automatically closed to prevent further losses.'''
                },
                "tp": {
                    "title": "take_profit",
                    "type": "number",
                    "enum": ["dollars"],
                    "description": '''The take-profit order price. It’s the price at which the position should be automatically closed to secure profits.'''
                }
            },
            "required": ["symbol", "direction", "order_type", "size", "sl", "tp"]
        }
    },


    ######### Calculate Support and Resistance Levels #########
    {
        "name": "calculate_sr",
        "description": # "Identifying and scoring support and resistance levels in financial markets based on historical price data. \
"Support and resistance levels are key concepts in technical analysis, representing price points on a chart where the odds favor a pause or reversal of a prevailing trend. \
This function analyzes candlestick charts over a specified timeframe and lookback period to calculate these levels and their respective strengths. \
Returns a dictionary containing four lists, each corresponding to a specific aspect of the calculated support and resistance levels: \
1. levels_prices (list of floats): The prices at which support and resistance levels have been identified. \
2. levels_start_timestamps (list of timestamps): The starting timestamps for each identified level, indicating when the level first became relevant. \
3. levels_end_timestamps (list of timestamps): The ending timestamps for each level, marking when the level was last relevant. \
4. levels_scores (list of floats): Scores associated with each level, indicating the strength or significance of the level. Higher scores typically imply stronger levels.",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "enum": ['NQ', 'ES', 'GC', 'YM', 'RTY', 'CL'],
                    "description": '''The ticker symbol of the financial instrument to be analyzed.'''
                },
                "timeframe": {
                    "type": "string",
                    # "enum": ["days", "hours"],
                    "description": '''Specifies the timeframe of the candlestick chart to be analyzed. This parameter defines the granularity of the data used for calculating the levels.'''
                },
                "lookback_days": {
                    "type": "integer",
                    "enum": ["days"],
                    "description": '''The number of days to look back for calculating the support and resistance levels. This parameter determines the depth of historical data to be considered in the analysis.'''
                }
            },
            "required": ["symbol"]
        }
    },
    
    
    ######### News Analysis #########
    {
        "name": "news_analysis",
        "description": "The function is designed to identify and analyze upcoming high-impact financial news events related to a specific financial instrument. \
This function helps traders and analysts understand the potential market impact of forthcoming news, drawing on historical data to assess how similar news types have influenced the market in the past. \
Returns a dictionary containing three lists, each representing a different aspect of the upcoming news and their historical market impact: \
1. news_types (list of strings): The types of upcoming high-impact news events (e.g., ‘Interest Rate Decision’, ‘Earnings Report’). \
2. news_timestamps (list of timestamps): The scheduled timestamps for each upcoming news event. \
3. news_historical_analysis (list of strings/objects): Analysis of the historical impact of similar news types on the market. This could include quantitative data (like average price movement) or qualitative analysis (like typical market sentiment post-news).",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "enum": ['NQ', 'ES', 'GC', 'YM', 'RTY', 'CL'],
                    "description": '''The ticker symbol of the financial instrument to be analyzed.'''
                },
                "timerange": {
                    "type": "array",
                    "items": {"type": "integer"},
                    "format": "date-time",
                    # "enum": ["hours", "days", "weeks", "months", "years"],
                    "description": '''The period over which the analysis is done. This value should have a start (e.g. 3/10/2023 15:45:30) and an end(e.g. 3/10/2023 17:25:20)'''
                },
                "news_type": {
                    "type": "string",
                    # "enum": [],
                    "description": '''The specific type of news to be analyzed (e.g., ‘earnings report’, ‘federal announcement’). This parameter is optional and, if provided, filters the news to the specified type. If not specified, the function analyzes all types of high-impact news.'''
                }
            },
            "required": ["symbol"]
        }
    },


#     ######### Gap Detection #########
#     {
#         "name": "gap_detection",
#         "description": "Products opened with gap and the gap status right now. \
# For example, ES and NQ opened with gap today, ES with gap of 10 points and NQ with gap of 5 points. \
# The gap on ES is filled at 9:20:00 am and the gap on NQ is partially filled (2 points out of 5). \
# Output of the function can be like this: {'ES': [10,10,'09:20:00'], 'NQ': [5,2,'']} \
# Returns list of symbols and gaps size for each.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "symbol": {
#                     "type": "array",
#                     "items": {"type": "string"},
#                     "enum": ['NQ', 'ES', 'GC', 'YM', 'RTY', 'CL'],
#                     "description": '''The ticker symbol list of the financial instruments to be analyzed. The only allowed values for symbols are: NQ, ES, GC, CL, YM, RTY. Complete form of each symbol is as follows: NQ: E-mini Nasdaq-100, ES: E-mini S&P 500, GC: E-mini Gold, YM: E-mini Dow Jones Industrial Average Index, RTY: E-mini Russell 2000 Index, CL: E-mini Crude Oil'''
#                 },
#                 "date": {
#                     "type": "date-time",
#                     "description": '''Specifies the date that the analyzis will be done. Default is today'''
#                 }
#             },
#             "required": ["symbol", "date"]
#         }
#     },


#     ######### Higher Timeframe Confluence #########
#     {
#         "name": "htf_confluence",
#         "description": "Check confluence on higher timeframes. \
# If the trend on each of the upper timeframes is the same as input direction, it's considered as a confluence, otherwise as a contradiction.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "symbol": {
#                     "type": "string",
#                     "enum": ["NQ", "ES", "GC", "CL", "YM", "RTY"],
#                     "description": '''The ticker symbol of the financial instrument to be analyzed.'''
#                 },
#                 "higher_timeframes": {
#                     "type": "array",
#                     "items": {"type": "integer"},
#                     "description": '''The period over which the analysis is done'''
#                 }
#             },
#             "required": ["symbol"]
#         }
#     },


#     ######### Level Analysis #########
#     {
#         "name": "level_analysis",
#         "description": "Giving an analysis of most important levels in the current market based on the real-time reactions. \
# Returns a text output explaining the most important current level based on last price reactions if the level is breaking or holding in the last 5 minutes. \
# If there was no recent reaction, explain what are the nearest levels above and below the current price.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "symbol": {
#                     "type": "string",
#                     "enum": ["NQ", "ES", "GC", "CL", "YM", "RTY"],
#                     "description": '''The ticker symbol of the financial instrument to be analyzed.'''
#                 }
#             },
#             "required": ["symbol"]
#         }
#     },


#     ######### Limit Order Book Analysis #########
#     {
#         "name": "lob_analysis",
#         "description": "Giving the relative status of bid and ask sides in the order book and also provide insights on liquiditiy levels reactions and fillings. \
# Returns Float output for bid / ask lob ratio. Also a text output explaining the most important current liquidity level based on last price reactions if the level is breaking or holding in the last 5 minutes. \
# If there was no recent reaction, explain what are the nearest liquidity levels above and below the current price.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "symbol": {
#                     "type": "string",
#                     "enum": ["NQ", "ES", "GC", "CL", "YM", "RTY"],
#                     "description": '''The ticker symbol of the financial instrument to be analyzed.'''
#                 }
#             },
#             "required": ["symbol"]
#         }
#     }
]
