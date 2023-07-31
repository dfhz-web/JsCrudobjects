let valores = [];
let Campotabla = document.getElementById("tabla");

let persona = {
    AgregarDatos(nombre, apellido, edad) {
        let dato = { nombre, apellido, edad };
        valores.push(dato);
    }
};

document.getElementById("agregar").addEventListener("click", () => {
    persona.AgregarDatos(
        document.getElementById("nombre").value,
        document.getElementById("apellido").value,
        document.getElementById("edad").value
    );

    actualizarTabla();
});

Campotabla.addEventListener("dblclick", function (e) {
    // Verificar si el clic fue en una fila (tag <tr>)
    if (e.target.tagName.toLowerCase() === "td") {
        // Obtener la fila que contiene la celda en la que se hizo clic
        const row = e.target.parentElement;
        // Obtener el índice de la fila a eliminar
        const inde = Array.prototype.indexOf.call(row.parentElement.children, row);
        // Eliminar la fila del arreglo y actualizar la tabla
        valores.splice(inde, 1);
        actualizarTabla();
    }
});

function actualizarTabla() {



    // Limpiar la tabla
    Campotabla.innerHTML = "";

    // Insertar las filas actualizadas
    valores.forEach((valor, index) => {
        let v = `
        <tr id="fila-${index}">
            <td>${valor.nombre}</td>
            <td>${valor.apellido}</td>
            <td>${valor.edad}</td>
        </tr>
        `;

        Campotabla.insertRow(-1).innerHTML = v;

     
    });
}


