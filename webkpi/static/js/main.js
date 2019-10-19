$(function() {
    $('.table-filter').find('input, select').change(function() {
        $(this).parents('form').submit();
    })
});