/* global $, require */
require('eonasdan-bootstrap-datetimepicker');

const dateTimePickerInit = (selector = '.datetimeinput') => {
    $(selector).datetimepicker({
	showTodayButton: true,
	format: 'YYYY-MM-DD HH:mm'
    });
};

const datePickerInit = (selector = '.dateinput') => {
    $(selector).datetimepicker({
        showTodayButton: true,
        format: 'YYYY-MM-DD'
    })
}

$(() => {
    dateTimePickerInit()
    datePickerInit()
});
