from helpers import get_countries
import random

__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'


def create_passport(
    name,
    date_of_birth,
    place_of_birth,
    height,
    nationality
):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": float(height),
        "nationality": nationality
    }
    return passport


def add_stamp(
    passport,
    visited_country
):
    nationality = passport.get("nationality")
    visited_countries = passport.get("stamps")
    if ("stamps" not in passport and visited_country != nationality):
        passport["stamps"] = []
        passport["stamps"].append(visited_country)
    elif (visited_countries is not None and visited_country not in visited_countries and
            visited_country != nationality):
        passport["stamps"].append(visited_country)
    else:
        passport = passport
    return passport


def check_passport(
    passport,
    country,
    allowed,
    not_allowed
):
    print(passport)
    nationality = passport.get("nationality")
    visited_countries = passport.get("stamps")
    print(visited_countries)
    countries_allowed = allowed.get(nationality)
    countries_not_allowed = not_allowed.get(country)

    country_allowed = False
    if country in countries_allowed:
        print(f"Allowed to visit {country} by home nation {nationality}")
        country_allowed = True
    else:
        country_allowed = False

    visited_countries_not_allowed = False
    if countries_not_allowed is not None and visited_countries is not None:
        for country in countries_not_allowed:
            if country in visited_countries:
                print('Traveller has visited forbidden country')
                visited_countries_not_allowed = True
            else:
                visited_countries_not_allowed = False

    nationality_allowed = True
    if countries_not_allowed is not None:
        if nationality not in countries_not_allowed:
            print('Traveller is not from forbidden country')
            nationality_allowed = True
        else:
            nationality_allowed = False

    if (country_allowed is True and
            visited_countries_not_allowed is False and
            nationality_allowed is True):
        passport["stamps"].append(country)
        print(passport)
        return passport
    else:
        print(False)
        return False


if __name__ == "__main__":
    julia = create_passport(
        "Julia",
        "1989-10-07",
        "Hilversum",
        1.72,
        "Belgium")
    add_stamp(julia, "North-Korea")
    check_passport(
        julia,
        "Netherlands",
        {'Belgium': ['Netherlands']},
        {'Netherlands': ['North-Korea']}
        )
