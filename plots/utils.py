def lower_bound_float(data, bound):
    index_lower_bound = 1
    while data[index_lower_bound] < bound:
        index_lower_bound += 1

    # intrapolate to find exact lower_bound                                     
    # exact_lower_bound = (bound - c)/m,  m = slope,  c = y - m*x               
    m = (data[index_lower_bound] - data[index_lower_bound - 1])
    c = data[index_lower_bound] - m * index_lower_bound
    return (bound - c)/m


def lower_bound_float_integral(data, bound):
    index_lower_bound = 1
    while sum(data[:index_lower_bound]) < bound:
        index_lower_bound += 1

    # intrapolate to find exact lower_bound                                     
    # exact_lower_bound = (bound - c)/m,  m = slope,  c = y - m*x               
    m = (sum(data[:index_lower_bound]) - sum(data[:index_lower_bound - 1]))
    c = sum(data[:index_lower_bound]) - m * index_lower_bound
    return (bound - c)/m

def next_color():
    """ Cycling through plot data, return a different one on every invocation. Wrapping around when all colors are used. """
    if not hasattr(next_color, "current_color_index"):
        next_color.colors = ["y", "b", "g", "r", "c", "m", "k"]
        next_color.current_color_index = 0

    next_color.current_color_index += 1
    if next_color.current_color_index == len(next_color.colors):
        next_color.current_color_index = 0
    return next_color.colors[next_color.current_color_index]

next_color()

def reset_next_color():
    next_color.current_color_index = 0

