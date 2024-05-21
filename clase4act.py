# actividad 1

texto1= 'gordon lanzo su curva&strawberry ha fallado por un pie!'
texto2= '-grito Joe Castiglione&dos pies - le corrigio'
texto3= 'Troop&strawberry menea la cabeza como disgustado...'
texto4= 'agrega el comentarista'

# Gordon lanzo su curva...
# -Strawberry ha fallado por un pie! -grito Joe Castiglione.
# -Dos pies le corrigio Troop.
# -Strawberry menea la cabeza como disgustado. -agrega el comentarista.

# Colocar los textos en una lista
textos = [texto1, texto2, texto3, texto4]

# Ordenar los textos alfabéticamente
textos_ordenados = sorted(textos)

# Formatear y mostrar los textos en el orden deseado
for texto in textos_ordenados:
    # Aplicar capitalización y formato según el texto
    if texto.startswith('Gordon'):
        texto = texto.capitalize() + '...'
    elif texto.startswith('-'):
        parts = texto.split('&')
        texto = parts[1].capitalize() + ' -' + parts[0].lower() + '.'
    elif 'pies le corrigio' in texto:
        texto = texto.replace('pies', 'pies ').capitalize() + ' Troop.'
    elif 'menea la cabeza' in texto:
        texto = texto.capitalize() + ' -agrega el comentarista.'

    # Imprimir el texto formateado
    print(texto)