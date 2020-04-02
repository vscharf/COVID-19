import datetime
import inspect, os

# from https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
_MODULE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
_CSSE_DATA_PATH = os.path.join(_MODULE_PATH, "..", "csse_covid_19_data", "csse_covid_19_time_series")
_COUNTRY_INDEX   = 1
_FIRST_DAY_INDEX = 4

_days           = []
_case_data      = {}
_death_data     = {}
_recovered_data = {}

def _get_days(line):
    return line.split(',')[_FIRST_DAY_INDEX:]

def _clean_file(file):
    """ Cleans up the file before parsing. Returns an iterator of a list of lines  """
    for line in file:
        if "\"" in line:
            line = line.replace("\"Korea, South\"", "SouthKorea")
            yield line
        else:
            yield line


def _parse_file(filename):
    """ Returns a dicitionary that maps countery to a list of counts per day. """
    global _days
    result = {}
    with open(filename) as file:
        days = _get_days(file.next().strip())
        if not _days:
            _days = days
        else: # make sure that the files contain the same days
            if not len(days) == len(_days) or not all([day == _days[idx] for idx, day in enumerate(days)]):
                raise RuntimeError("File '%s' has different order of days than already opened file." % filename)

        for line in _clean_file(file):
            # only take data without any Province/State given
            if not line.startswith(","): continue
            data = line.strip().split(",")
            country = data[_COUNTRY_INDEX]
            if country in result:
                raise RuntimeError("Duplicated entry for country '%s' in file '%s'." % (country, filename))
            result[country] = map(int, data[_FIRST_DAY_INDEX:])
    return result


def _parse_cases():
    global _case_data
    filename = os.path.join(_CSSE_DATA_PATH, "time_series_covid19_confirmed_global.csv")
    _case_data = _parse_file(filename)


def _parse_deaths():
    global _death_data
    filename = os.path.join(_CSSE_DATA_PATH, "time_series_covid19_deaths_global.csv")
    _death_data = _parse_file(filename)


def _parse_recovered():
    global _recovered_data
    filename = os.path.join(_CSSE_DATA_PATH, "time_series_covid19_recovered_global.csv")
    _recovered_data = _parse_file(filename)


def get_days():
    """ Returns a list of days. Indexes are the same as for return data."""
    global _days
    if not _days:
        _parse_cases()
    return [datetime.datetime.strptime(day, "%m/%d/%y").date() for day in _days]


def get_cases(country):
    """ Returns a list of case count in @country per day. """
    if not _case_data:
        _parse_cases()
    return _case_data[country]


def get_deaths(country):
    """ Returns a list of death count in @country per day. """
    if not _death_data:
        _parse_deaths()
    return _death_data[country]


def get_recovered(country):
    """ Returns a list of recovery count in @country per day. """
    if not _recovered_data:
        _parse_recovered()
    return _recovered_data[country]
