import includes from 'lodash/includes';

$(() => {
    let $form = $('form.bills-bill-form');
    if(!$form.length) return;

    let $tagsInput = $form.find('#id_tags');
    let $formGroup = $tagsInput.closest('.form-group');
    let tagsValue = $tagsInput.val().split(/,\s*/);

    $tagsInput.attr('type', 'hidden');
    $formGroup.find('#hint_id_tags').addClass('hidden');

    let $select = $('<select>');
    $select.addClass('form-control');
    $select.attr('multiple', true);

    $formGroup.append($select);
    $select.select2({tags: true, data: window.billTags});
    $select.val(tagsValue).trigger('change');

    $select.on('change', () => {
	$tagsInput.val($select.val().join(', '));
    });
});
