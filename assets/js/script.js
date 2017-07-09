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
            $.each(sources, function (index, value) {
                if(value== response[0]){
                    value.show();
                }
                else{
                    value.hide();
                }
            }); 

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