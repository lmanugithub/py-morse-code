import sys

CODE = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
    ' ':'-.-.-.-',
    ',':'--..--',
    ':':'---...',
    ';':'-.-.-.',
    '.':'.-.-.-',
    '"':'.-..-.',
    '(':'-----.',
    ')':'.-----',
    "'":'-.--.-',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}

def limpiado(mensaje):
    mensaje = mensaje.lower()
    mensaje_limpio = ""
    for char in mensaje:
        if char in CODE:
            mensaje_limpio += char

    return mensaje_limpio

def traductor(msg):
    limpio = limpiado(mensaje=msg)
    traduccion = ""
    for char in limpio:
        traduccion += CODE[char]
    return traduccion

def run():
    texto = str(sys.argv[1])
    print(traductor(texto))

if __name__=='__main__':
    run()