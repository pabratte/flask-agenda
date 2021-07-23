# Ejemplo Agenda Flask

Ejemplo de una agenda de contactos simple desarrollada utilizando Flask. 

## Pasos para instalar

```bash
# crear entorno virtual
python3 -m venv venv

# activar entorno virtual
source venv/bin/activate

# instalar dependencias
pip install -r requirements.txt

# ejecutar
FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run
```

## Ejercicio

Modificar el archivo ```app.py``` comentando la siguiente línea:

```python
import agenda_mem as agenda
```
y descomentando la siguiente línea:

```python
#import agenda_db as agenda
```

Modificar el archivo ```agenda_db.py```:

* Modificar los datos para la conexión con la DB
* Prestar atención a los ```# TODO:```, escribir los comandos SQL para realizar las operaciones solicitadas 
