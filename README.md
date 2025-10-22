

---


# Microservicio de Calculo Factorial

Este proyecto implementa un microservicio en Flask que recibe un numero por URL y devuelve una respuesta JSON con:

- El numero recibido  
- Su factorial  
- Una etiqueta "par" o "impar" segun el resultado del factorial  

Ejemplo de respuesta:
```json
{
  "numero": 5,
  "factorial": 120,
  "paridad_factorial": "par"
}
````

---

## Ejecucion local (sin Docker)

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el servicio:

```bash
python app.py
```

Probar en navegador:

```bash
 http://localhost:8080/factorial/5
```

---

## Ejecucion con Docker

Construir la imagen:

```bash
docker build -t factorial-service:1.0 .
```

Ejecutar el contenedor:

```bash
docker run --rm -p 8080:8080 factorial-service:1.0
```

Probar:

```bash
 http://localhost:8080/factorial/7
```

---

## Estructura del proyecto

```
Parcial2/
app.py
requirements.txt
Dockerfile
.venv/
README.md
```

```

---

```


## Pregunta del parcial

Si el microsevicio debe comunicarse con otro el segundo microservicio que reciba haga la peticion y reciba resultados debria guardarlos en su propia
base de datos, el servicio principal manda los datos del numero mediante la peticion POST esto para poder mantener la independencia de los dos, cada uno
ejecutando su contenedor perimitiendo que la arquitectura sea modular y los datos persistentes aun que el sistema se reinicie 

En otras palabras uno calcula los resultados el otro realiza las peticiones y guarda en la base de datos 
