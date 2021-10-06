for outside_counter in range(4):   # 0-3
    for inside_counter in range(5): # 0-4
        product = inside_counter * outside_counter
        print("{} x {} = {:2d}".
              format(outside_counter, inside_counter, product))