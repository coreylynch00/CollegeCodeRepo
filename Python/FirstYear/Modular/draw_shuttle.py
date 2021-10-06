# Corey Lynch - 13/092/2020

def draw_lines():
        print("-", " " * 10, "-")

def draw_last_lines():
        print("+", "-" * 10, "+")

def main():
        draw_last_lines()
        for k in range(3):
            draw_lines()
        draw_last_lines()

main()
main()
main()