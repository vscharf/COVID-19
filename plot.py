import sys
import code
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

import data.csse
from plots.cumulative_data import plot_normalized_cumulative_data
from plots.death_rate import plot_normalized_death_rate

#plot_normalized_cumulative_data("cases", "de_it_us_es", 0.15, data.csse.get_cases("Germany"), data.csse.get_cases("Italy"), data.csse.get_cases("US"), data.csse.get_cases("Spain"))

#plot_normalized_cumulative_data("death", "de_it_us_es", 0.25, data.csse.get_deaths("Germany"), data.csse.get_deaths("Italy"), data.csse.get_deaths("US"), data.csse.get_deaths("Spain"))

plot_normalized_death_rate("death_rate", "us", 14, data.csse.get_cases("US"), data.csse.get_deaths("US"))
