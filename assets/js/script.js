$(function () {

    var container = $('#pagination-demo');

    $.each(document.getElementById("browsers").options, function (index, value) {
        console.log(index);
        console.log(value.value);
    });    
    
    var sources  = ['1', '2', '3'];
    
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