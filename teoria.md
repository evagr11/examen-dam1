# Teoria

Realiza el examen directamente sobre el archivo!

Este examen solo muestra algunos conceptos al azar que me parecen importantes, hay muchos!

Intenta añadir código cuando lo necesites utilizando

```lenguaje
codigo
```

1. ¿Que diferencia una variable creada con `let` de una creada con `const`?
    `let`: Permite declarar variables cuyo valor puede cambiar posteriormente.
    `const`: Declara variables con un valor constante, lo que significa que no se puede reasignar después de su inicialización.

2. ¿Qué es un dato primitivo? ¿y un objeto?
    Dato primitivo: Son los valores que no tienen métodos ni propiedades. 
    Objeto: Es una estructura que puede tener propiedades y métodos.
```
let primitivo = "Hola"; // Primitivo
let objeto = { nombre: "Juan", edad: 25 }; // Objeto
```

2. ¿Qué diferencia hay entre `==` y `===`?
    `==`: Compara valores después de realizar una transformación implícita.
	`===`: Compara valores y tipos de dato sin transformación.

3. Analiza el siguiente código, ¿qué valor se mostrará en la consola?
```js
let a = 1;

function mi_funcion() {
    let a = 2;
}

mi_funcion();
console.log(a);
```
Imprimira en consola: 1
La variable a dentro de la función es una variable local debido al uso de let. Por lo tanto, no afecta la variable global a.

4. ¿Qué es el DOM? Explícalo brevemente.
    Es una interfaz que organiza el contenido de una pagina HTML , permitiendo a JavaScript interactuar y modificar su estructura, estilo y contenido

5. ¿Este código es correcto? Si no lo es, ¿por qué?
```js
const boton = document.querySelector('button');
function saluda() {
    console.log('Hola');
}
boton.addEventListener('click', saluda());
```
    En addEventListener, se esta llamando a la función saluda(), con parentesis lo que hace que se ejecute inmediatamente, lo correcto seria pasar la función sin parentesis, es decir:
```js
const boton = document.querySelector('button');
function saluda() {
    console.log('Hola');
}
boton.addEventListener('click', saluda);
```    

6. ¿Que formas de seleccionar elementos del DOM conoces? ¿Cuál es la diferencia entre ellas?
    `getElementById`: Selecciona un elemento por su id.
	`querySelector`: Selecciona el primer elemento que coincida con un selector CSS.
    `querySelectorAll`: Selecciona todos los elementos que coincidan con un selector CSS.
	`getElementsByClassName`: Selecciona elementos por su clase.
	`getElementsByTagName`: Selecciona elementos por su etiqueta HTML.

7. ¿Qué es un evento? ¿Qué formas conoces de crearlos?
    Un evento es la acción que ocurre en el navegador.
    Formas de crear eventos:
	`addEventListener`: Añadir un evento a un elemento.
    En el HTML directamente con atributos.

8. ¿Como se añade una libreria externa a un proyecto de JavaScript? Puedes usar p5 como referencia.
    Se utiliza la etiqueta <script> dentro del archivo HTML. Un ejemplo de p5 de los que hemos hecho en clase seria este
```js
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.11.1/p5.js"></script>
```

9. ¿Que es esto? `<meta charset="UTF-8">` ¿Por qué es importante?
    Es una etiqueta que define la codificación del documento HTML. Es importante para evitar problemas con acentos y caracteres especiales.

10. ¿Que es una función? Explica brevemente su sintaxis en el lenguaje que prefieras.
    Una función es un bloque de código que realiza una tarea específica.

```js
function prueba(valor1, valor2) {
    return valor1 + valor2;
}
let resultado = prueba(2, 3);
console.log(resultado); 
```
    En consola se imprimira el número 5