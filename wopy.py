#!/usr/bin/python3
import colorama
import sys

colorama.init(autoreset=True)


# word dicts
edge_font = {
        'a' : [' ██         ', ' █ █        ', ' █▄▄█       ', ' █  █       ', '    █       ', '   █        ', '  ▀         '],
        'b' : [' ███        ', ' █  █       ', ' █ ▀ ▄      ', ' █  ▄▀      ', ' ███        ', '            ', '            '],
        'c' : [' ▄█▄        ', ' █▀ ▀▄      ', ' █   ▀      ', ' █▄  ▄▀     ', ' ▀███▀      ', '            ', '            '],
        'd' : [' ██▄        ', ' █  █       ', ' █   █      ', ' █  █       ', ' ███▀       ', '            ', '            '],
        'e' : [' ▄███▄      ', ' █▀   ▀     ', ' ██▄▄       ', ' █▄   ▄▀    ', ' ▀███▀      ', '            ', '            '],
        'f' : [' ▄████      ', ' █▀   ▀     ', ' █▀▀        ', ' █          ', '  █         ', '   ▀        ', '            '],
        'g' : ['   ▄▀       ', ' ▄▀         ', ' █ ▀▄       ', ' █   █      ', '  ███       ', '            ', '            '],
        'h' : ['  ▄  █      ', ' █   █      ', ' ██▀▀█      ', ' █   █      ', '    █       ', '   ▀        ', '            '],
        'i' : [' ▄█         ', ' ██         ', ' ██         ', ' ▐█         ', '  ▐         ', '            ', '            '],
        'j' : ['   ▄▄▄▄▄    ', ' ▄▀  █      ', '     █      ', '  ▄ █       ', '   ▀        ', '            ', '            '],
        'k' : [' █  █▀      ', ' █▄█        ', ' █▀▄        ', ' █  █       ', '   █        ', '  ▀         ', '            '],
        'l' : [' █          ', ' █          ', ' █          ', ' ███▄       ', '     ▀      ', '            ', '            '],
        'm' : [' █▀▄▀█      ', ' █ █ █      ', ' █ ▄ █      ', ' █   █      ', '    █       ', '   ▀        ', '            '],
        'n' : ['    ▄       ', '     █      ', ' ██   █     ', ' █ █  █     ', ' █  █ █     ', ' █   ██     ', '            '],
        'o' : [' ████▄      ', ' █   █      ', ' █   █      ', ' ▀████      ', '            ', '            ', '            '],
        'p' : [' █ ▄▄       ', ' █   █      ', ' █▀▀▀       ', ' █          ', '  █         ', '   ▀        ', '            '],
        'q' : ['  ▄▄ █      ', ' █   █      ', '  ▀▀▀█      ', '     █      ', '      █     ', '       ▀    ', '            '],
        'r' : [' █▄▄▄▄      ', ' █  ▄▀      ', ' █▀▀▌       ', ' █  █       ', '   █        ', '  ▀         ', '            '],
        's' : ['    ▄▄▄▄▄   ', '   █     ▀▄ ', ' ▄  ▀▀▀▀▄   ', '  ▀▄▄▄▄▀    ', '            ', '            ', '            '],
        't' : ['    ▄▄▄▄▀   ', ' ▀▀▀ █      ', '     █      ', '    █       ', '   ▀        ', '            ', '            '],
        'u' : ['   ▄        ', '    █       ', ' █   █      ', ' █   █      ', ' █▄ ▄█      ', '  ▀▀▀       ', '            '],
        'v' : ['     ▄      ', '      █     ', ' █     █    ', '  █    █    ', '   █  █     ', '    █▐      ', '    ▐       '],
        'w' : ['   ▄ ▄      ', '  █   █     ', ' █ ▄   █    ', ' █  █  █    ', '  █ █ █     ', '   ▀ ▀      ', '            '],
        'y' : [' ▀▄    ▄    ', '   █  █     ', '    ▀█      ', '    █       ', '  ▄▀        ', '            ', '            '],
        'z' : ['  ▄▄▄▄▄▄    ', ' ▀   ▄▄▀    ', '  ▄▀▀   ▄▀  ', '  ▀▀▀▀▀▀    ', '            ', '            ', '            ']

        }


description = '''Ascii art generator
Usage:
    script_name 'your text'
    script_name 'your text' -flag [OPTION]...

Flags:
    -v  |  --version              Print current version
    -h  |  --help                 Print this information
    -f  |  --font [OPTION]        Chose the need of font
    -C  |  --center               Set the text at the center of the terminal
    -c  |  --color [OPTION]       Set the colour for the text
    -r  |  --random               The random choose the font and colour
    -F  |  --font-list            Print exists fonts
    -cc |  --colors-list          Print exists colors

'''


# current version
version = 'wopy v0.1'


# exists fonts
font_list = ['edge font']


# exists colors
colors_list = ['green', 'red', 'blue', 'yellow']


# simple tests
def tests():
    for key, value in edge_font.items():
        print(value)


def main():
    user_input = sys.argv[1]
    user_text = sys.argv[2]
    user_flags = sys.argv[3:]
    

    # Output description
    match user_input:

        case '-h' | '--help':
            print(description)
            return


        case '-v' | '--version':
            print(version)
            return

        
        case '-F' | '--font-list':
            for font in font_list:
                print(font)    
            return


        case '-cc' | '--colors-list':
            for color in colors_list:
                print(color)
            return


    for i in user_text:
        print(edge_font[i], end='')   


if __name__ == '__main__':
    main()

else:
    tests()
