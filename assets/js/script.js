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
        pageSize: 1,
        totalNumber: 4,
        callback: function (response, pagination) {
            console.log(response);
            console.log(pagination);
            var dataHtml = ' <div id="test" style="display: none;">';
            dataHtml += '<ol> {% for post in site.posts  reversed %}<li>';
            dataHtml += '<a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>';
            dataHtml += ' </li> {% endfor %}</ol></div>';
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