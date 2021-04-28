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
                {"data": "numero"},
                {"data": "opciones"},
            ],
            columnDefs: [
                {
                    targets: [4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row){
                        var buttons = '<a href="/activos/puerto/editar/'+row.id+'/" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a>&nbsp';
                        buttons += '<a href="/activos/puerto/eliminar/'+row.id+'/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>&nbsp';
                        buttons += '<a href="#" type="button" class="btn btn-secondary btn-xs"><i class="fas fa-exclamation-triangle"></i></a>';
                        return buttons;
                    }
                }
            ],
            initComplete: function (settings, json){
            }
        });
});