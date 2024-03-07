""" Universal Chess Interface Parsing

Created by TJ on 3/6/2024
Last Modified: 3/6/2024
"""

def interpreter(inString):
    keywords = inString.split(' ')
    match keywords[0]:
        case None:
            return
        case 'uci':
            print('uci')
        case 'debug':
            print('debug')
        case 'isready':
            print('readyok')
        case 'setoption':
            print('setoption')
        case 'register':
            print('register')
        case 'ucinewgame':
            # Not useful unless the engine saves states from other games.
            print('ucinewgame')
        case 'position':
            print('position')
        case 'incheck':
            print('incheck')
        case 'getfen':
            print('getfen')
        case 'evaluate':
            print('evaluate')
        case 'makemove':
            print('makemove')
        case 'undomove':
            print('undomove')
        case 'nullmove':
            print('nullmove')
        case 'undonullmove':
            print('undonullmove')
        case 'isrepeated':
            print('isrepeated')
        case 'go':
            print('go')
        case 'stop':
            print('stop')
        case 'quit':
            print('quit')
        case _:
            print("Error in input.")

