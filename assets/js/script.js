$(function () {

    var container = $('#pagination-demo');

    var sources  = [];
    if(document.getElementById("browsers") != "null"){
        $.each(document.getElementById("browsers").options, function (index, value) {
            sources.push(value.value);
        }); 
    }
    
    var options = {
        dataSource: sources,
        pageSize: 1,
        totalNumber: 4,
        callback: function (response, pagination) {
            $.each(sources, function (index, value) {
                if(value == response[0]){
                    document.getElementById(value).style.display = 'block';
                }
                else{
                    document.getElementById(value).style.display = 'none';
                }
            }); 

        }
    };
    container.pagination(options);
    return container;
});