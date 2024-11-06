# Crea una función log que acepte cualquier número de
# argumentos y los imprima por pantalla en una misma
# línea. La línea debe empezar con el prefijo ‘LOG: ’.
# Modifica la función log para que usuario pueda
# especificar cualquier prefijo que desee.
# Modifica la función log para que el prefijo tenga el
# valor por defecto ‘LOG: ’.
# Modifica la función log para que el usuario pueda
# establecer tanto prefijo como separador entre
# argumentos. Ambos deben pasarse sólo por los
# nombres (no por posición) ‘sep’ y ‘prefix’. No hace
# falta que estos tengan valor por defecto.
# Modfica la función log para que ahora ‘sep’ y ‘prefix’
# tengan un valor por defecto.
# Modifica la función log para que acepte el siguiente
# diccionario. Recuerda que hay que pasarlo
# desempaquetándolo con la sintaxis de doble
# asterisco (**).

def log(*args):
    print('LOG',*args)
    log('Este', 'es', 'un', 'mensaje') #salida: LOG Este es un mensaje

#Permitir que el usuario especifique el prefijo
def log(prefix,*args):
    print(prefix, *args)
log('DEBUG:', 'Este', 'es', 'un', 'mensaje') #Salida: DEBUG: Este es un mensaje

#Prefijo con valor por defecto
def log(*args, prefix='LOG'):
    print(prefix, *args)
log('Este', 'es', 'un', 'mensaje') #salida: LOG Este es un mensaje
log('Este', 'es', 'un', 'mensaje', prefix='DEBUG:') #Salida: DEBUG: Este es un mensaje

#Permitir que el usuario establezca el prefijo y el separador(sin valores por defecto)
def log(*args, prefix, sep):
    print(prefix,sep.join(map(str, args)))
log('Este', 'es', 'un', 'mensaje', prefix='DEBUG:',sep='|') #Salida: DEBUG: Este|es|un|mensaje

#Valores por defecto para 'sep' y 'prefix':
def log(*args, prefix='LOG:', sep=' '):
    print(prefix, sep.join(map(str, args)))
log('Este', 'es', 'un', 'mensaje') #salida: LOG: Este es un mensaje
log('Este', 'es', 'un', 'mensaje', prefix='DEBUG:', sep='|') #Salida: DEBUG: Este|es|un|mensaje

#Aceptar un diccionario: asumiendo que se debe convertir el diccionario a una cadena de texto separada:
def log(prefix='LOG:', sep=' ', **kwargs):
    print(prefix, sep.join(f"{k}={v}" for k, v in kwargs.items()))
log(prefix='INFO:', sep=', ', a=1, b=2, c=3) #Salida: INFO: a=1, b=2, c=3
