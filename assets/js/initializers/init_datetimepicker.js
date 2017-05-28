require('eonasdan-bootstrap-datetimepicker');

const dateTimePickerInit = (selector = '.datetimeinput') => {
    $(selector).datetimepicker({
	showTodayButton: true,
	format: 'YYYY-MM-DD HH:mm'
    });
};

$(() => {
    dateTimePickerInit();
});
