from tkinter import *
import requests

#Marketstack API
BASE_URL = 'http://api.marketstack.com/v1/tickers/'
API_KEY = 'redacted'

#Dividends have been hard coded due to api not consistently containing the information, should not be an issue as dividend returns do not change frequently
DIV_DICT = {'Apple':['AAPL', 0.88 ], 'Coca-Cola':['KO', 1.76], 'Starbucks':['SBUX', 1.96], 'Nike':['NKE', 1.22], 'Target':['TGT', 3.60]}


#Makes API call and loads stock data
def load_company(choice):
    choice = company.get()
    choice_ticker = DIV_DICT[choice][0]
    params = {'access_key': API_KEY}
    target_url = f'{BASE_URL}{choice_ticker}/eod/latest'
    api_result = requests.get(target_url, params)
    api_response = api_result.json()
    eod_text.set(value=api_response['close'])
    ticker_text.set(value=choice_ticker)
    dividend_text.set(value=f'{DIV_DICT[choice][1]:.2f}') 

#Calculates the number and values of share necessary to reach the given annual dividend return
def calc_shares():
    target = float(target_text.get())
    dividend = float(dividend_text.get())
    eod = float(eod_text.get())
    num_shares = target / dividend
    shares_text.set(value=f'{num_shares:.2f}')
    stock_value = eod * num_shares
    value_text.set(value=f'{stock_value:.2f}')



# Create window object
app = Tk()

app.title('Divivend Calculator')
app.geometry('800x600')

stock_ticker = Label(app, text='Company Name:', font=('bold', 14), pady=20)
stock_ticker.grid(row=0, column=0)

# List of Companies Drop Down
# Apple, Nike, Starbucks, Coca-Cola, Target
company_select = ['Apple', 'Nike', 'Starbucks', 'Coca-Cola', 'Target']

company = StringVar()
company.set(company_select[0])

dropdown = OptionMenu(app, company, *company_select, command=load_company)
dropdown.grid(row = 0, column=1)


#Desired value of dividend
target_text = StringVar(value='100')
target_label = Label(app, text='Desired value:', font=('bold', 14), pady=20)
target_label.grid(row=2, column=0)
target_entry = Entry(app, textvariable=target_text)
target_entry.grid(row=2, column=1)

#Current EOD share price
eod_text = StringVar()
eod_label = Label(app, text='Price per share:', font=('bold', 14), pady=20)
eod_label.grid(row=1, column=0)
eod_value = Label(app, textvariable=eod_text, font=('bold', 14))
eod_value.grid(row=1, column=1)

#Stock Ticker
ticker_text = StringVar()
ticker_label = Label(app, text='Stock Ticker:', font=('bold', 14))
ticker_label.grid(row=0, column=2)
ticker_value = Label(app, textvariable=ticker_text, font=('bold', 14))
ticker_value.grid(row=0, column=3)

#Stored dividend value
dividend_text = StringVar()
dividend_label = Label(app, text='Annual dividend return per share:', font=('bold', 14))
dividend_label.grid(row=1, column=2)
dividend_value = Label(app, textvariable=dividend_text, font=('bold', 14))
dividend_value.grid(row=1, column=3)

#Value of shares
value_text = StringVar()
value_label = Label(app, text='Value of shares:', font=('bold', 14))
value_label.grid(row=4, column=2)
value_share = Label(app, textvariable=value_text, font=('bold', 14))
value_share.grid(row=4, column=3)

#number of shares
shares_text = StringVar()
shares_label = Label(app, text='Number of shares', font=('bold', 14), pady=20)
shares_label.grid(row=4, column=0)
shares_value = Label(app, textvariable=shares_text, font=('bold', 14))
shares_value.grid(row=4, column=1)

#Calculate button
calc_button = Button(app, text='Calculate', width=12, command=calc_shares, pady=20)
calc_button.grid(row=3, column=1, pady=20)

# Start program
app.mainloop()