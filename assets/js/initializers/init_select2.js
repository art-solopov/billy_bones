require('select2');

const select2Init = (selector='select') => {
    $(selector).select2({theme: 'bootstrap'});
}

export default select2Init;

$(() => {
    select2Init();
});
