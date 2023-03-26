export function activ_or_unactiv_elements(class_button_open, class_list_activ, class_list_unactiv, class_buttons_close){
    let button_open = $('.'+class_button_open),
        buttons_close = $('.'+class_buttons_close),
        index;

    buttons_close.on('click', function(){
        index = $(this).attr('data-index');
        $('.'+class_list_activ+'[data-index="'+index+'"]').addClass('hidden');
        $('.'+class_list_unactiv+'[data-index="'+index+'"]').removeClass('hidden');
    });

    button_open.on('click', function(){
        index = $(this).attr('data-index');
        $('.'+class_list_activ+'[data-index="'+index+'"]').removeClass('hidden');
        $('.'+class_list_unactiv+'[data-index="'+index+'"]').addClass('hidden');
    });
};