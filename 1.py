def formats(t):
    minutes = t // 600
    tens_of_sec = (t - minutes * 600) // 100
    seconds = ((t - minutes * 600) % 100) // 10
    millisec = (t - minutes * 600) % 10
    return str(minutes) + ':' + str(tens_of_sec) + str(seconds) + '.' + str(millisec)
