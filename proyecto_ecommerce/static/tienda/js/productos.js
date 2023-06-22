const renderProducto = (producto) => {
    html = `
    <div class="col mb-5">
        <div class="card h-100">
            <!-- Product image-->
            <img class="card-img-top" src="${producto.portada}" alt="${producto.nombre}" />
            <!-- Product details-->
            <div class="card-body p-4">
                <div class="text-center">
                    <!-- Product name-->
                    <h5 class="fw-bolder">${producto.nombre}</h5>
                    <!-- Product price-->
                    $ ${producto.precio}
                </div>
            </div>
            <!-- Product actions-->
            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="#">AGREGAR AL CARRITO</a></div>
            </div>
        </div>
    </div>    
        `;
        return html;
}
const divProductos = document.querySelector("#divProductos");

fetch('/api_productos')
    .then((response) => response.json())
    .then(data => {

        console.log(data);
        let productos = data.data;
        productos.forEach(producto => {
            let html = renderProducto(producto);
            divProductos.insertAdjacentHTML('beforeend', html);
            
        });
    });
