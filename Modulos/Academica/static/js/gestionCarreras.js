(function(){
    const btnEliminar=document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
            const confirmacion=confirm('¿Seguro que desea eliminar esta carrera?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();