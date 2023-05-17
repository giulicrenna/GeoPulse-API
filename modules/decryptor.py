def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

key : list = ['S', 'E', 'H', 'K', '1', '2', 'J', 'M', 'Z', 'P', 'O', 'Y', '6', '5', '7', 'Q'] 

keymap : dict =  {'1' : key[0],
                  '2' : key[1],
                  '3' : key[2],
                  '4' : key[3],
                  '5' : key[4],
                  '6' : key[5],
                  '7' : key[6],
                  '8' : key[7],
                  '9' : key[8],
                  'E' : key[9],
                  'S' : key[10],
                  'P' : key[11],
                  'A' : key[12],
                  'D' : key[13],
                  '-' : key[14],
                  '0' : key[15]}


def decrypt(string : str) -> str:
    desencriptado : str = ""
    for char in string:
        desencriptado += get_key(char, keymap)
    return desencriptado
