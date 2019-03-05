# Ejemplo Agenda Flask

## Pasos para instalar

1. Crear entorno virtual
```bash
python3 -m venv venv
```

1. Activar entorno virtual

En Linux:
```bash
source venv/bin/activate
```

En Windows:
```bash
venv\\Scripts\\activate
```

1. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar

```bash
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
