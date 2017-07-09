$(function () {
    var container = $('#pagination-demo');
    var sources  = $("#SSID").data("texts").split(',').map(JSON.parse);
    
    var options = {
        dataSource: sources,
        pageSize: 1,
        totalNumber: 4,
        callback: function (response, pagination) {
            console.log(response);
            console.log(pagination);
            var dataHtml = '<ul>';
            $.each(response, function (index, item) {
                dataHtml += '<li>' + item + '</li>';
            });
            dataHtml += '</ul>';

            $('#data-container').html(dataHtml);
        }
    };
            //$.pagination(container, options);
    container.addHook('beforeInit', function () {
        window.console && console.log('beforeInit...');
    });
    container.pagination(options);
    container.addHook('beforePageOnClick', function () {
        window.console && console.log('beforePageOnClick...');
                //return false
            });
    return container;
});