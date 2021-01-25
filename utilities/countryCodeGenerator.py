import random

from utilities import db_connector as db

""" Получение из базы списка стран по полям название, код, формат индекса, формат налогового кода """
def get_countries():
    data = db.fetchall("select name, iso_code_2, tax_id_format, postcode_format from lc_countries")
    country_dict = []
    for country in data:
        countries = {
            'country_name': country[0],
            'country_code': country[1],
            'tax_id_format': country[2],
            'postcode_format': country[3],
        }
        country_dict.append(countries)
    return country_dict

countries = get_countries()


def get_countries_codes():
    data = db.fetchall("select iso_code_2 from lc_countries")
    countries_codes = []
    for item in data:
        countries_codes.append(*item)
    return countries_codes

countries_codes_dict = get_countries_codes()

""" Нумерованный список кодов стран для выбора из селекта при регистрации пользователя"""
def get_enumerate_countries_codes(countries):
    countries_codes = []
    for idx, country in enumerate(countries):
        countries_codes.append(
            {idx: country['country_code']}
        )
    return countries_codes  # [{0: 'AF'}, {1: 'AL'}, {2: 'US'}...

enumerate_countries_codes = get_enumerate_countries_codes(countries)


""" Словарь по зонам, в качестве ключа код зоны, в качестве значение код страны  """
def get_zone_codes():
    zones_data = db.fetchall("select * from lc_zones")
    zones = {}
    for zone in zones_data:
        zones.update({
            zone[2]: zone[1]
        })
    return zones  # {'ACT': 'AU'}, {'NSW': 'US'}, {'NT': 'CA'}...

zone_codes = get_zone_codes()


""" список стран имеющих штаты """
def get_countries_with_state(zones):
    country_with_state = set()
    for value in zones.values():
        country_with_state.add(value)
    return country_with_state  # {'AU', 'CA', 'US'}

countries_with_state = get_countries_with_state(zone_codes)


""" словарь из стран со списком принадлежащих им штатов """
def get_country_states_linked_list(countries_list, zones):
    codes_dict = {}
    for code in countries_list:
        codes_dict[code] = [key for key, value in zones.items() if value == code]
    return codes_dict  # {'AU': ['ACT', 'NSW', 'QLD', 'SA', 'TAS', 'VIC'], 'CA': ['NT', 'AB']

country_states_linked_list = get_country_states_linked_list(countries_with_state, zone_codes)


def get_random_country_code(countries):
    code = random.choice(countries)
    return code

random_country_code = get_random_country_code(countries_codes_dict)


def get_random_state_code(country_code, countries_with_states, states_codes):
    if country_code in countries_with_states:
        state = random.choice(states_codes[country_code])
        return state
    else:
        return

random_state_code = get_random_state_code(random_country_code, countries_with_state, country_states_linked_list)
