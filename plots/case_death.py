from utils import lower_bound_float, next_color, reset_next_color, Plot, differences

def plot_case_death(title, filename, normalization_fraction, deaths, cases):
    """ Plots cases and death each normalized to the first @normalization_fraction cases of the smallest total case count. Plot is saved as an png image to @filename ."""

    normalization_boundary_cases = normalization_fraction * cases[-1]
    normalization_boundary_deaths = normalization_fraction * deaths[-1]

    print "Using normalization point %.0f cases and %.0f death" % (normalization_boundary_cases, normalization_boundary_deaths)
    
    # create plot
    plot = Plot(title=title)

    # figure out the index where all greater indices account for 95% of the total cases (round up)
    start_index = int(lower_bound_float(deaths, 1) + 0.5)

    reset_next_color()

    normalization_offset_cases = lower_bound_float(cases, normalization_boundary_cases)
    normalization_offset_deaths = lower_bound_float(deaths, normalization_boundary_deaths)

    normalization_cases_to_deaths = sum(deaths[:int(normalization_offset_deaths)])/float(sum(cases[:int(normalization_offset_cases)]))

    print "Start Index: %d" % start_index
    print "normalization_offset_cases: %d" % normalization_offset_cases
    print "normalization_offset_deaths: %d" % normalization_offset_deaths

    # x-points
    cases_x = [idx - normalization_offset_cases for idx in range(len(cases))][start_index:]
    deaths_x = [idx - normalization_offset_deaths for idx in range(len(deaths))][start_index:]

    # y-points
    cases_y = [normalization_cases_to_deaths * x for x in cases[start_index:]]
    deaths_y = deaths[start_index:]

    format = next_color()
    plot.add_curve("Cases x %.2f" % normalization_cases_to_deaths,
                   cases_x, cases_y, format)

    format = next_color()
    plot.add_curve("Deaths", deaths_x, deaths_y, format)


    plot.xlabel = "Days since %d cases and %d deaths (%.0f%% of dataset)" % (normalization_boundary_cases, normalization_boundary_deaths, normalization_fraction)
    plot.save(filename)
    

