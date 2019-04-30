def get_country_codes(prices):
    country_code_list = []
    prices_list = prices.split(', ')
    for item in prices_list:
        string_split = item.split('$')
        country_code = string_split[0]
        country_code_list.append(country_code)

    return ", ".join(country_code_list)    
