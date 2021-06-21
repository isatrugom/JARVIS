$(function () {
        $('#data').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                data: {'action': 'searchdata'},
                dataSrc: ""
            },
            columns: [
                {"data": "nombre"},
                {"data": "impacto"},
                {"data": "timestamp"},
                {"data": "version"},
                {"data": "proveedor"},
                {"data": "fechaAdquisicion"},
                {"data": "fechaExpiracion"},
                {"data": "plugin"},
                {"data": "tipoSoftware"},
                {"data": "opciones"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    render: function (data, type, row){
                        var nombre = '<a href="/activos/activo/vulnerabilidades/'+row.id+'/">'+row.nombre+'</a>';
                        return nombre
                    }
                },
                {
                    targets: [2],
                    render: function (data, type, row){
                        var fecha = row.timestamp.split('-')[2].split('T')[0] + "-" + row.timestamp.split('-')[1] + "-" + row.timestamp.split('-')[0];
                        var hora = row.timestamp.split('T')[1].substring(0, 5);
                        return fecha + " " + hora
                    }
                },
                {
                    targets: [5],
                    render: function (data, type, row){
                        var fecha = row.fechaAdquisicion.split('-')[2].split('T')[0] + "-" + row.fechaAdquisicion.split('-')[1] + "-" + row.fechaAdquisicion.split('-')[0];
                        return fecha
                    }
                },
                {
                    targets: [6],
                    render: function (data, type, row){
                        if (row.fechaExpiracion){
                            var fecha = row.fechaExpiracion.split('-')[2].split('T')[0] + "-" + row.fechaExpiracion.split('-')[1] + "-" + row.fechaExpiracion.split('-')[0];
                            return fecha
                        }else{
                            return " "
                        }

                    }
                },
                {
                    targets: [9],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row){
                        var buttons = '<a href="/activos/software/editar/'+row.id+'/" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a>&nbsp';
                        buttons += '<a href="/activos/software/eliminar/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>&nbsp';
                        buttons += '<a href="#" type="button" class="btn btn-secondary btn-xs"><i class="fas fa-exclamation-triangle"></i></a>';
                        return buttons;
                    }
                }
            ],
            initComplete: function (settings, json){
            }
        });
});