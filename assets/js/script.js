$(document).ready(function() {
    document.getElementById("pager").appendTo('body').pagination({
        items: 100,
        itemsOnPage: 10,
        cssStyle: 'light-theme'
    });
});