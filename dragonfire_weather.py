import re
import urllib2 #or urllib.requests for Python 3
import time
import itertools
# TODO:potentialy change noaa weather to wunderground weather
#--------------------------------------------Notes---------------------------------------------------
#Allowable commands: ["WHAT IS THE WEATHER FORCAST", "WHAT IS THE WEATHER LIKE", "WHAT IS THE WEATHER TOMORROW", 'WHAT IS THE WEATHER IN PARIS' (can substitute for any city here)]
#these commands are the basics, but this program will interpret any others that at least include 'WEATHER' as a keyword. One must specialize a particular operation, however
#this progam assumes that 'com' is all uppercase.
#--------------------------------------------------------------------------------------------------

com = "WHAT IS THE WEATHER IN ISTANBUL"

if 3 == 4:
    pass


elif "WEATHER" in com or "FORCAST" in com: #because it could be "SHOW THE FORCAST", which does not reference weather:
    url = "https://geoiptool.com/" #use this site to scrape for location


    req = urllib2.Request(url)

    resp = urllib2.urlopen(req)

    respData = resp.read()

    info = re.findall("<span>(.*?)</span>", str(respData))
    state = info[20]
    town = info[21]
    lat = info[-2]
    lon = info[-1]



    abbreviations = {'Mississippi': 'MS', 'Palau': 'PW', 'Northern': 'MP', 'Oklahoma': 'OK', 'Dist.': 'DC', 'Minnesota': 'MN', 'Micronesia': 'FM', 'Illinois': 'IL', 'Arkansas': 'AR', 'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 'California': 'CA', 'Massachusetts': 'MA', 'Puerto Rico': 'PR', 'Delaware': 'DE', 'New Hampshire': 'NH', 'Wisconsin': 'WI', 'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 'Pennsylvania': 'PA', 'West Virginia': 'WV', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 'Hawaii': 'HI', 'South Carolina': 'SC', 'American': 'AS', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 'Alabama': 'AL', 'Rhode Island': 'RI', 'Marshall': 'MH', 'Virgin Islands': 'VI', 'South Dakota': 'SD', 'Colorado': 'CO', 'New Jersey': 'NJ', 'Guam': 'GU', 'Washington': 'WA', 'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 'Nevada': 'NV', 'Maine': 'ME'}

    state_abbreviation = abbreviations[state]

    new_url = "http://forecast.weather.gov/MapClick.php?CityName={}&state={}&site=BOX&textField1={}&textField2={}#.WU7Br4qQxLw".format(town, state_abbreviation, lat, lon)




    try:
        newreq = urllib2.Request(new_url)

        newresp = urllib2.urlopen(newreq)

        newrespData = newresp.read()

    except:
        raise Warning("Unable to access page data.")


    if com == "WHAT IS THE WEATHER LIKE": #nest all of these related to "WEATHER" if weather in com: if com == what is the ....

        temp1 = re.findall('<p class="myforecast-current-lrg">(.*?)</p>', str(newrespData))[0] #ferhenight
        temp2 = re.findall('<p class="myforecast-current-sm">(.*?)</p>', str(newrespData))[0] #celcius
        wind_speed = re.findall('<td>W (.*?) mph</td>', str(newrespData))
        print "wind speed:", wind_speed[0], "mph"
        converter = {'F':'Fahrenheit', 'C':'Celsius'}

        first = temp1.split(';')
        second = temp2.split(';')
        print "Temperature for ", town, ",", state
        print first[0][:-4], "degrees", converter[first[-1]]

        print "(", second[0][:-4], "degrees", converter[second[-1]], ")"
        forcast = re.findall('<div class="col-sm-10 forecast-text">(.*?)</div>', str(newrespData))
        print "tonight:"

        print forcast[0]

        print "tomorrow:"
        print forcast[1]

    else:
        if "TOMORROW" in com:


            print "Tomorrow:"

            forcast = re.findall('<div class="col-sm-10 forecast-text">(.*?)</div>', str(newrespData))

            print forcast[1]

            print "Tomorrow night"
            print forcast[2]


        elif "FORCAST" in com:
            forcast = re.findall('<div class="col-sm-10 forecast-text">(.*?)</div>', str(newrespData))
            days = re.findall('<b>(.*?)</b>', str(newrespData))
            #print days[13:]


            for a, b in zip(days[13:], forcast):
                print a, ": ", b

        else:
            cities = {'Monterrey': 'Mexico', 'Zhengzhou': 'China', 'San Diego': 'United', 'Paris': 'France', 'Seoul South': 'Korea', 'Fortaleza': 'Brazil', 'Jeddah Saudi': 'Arabia', 'Zhongshan': 'China', 'San Francisco': 'United', 'Sao Paulo': 'Brazil', 'Shenzhen': 'China', 'Wuhan': 'China', 'Santiago': 'Chile', 'Chennai': 'India', 'Delhi': 'India', 'Baghdad': 'Iraq', 'Harbin': 'China', 'Ahmedabad': 'India', 'Pune': 'India', 'Addis Ababa': 'Ethiopia', 'Chittagong': 'Bangladesh', 'Ho Chi': 'Minh', 'Rome': 'Italy', 'Accra': 'Ghana', 'Surat': 'India', 'Taipei': 'Taiwan', 'Kanpur': 'India', 'Alexandria': 'Egypt', 'Casablanca': 'Morocco', 'Osaka': 'Japan', 'Shenyang': 'China', 'Milan': 'Italy', 'Medan': 'Indonesia', 'Miami United': 'States', 'Yangon': 'Myanmar', 'Guadalajara': 'Mexico', 'Bangkok': 'Thailand', 'Sydney': 'Australia', 'Durban South': 'Africa', 'Kolkata': 'India', 'Curitiba': 'Brazil', 'Melbourne': 'Australia', 'Singapore': 'Singapore', 'Moscow': 'Russia', 'Guangzhou': 'China', 'Hefei': 'China', 'Kuala Lumpur': '(Klang', 'Berlin': 'Germany', 'Los Angeles': 'United', 'Tehran': 'Iran', "Sana'a": 'Yemen', 'Seattle United': 'States', 'Karachi': 'Pakistan', 'Kuwait City': 'Kuwait', 'Xiamen': 'China', 'Ibadan': 'Nigeria', 'Lucknow': 'India', 'Boston United': 'States', 'Kano': 'Nigeria', 'Cape Town': 'South', 'Shijiazhuang': 'China', 'Hangzhou': 'China', 'Abidjan Ivory': 'Coast', 'Changzhou': 'China', 'Ningbo': 'China', 'Madrid': 'Spain', 'Yaounde': 'Cameroon', 'Rio de': 'Janeiro', 'Fuzhou': 'China', 'Wuxi': 'China', 'Detroit United': 'States', 'Mexico City': 'Mexico', 'Philadelphia United': 'States', 'Istanbul': 'Turkey', 'Hanoi': 'Vietnam', 'Mashhad': 'Iran', 'Quanzhou': 'China', 'Aleppo': 'Syria', 'Bengaluru': 'India', 'Manila': 'Philippines', 'Lahore': 'Pakistan', 'urumi': 'China', 'Dongguan': 'China', 'Luanda': 'Angola', 'Jaipur': 'India', 'Khartoum': 'Sudan', 'Kunming': 'China', 'Faisalabad': 'Pakistan', 'Hong Kong': 'China', 'Toronto': 'Canada', 'Houston United': 'States', 'Tokyo': 'Japan', 'London': 'United Kingdom', 'Athens': 'Greece', 'Bogota': 'Colombia', 'Tel Aviv': 'Israel', 'Nairobi': 'Kenya', 'Montreal': 'Canada', 'Beijing': 'China', 'Dubai United': 'Arab', 'Chicago United': 'States', 'New York': 'City', 'Lima': 'Peru', 'Belo Horizonte': 'Brazil', 'Dares Salaam': 'Tanzania', 'Surabaya': 'Indonesia', 'Mumbai': 'India', 'Tianjin': 'China', 'Shanghai': 'China', 'Nagoya': 'Japan', 'Kabul': 'Afghanistan', 'Dakar': 'Senegal', 'Saint Petersburg': 'Russia', 'Zhangjiagang': 'China', 'Porto Alegre': 'Brazil', 'Dallas United': 'States', 'Naples': 'Italy', 'Busan South': 'Korea', 'Kinshasa Democratic': 'Republic', 'Wenzhou': 'China', 'Buenos Aires': 'Argentina', 'Changchun': 'China', 'Greater Cairo': 'Egypt', 'Ankara': 'Turkey', 'Johannesburg South': 'Africa', 'Qingdao': 'China', 'Chongqing': 'China', 'Dhaka': 'Bangladesh', 'Riyadh Saudi': 'Arabia', 'Salvador': 'Brazil', 'Jakarta': 'Indonesia', 'Atlanta United': 'States', 'Taiyuan': 'China', 'Barcelona': 'Spain', 'Changsha': 'China', 'Bandung': 'Indonesia', 'Suzhou': 'China', 'Recife': 'Brazil', 'Washington D.C.': 'United', 'Dalian': 'China', 'Chengdu': 'China', 'Jinan': 'China', 'Nanjing': 'China', 'Lagos': 'Nigeria', 'Phoenix United': 'States', 'Izmir': 'Turkey'}


            abbrs = {'ERITREA': 'er', 'PORTUGAL': 'pt', 'NEW CALEDONIA': 'nc', 'SVALBARD AND JAN MAYEN': 'sj', 'BAHAMAS': 'bs', 'TOGO': 'tg', 'WESTERN SAHARA': 'eh', 'CROATIA': 'hr', 'LUXEMBOURG': 'lu', 'SAINT VINCENT AND THE GRENADINES': 'vc', 'KIRIBATI': 'ki', 'THAILAND': 'th', 'BARBADOS': 'bb', 'BENIN': 'bj', 'YEMEN': 'ye', 'ALGERIA': 'dz', 'KAZAKHSTAN': 'kz', 'SAINT HELENA': 'sh', 'COSTA RICA': 'cr', 'ARUBA': 'aw', 'ETHIOPIA': 'et', 'HINA': 'cn', 'HEARD ISLAND AND MCDONALD ISLANDS': 'hm', 'NIUE': 'nu', 'PERU': 'pe', 'ANGUILLA': 'ai', 'NORWAY': 'no', 'QATAR': 'qa', 'PALAU': 'pw', 'NORFOLK ISLAND': 'nf', 'DENMARK': 'dk', 'NEPAL': 'np', 'AZERBAIJAN': 'az', 'PAPUA NEW GUINEA': 'pg', 'UNITED STATES': 'us', 'ZIMBABWE': 'zw', 'GABON': 'ga', 'GIBRALTAR': 'gi', 'SWAZILAND': 'sz', 'VANUATU': 'vu', 'IRAQ': 'iq', 'URINAME': 'sr', 'PALESTINIAN TERRITORY, OCCUPIED': 'ps', 'ECUADOR': 'ec', 'UZBEKISTAN': 'uz', 'AUSTRALIA': 'au', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS': 'gs', 'FRENCH SOUTHERN TERRITORIES': 'tf', 'PITCAIRN': 'pn', 'GAMBIA': 'gm', 'WALLIS AND FUTUNA': 'wf', 'CENTRAL AFRICAN REPUBLIC': 'cf', 'FRANCE': 'fr', 'TRINIDAD AND TOBAGO': 'tt', 'ARMENIA': 'am', 'KUWAIT': 'kw', 'SRI LANKA': 'lk', 'OLIVIA': 'bo', 'TURKS AND CAICOS ISLANDS': 'tc', 'COMOROS': 'km', 'SAINT PIERRE AND MIQUELON': 'pm', 'TONGA': 'to', 'GEORGIA': 'ge', 'HONDURAS': 'hn', 'SOUTH AFRICA': 'za', 'MAYOTTE': 'yt', 'INDONESIA': 'id', 'VIET NAM': 'vn', 'ANTARCTICA': 'aq', 'ANTIGUA AND BARBUDA': 'ag', 'COLOMBIA': 'co', 'MARTINIQUE': 'mq', 'SWITZERLAND': 'ch', 'MOLDOVA, REPUBLIC OF': 'md', 'CANADA': 'ca', 'JAMAICA': 'jm', 'EQUATORIAL GUINEA': 'gq', 'EGYPT': 'eg', 'LEBANON': 'lb', 'MONGOLIA': 'mn', 'SIERRA LEONE': 'sl', 'COCOS (KEELING) ISLANDS': 'cc', 'AUSTRIA': 'at', 'CONGO': 'cg', 'MALI': 'ml', 'MAURITANIA': 'mr', 'COOK ISLANDS': 'ck', 'PAKISTAN': 'pk', 'SEYCHELLES': 'sc', 'ANGOLA': 'ao', 'SAINT LUCIA': 'lc', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF": 'kp', 'SAINT KITTS AND NEVIS': 'kn', 'UNITED STATES MINOR OUTLYING ISLANDS': 'um', 'SENEGAL': 'sn', 'MALAYSIA': 'my', 'TANZANIA, UNITED REPUBLIC OF': 'tz', 'R\xc3\x89UNION': 're', 'OMAN': 'om', 'IRELAND': 'ie', 'RUSSIAN FEDERATION': 'ru', 'GRENADA': 'gd', 'NEW ZEALAND': 'nz', 'NIGERIA': 'ng', 'KYRGYZSTAN': 'kg', 'BANGLADESH': 'bd', 'ESTONIA': 'ee', 'BOUVET ISLAND': 'bv', 'ICELAND': 'is', 'SLOVENIA': 'si', 'BRUNEI DARUSSALAM': 'bn', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF': 'mk', 'LESOTHO': 'ls', 'SYRIAN ARAB REPUBLIC': 'sy', 'TUNISIA': 'tn', 'BOSNIA AND HERZEGOVINA': 'ba', 'MICRONESIA, FEDERATED STATES OF': 'fm', 'MONACO': 'mc', 'JAPAN': 'jp', 'UKRAINE': 'ua', 'ISRAEL': 'il', 'CHAD': 'td', 'MEXICO': 'mx', 'SUDAN': 'sd', 'TUVALU': 'tv', 'LITHUANIA': 'lt', 'CAPE VERDE': 'cv', 'UNITED KINGDOM': 'gb', 'MOROCCO': 'ma', 'NETHERLANDS': 'nl', 'UGANDA': 'ug', "LAO PEOPLE'S DEMOCRATIC REPUBLIC": 'la', 'BOTSWANA': 'bw', 'BRAZIL': 'br', 'MADAGASCAR': 'mg', 'ALBANIA': 'al', 'CZECH REPUBLIC': 'cz', 'BRITISH INDIAN OCEAN TERRITORY': 'io', 'SWEDEN': 'se', 'VIRGIN ISLANDS, U.S.': 'vi', 'RWANDA': 'rw', 'GERMANY': 'de', 'HRISTMAS ISLAND': 'cx', 'PUERTO RICO': 'pr', 'NIGER': 'ne', 'HONG KONG': 'hk', 'MALAWI': 'mw', 'AFGHANISTAN': 'af', 'SAUDI ARABIA': 'sa', 'ITALY': 'it', 'AROE ISLANDS': 'fo', 'PHILIPPINES': 'ph', 'MONTSERRAT': 'ms', 'TAIWAN, PROVINCE OF CHINA': 'tw', 'BERMUDA': 'bm', 'FRENCH GUIANA': 'gf', 'SOMALIA': 'so', 'ARGENTINA': 'ar', 'CYPRUS': 'cy', 'TURKMENISTAN': 'tm', 'BAHRAIN': 'bh', 'MALDIVES': 'mv', 'MYANMAR': 'mm', 'SERBIA AND MONTENEGRO': 'cs', 'NICARAGUA': 'ni', 'CAYMAN ISLANDS': 'ky', 'MARSHALL ISLANDS': 'mh', 'LATVIA': 'lv', 'SLOVAKIA': 'sk', 'GUYANA': 'gy', 'BELGIUM': 'be', 'MOZAMBIQUE': 'mz', 'TIMOR': 'tl', 'BURKINA FASO': 'bf', 'LIBERIA': 'lr', 'SAN MARINO': 'sm', 'GUAM': 'gu', 'AMERICAN SAMOA': 'as', 'MAURITIUS': 'mu', 'LIECHTENSTEIN': 'li', 'NAMIBIA': 'na', 'TAJIKISTAN': 'tj', 'GREECE': 'gr', 'NETHERLANDS ANTILLES': 'an', 'NAURU': 'nr', 'BELIZE': 'bz', 'FIJI': 'fj', 'LIBYAN ARAB JAMAHIRIYA': 'ly', 'ROMANIA': 'ro', 'GREENLAND': 'gl', 'TURKEY': 'tr', 'EL SALVADOR': 'sv', 'POLAND': 'pl', 'KOREA, REPUBLIC OF': 'kr', 'INDIA': 'in', 'GUATEMALA': 'gt', 'CAMBODIA': 'kh', 'SOLOMON ISLANDS': 'sb', 'HUNGARY': 'hu', 'MACAO': 'mo', 'SPAIN': 'es', 'CUBA': 'cu', 'UNITED ARAB EMIRATES': 'ae', 'FINLAND': 'fi', 'MALTA': 'mt', 'ANDORRA': 'ad', 'DJIBOUTI': 'dj', 'BELARUS': 'by', 'JORDAN': 'jo', 'KENYA': 'ke', 'PARAGUAY': 'py', 'DOMINICAN REPUBLIC': 'do', 'VIRGIN ISLANDS, BRITISH': 'vg', 'DOMINICA': 'dm', 'GHANA': 'gh', 'SAO TOME AND PRINCIPE': 'st', 'SAMOA': 'ws', 'NORTHERN MARIANA ISLANDS': 'mp', 'BHUTAN': 'bt', 'URUGUAY': 'uy', 'CONGO, THE DEMOCRATIC REPUBLIC OF': 'cd', 'GUINEA': 'gw', 'PANAMA': 'pa', 'SINGAPORE': 'sg', 'IRAN, ISLAMIC REPUBLIC OF': 'ir', 'FRENCH POLYNESIA': 'pf', 'TOKELAU': 'tk', 'FALKLAND ISLANDS (MALVINAS)': 'fk', 'CHILE': 'cl', 'BURUNDI': 'bi', 'HAITI': 'ht', 'GUADELOUPE': 'gp', 'CAMEROON': 'cm', 'BULGARIA': 'bg'}
            new_com = com.split()


            city = [i for i in new_com if i.lower() in [b.lower() for b in cities.keys()]][0] #city will still be all uppercase
            city1 = city[0].upper()+city.lower()[1:] #'PARIS' to 'Paris'



            try: #here, attempting to make program more robust
                city_abbreviation = abbrs[cities[city1].upper()] #'fr', for 'PARIS'
                print city_abbreviation


            except KeyError:
                raise KeyError("Unable to find your location in our data")


            else:


                the_url = "https://www.wunderground.com/{}/{}?MR=1".format(city_abbreviation, city.lower()) #'fr', 'paris'


                req = urllib2.Request(the_url)

                resp = urllib2.urlopen(req)

                respData = resp.read()

                temperature = re.findall('<span class="wx-value">(\d{1,3})</span>', str(respData))[2]

                skies = re.findall('<span class="wx-value">(\w{1,})</span>', str(respData))[2]

                print "Weather for ", city1
                print temperature, "F"
                print "skies:", skies
