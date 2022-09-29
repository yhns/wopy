#!/usr/bin/python3
import colorama
import sys

colorama.init(autoreset=True)


# word dicts
edge_font = {
        'a' : [' ██  ', ' █ █ ', ' █▄▄█', ' █  █', '    █', '   █ ', '  ▀  '],
        'b' : [' ███  ', ' █  █ ', ' █ ▀ ▄', ' █  ▄▀', ' ███  ', '      ', '      '],
        'c' : [' ▄█▄   ', ' █▀ ▀▄ ', ' █   ▀ ', ' █▄  ▄▀', ' ▀███▀ ', '       ', '       '],
        'd' : [' ██▄  ', ' █  █ ', ' █   █', ' █  █ ', ' ███▀ ', '      ', '      '],
        'e' : [' ▄███▄  ', ' █▀   ▀ ', ' ██▄▄   ', ' █▄   ▄▀', ' ▀███▀  ', '        ', '        '],
        'f' : [' ▄████ ', ' █▀   ▀', ' █▀▀   ', ' █     ', '  █    ', '   ▀   ', '       '],
        'g' : ['   ▄▀ ', ' ▄▀   ', ' █ ▀▄ ', ' █   █', '  ███ ', '      ', '      '],
        'h' : ['  ▄  █', ' █   █', ' ██▀▀█', ' █   █', '    █ ', '   ▀  ', '      '],
        'i' : [' ▄█', ' ██', ' ██', ' ▐█', '  ▐', '   ', '   '],
        'j' : ['   ▄▄▄▄▄', ' ▄▀  █  ', '     █  ', '  ▄ █   ', '   ▀    ', '        ', '        '],
        'k' : [' █  █▀', ' █▄█  ', ' █▀▄  ', ' █  █ ', '   █  ', '  ▀   ', '      '],
        'l' : [' █    ', ' █    ', ' █    ', ' ███▄ ', '     ▀', '      ', '      '],
        'm' : [' █▀▄▀█', ' █ █ █', ' █ ▄ █', ' █   █', '    █ ', '   ▀  ', '      '],
        'n' : ['    ▄  ', '     █ ', ' ██   █', ' █ █  █', ' █  █ █', ' █   ██', '       '],
        'o' : [' ████▄', ' █   █', ' █   █', ' ▀████', '      ', '      ', '      '],
        'p' : [' █ ▄▄ ', ' █   █', ' █▀▀▀ ', ' █    ', '  █   ', '   ▀  ', '      '],
        'q' : ['  ▄▄ █  ', ' █   █  ', '  ▀▀▀█  ', '     █  ', '      █ ', '       ▀', '        '],
        'r' : [' █▄▄▄▄', ' █  ▄▀', ' █▀▀▌ ', ' █  █ ', '   █  ', '  ▀   ', '      '],
        's' : ['    ▄▄▄▄▄  ', '   █     ▀▄', ' ▄  ▀▀▀▀▄  ', '  ▀▄▄▄▄▀   ', '           ', '           ', '           '],
        't' : ['    ▄▄▄▄▀', ' ▀▀▀ █   ', '     █   ', '    █    ', '   ▀     ', '         ', '         '],
        'u' : ['   ▄  ', '    █ ', ' █   █', ' █   █', ' █▄ ▄█', '  ▀▀▀ ', '      '],
        'v' : ['     ▄  ', '      █ ', ' █     █', '  █    █', '   █  █ ', '    █▐  ', '    ▐   '],
        'w' : ['   ▄ ▄  ', '  █   █ ', ' █ ▄   █', ' █  █  █', '  █ █ █ ', '   ▀ ▀  ', '        '],
        'y' : [' ▀▄    ▄', '   █  █ ', '    ▀█  ', '    █   ', '  ▄▀    ', '        ', '        '],
        'z' : ['  ▄▄▄▄▄▄  ', ' ▀   ▄▄▀  ', '  ▄▀▀   ▄▀', '  ▀▀▀▀▀▀  ', '          ', '          ', '          ']
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
    -r  |  --random               The random choose the font and color
    -R  |  --random-color-letters Random color for letters
    -F  |  --font-list            Print exists fonts
    -cc |  --colors-list          Print exists colors
    
'''


# current version
version = 'wopy v0.2'


# exists fonts
font_list = ['edge font']


# exists colors
colors_dict = {
        0 : 'white',
        1 : 'green',
        2 : 'red',
        3 : 'blue',
        4 : 'yellow',
        5 : 'black',

        }


# simple tests
def tests():
    for key, value in edge_font.items():
        print(value)


def main():
    user_input = sys.argv[0]
    user_text = sys.argv[1]
    user_flags = sys.argv[2:]
    

    # Output description
    match user_text:

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
 
    if not user_flags:
        render_text(user_text=user_text)

    i = 0
    print(user_flags)
    while i < len(user_flags):
        for flag in user_flags:
            if flag == '-c' or flag == '--color':
                i += 2
                print(user_text)
                print(f'color is: {colors_dict[int(user_flags[user_flags.index(flag) + 1])]}')
                render_text(user_text=user_text, color_id=int(user_flags[user_flags.index(flag) + 1]))


def render_text(user_text='', color_id=0, font_id=0, center_text=False, random=False, random_letters=False):
    print()
    result = ''
    for i in range(0, len(edge_font['a'])):
        for j in user_text:
            if j == ' ':
                result += '      '
            else:
                match color_id:

                    case 0:
                        result += f'{colorama.Fore.WHITE}{edge_font[j][i]}'

                    case 1:
                        result += f'{colorama.Fore.GREEN}{edge_font[j][i]}'

                    case 2:
                        result += f'{colorama.Fore.RED}{edge_font[j][i]}'

                    case 3:
                        result += f'{colorama.Fore.BLUE}{edge_font[j][i]}'

                    case 4:
                        result += f'{colorama.Fore.YELLOW}{edge_font[j][i]}'

                    case 5:
                        result += f'{colorama.Fore.BLACK}{edge_font[j][i]}'

        print(result)
        result = ''
    return



if __name__ == '__main__':
    main()
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2:])
else:
    tests()
