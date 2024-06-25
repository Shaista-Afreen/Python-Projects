# Currency Converter
#Install necessary libraries
#pip install CurrencyConverter
from currency_converter import CurrencyConverter

def main():
    print("This is a Currency Converter Project")
    print("Currencies that can be used are : ['INR','USD','EUR','JPY','AUD','CAD','GBP','CNY','NZD', 'BRL','HKD']")


    value = float(input("Enter the value you wish to convert:"))

    input_currency = input("Please input the source currency: ")
    desired_currency = input("Please input the desired currency: ")

    # CurrencyConverter.convert()
    c = CurrencyConverter()

    converted_value = c.convert(value,input_currency,desired_currency)

    print(f"The {value} {input_currency} in {desired_currency} is : {converted_value}")
main()    