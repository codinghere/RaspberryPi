$(function () {
    var container = $('#pagination-demo');
    var sources = function () {
        var result = [];
        for (var i = 1; i < 196; i++) {
            result.push(i);
        }
        return result;
    }();
    
    var options = {
        dataSource: sources,
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