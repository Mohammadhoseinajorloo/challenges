import json, requests


api = 'https://api.nobitex.ir/market/stats?dstCurrency=usdt&srcCurrency=btc,eth,bnb'


# Exception class
# -----------------------------------------

# this exception for error api
class JSONDecodeError(BaseException):
     pass

# this exeptioon for error in key json api
class KeyJsonExeption(BaseException):
     pass

# this exeption for error negative value in calculate_perfit_or_loss function
class NegaticException(BaseException):
     pass

# ------------------------------------------



# Color class
# -------------------------------------------

# this class for display gained, loss and warnings in error and more checking errors
class bcolors:
     OKGREEN = '\033[92m'
     WARNING = '\033[93m'
     ENDC = '\033[0m'
     RED = '\033[91m'

# -------------------------------------------


# Functions
# ----------------------------------------

# read api function
def read_api(api):
    try:
        r = requests.get(api)
        json_ = json.loads(r.text)
        return json_
    except:
        raise JSONDecodeError(f'Please check api,your input api is {bcolors.WARNING}{api}{bcolors.ENDC}')


# fide price and volomes in json api
def get_perice(json_):
     try:
         number_of_shares = float(json_['stats']['btc-usdt']['volumeSrc'])
         purchase_price = float(json_['stats']['btc-usdt']['bestSell'])
         sale_price = float(json_['stats']['btc-usdt']['latest'])
         return number_of_shares, purchase_price, sale_price
     except:
         raise KeyJsonExeption(f"Please checking key in json api. {bcolors.WARNING}{json_}{bcolors.ENDC}")
 

# calculate perfit and loss
def calculate_perfit_or_loss(number_of_shares, purchase_price, sale_price):
    number_of_shares_condition = number_of_shares < 0
    purchase_price_condition = purchase_price < 0
    sale_price_condition = sale_price < 0
    if number_of_shares_condition or purchase_price_condition or sale_price_condition:
        raise NegaticException(f"Can not negative price and volum a things.your vlaue is {bcolors.WARNING}'number of shares :  {number_of_shares} , purchase_price : {purchase_price}, sale_price: {sale_price}'{bcolors.ENDC}")

    buy = float(number_of_shares * purchase_price)
    first_commission = float(buy * .03)

    sale = float(number_of_shares * sale_price)
    second_commission = float(sale * .03)

    net = float(sale - buy - first_commission - second_commission)
    if net > 0:
        return f"After the transaction, you gained {bcolors.OKGREEN}{round(net, 2)}{bcolors.ENDC} dollars."
    if net < 0:
        return f"After the transaction, you lost {bcolors.RED}{round(net * -1, 2)}{bcolors.ENDC} dollars."

#-----------------------------------------------


# Main Progrramm
# -------------------------------------------------

def main():
    json_ = read_api(api)
    number_of_shares, purchase_price, sale_price = get_perice(json_)
    print(calculate_perfit_or_loss(number_of_shares, purchase_price, sale_price))

# --------------------------------------------------


if __name__ == "__main__":
    main()
