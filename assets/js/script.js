$(function () {

    var container = $('#pagination-demo');

    var sources  = [];
    $.each(document.getElementById("browsers").options, function (index, value) {
        sources.push(value.value);
    }); 
    
    var options = {
        dataSource: sources,
        pageSize: 1,
        totalNumber: 4,
        callback: function (response, pagination) {
            console.log(response);
            console.log(pagination);
            var dataHtml = '';
            $.each(response, function (index, item) {
                dataHtml += '<a href="' + item + '">' + item + '</a>';
            });

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