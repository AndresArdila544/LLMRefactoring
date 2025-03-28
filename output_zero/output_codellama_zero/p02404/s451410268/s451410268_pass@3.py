def print_pattern(width, height):
    if width == height == 0:
        return
    top_row = '#' * width
    mid_rows = ['#.' * (width - 2) + '#\n'] * (height - 2)
    bot_row = '#' * width
    print(top_row + '\n'.join(mid_rows) + bot_row)