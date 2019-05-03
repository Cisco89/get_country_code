def get_country_codes(prices):

    #for each comma sep value make a list
    #for each remove the comma
    #for each separate by "$" symbol
    #for each remove the number, maybe isalpha()
    #return list as a string comma sep each value
    countries_with_number = prices.split()
    country_list = []
    for country in countries_with_number:
        country_list.append(country[:2])
    return ", ".join(country_list)

    # your code here

print(get_country_codes("ca$199, ba$101"))
# some tests to check your work. You shouldn't modify these.
#from test import testEqual

#testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
#testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
#testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
#testEqual(get_country_codes("CA$40"), "CA")