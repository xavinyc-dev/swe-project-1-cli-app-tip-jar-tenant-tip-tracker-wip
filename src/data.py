from datetime import datetime

DATE_FORMAT = "%m-%d-%Y"


def validate_amnt(amnt):
    """Validates the amount before continuing"""
    try:
        amnt = float(amnt)
        return amnt >= 0
    except ValueError:
        return False


def validate_date(date):
    """Validates date is valid using datetime before continuing"""
    try:
        datetime.strptime(
            date, DATE_FORMAT
        )  # Checks if date can be turned into valid date
        return True
    except ValueError:
        return False


def validate_year(year):
    """Validate the year format"""
    try:
        datetime.strptime(year, "%Y")
        return True
    except ValueError:
        return False


def transform_date(date):
    """Transforms date into correct format to store"""
    date = (datetime.strptime(date, DATE_FORMAT)).strftime(DATE_FORMAT)
    return date


# def calc_this_year():
#     current_year = datetime.now().year
#     return current_year


def search_year(year, tips_jar):
    """Search The tips by year"""
    searched_year = [tip for tip in tips_jar if tip["Date"][-4:] == year]
    return searched_year


def return_date(tip):
    """Returns the date from the tip in date format"""
    date_text = tip["Date"]
    date = datetime.strptime(date_text, DATE_FORMAT)
    return date


def sort_date(selection, tips_jar):
    """Returns a copied sorted list by date"""
    if selection == 3:
        recent_to_furth = sorted(tips_jar, reverse=True, key=return_date)
        return recent_to_furth
    elif selection == 4:
        furth_to_recent = sorted(tips_jar, key=return_date)
        return furth_to_recent


def return_amount(tip):
    """Returns the amount value from the tip"""
    amnt = tip["Amount"]
    return amnt


def sort_amount(selection, tips_jar):
    """Sorts the amount of tips from high to low or low to high"""
    if selection == 1:
        high_to_low = sorted(tips_jar, reverse=True, key=return_amount)
        return high_to_low
    elif selection == 2:
        low_to_high = sorted(tips_jar, key=return_amount)
        return low_to_high


def total_tips_math(tips_jar):
    """Adds each value in Amount of each tip in a list and sums it up"""
    tips_total = [tip["Amount"] for tip in tips_jar]
    total = sum(tips_total)
    return total


def return_tip_from_id(wanted_id, tips_jar):
    """Returns the dictionary with the matching ID or None if cant find it"""
    for tip in tips_jar:
        if tip["ID"] == wanted_id:
            return tip
    return None


def remove_tip(wanted_id, tips_jar):
    """Removes tip(dictionary) from list tips_jar with matching ID"""
    tip = return_tip_from_id(wanted_id, tips_jar)
    tips_jar.remove(tip)
    return tips_jar


def build_tip(tip_id, tenant, apt, amnt, tip_type, desc, date):
    """Builds one tip dictionary and cleans the strings, date and amnt were cleaned on input to verify"""
    apt = clean_apartment(apt)
    tenant = clean_tenant(tenant)
    tip_type = clean_type(tip_type)
    desc = clean_description(desc)
    tip = {
        "ID": tip_id,
        "Date": date,
        "Apartment": apt,
        "Tenant": tenant,
        "Amount": amnt,
        "Tip Type": tip_type,
        "Description": desc,
    }

    return tip


def clean_tenant(tenant):
    """Cleaned the tenant input by stripping white space and using title"""
    cleaned_tenant = tenant.strip().title()
    return cleaned_tenant


def clean_type(tip_type):
    """Cleaned the tip_type input stripping white space and title"""
    cleaned_type = tip_type.strip().title()
    return cleaned_type


def clean_apartment(apt):
    """Cleaning the apartment input, all uppercase and stripping white space"""
    cleaned_apartment = apt.strip().upper()
    return cleaned_apartment


def clean_description(desc):
    """Cleaning description stripping white space"""
    cleaned_description = desc.strip()
    return cleaned_description
