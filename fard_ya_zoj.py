"""Help for those desperate Iranian students in trouble
who wonder if this week is Fard or Zoj!
"""

import random
import jdatetime


def print_random_response(responses: list):
    """Prints a random response from response list"""
    print(random.choice(responses))


def main(university_start_date: jdatetime):
    """Prints fard or zoj for today"""
    today = jdatetime.date.today()
    diff = (today - university_start_date).days

    if diff < 0:
        responses = [
            "Hanuz shoru nashode ke!",
            "Che ajaleyi dari pesaram/dokhtaram!",
            "Mashalla che zerange, az alan be fekre darse!",
            "Shoru nashode, vali hafteye aval farde.",
        ]
        print_random_response(responses)
    elif diff == 0:
        responses = [
            "Fard, lol",
            "Sale noe tahsili mobarak. Farde dige.",
            "Hafteye aval farde.",
            "It is fard pesaram/dokhtaram.",
        ]
        print_random_response(responses)
    else:
        is_odd = (diff // 7) % 2 == 0
        fard_zoj_str = "Fard" if is_odd else "Zoj"
        responses = [
            "Hafteye {}e.".format(fard_zoj_str),
            "{}.".format(fard_zoj_str),
            "Emruz hafteye {}e!".format(fard_zoj_str)
        ]
        print_random_response(responses)


if __name__ == "__main__":
    start_date = jdatetime.date(1399, 6, 22)  # for University of Tabriz
    main(start_date)
