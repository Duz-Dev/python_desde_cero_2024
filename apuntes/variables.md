# Variables

> Esto solo es un refuerzo de lo ya abordado en las clases. Cosulta el libro de aprende python (tema 3.1.2 - 3.1.3)

No existe una regla mágica que nos diga cuál es el nombre perfecto, pero podemos aplicar
el sentido común y, a través de la experiencia, ir detectando aquellos nombres que sean más
adecuados. En el ejemplo anterior, quizás podríamos descartar de principio la opción 1 y la
4 (por ser demasiado cortas o demasiado largas); nos quedaríamos con las otras dos. Si nos
fijamos bien, casi no hay mucha información adicional de la opción 3 con respecto a la 2. Así
que podríamos concluir que la opción 2 es válida para nuestras necesidades. En cualquier
caso esto dependerá siempre del contexto del problema que estemos tratando.
Como regla general:

- Usar nombres para variables (ejemplo article).
- Usar verbos para funciones (ejemplo get_article()).
- Usar adjetivos para booleanos (ejemplo available).


__Nota__: Hay que diferenciar la asignación en Python con la igualación en matemáticas. El
símbolo = lo hemos aprendido desde siempre como una equivalencia entre dos expresiones
algebraicas, sin embargo en Python nos indica una sentencia de asignación, del valor (en la
derecha) al nombre (en la izquierda)

Ya hemos visto asignaciones literales como esta:

```python
value = 150.44
```

Pero también es posible vincular una variable con otra:

```python
value = pesos
```
Solo debo aclarar que en este caso, la variable `pesos` debe de existir anteriormente con un valor asignado, si no daria error.

## Conocer el tipo de una variable
Para poder descubrir el tipo de un literal o una variable, Python nos ofrece la función `type()`.
Veamos algunos ejemplos de su uso:


```python
type(9)
#>>> int

type(12.11)
#>>>float

text="pablosgod"
type(text)
#>>>str
```
Apartir de aqui practica y aplica lo aprendido :D
<span>repositorio: https://github.com/Duz-Dev/python_class</span>