export function modal_window_use(class_button_open, id_modal_window, class_buttons_close, slider = false){
    class_button_open = $('.'+class_button_open);
    id_modal_window = $('#'+id_modal_window);
    class_buttons_close = $('.'+class_buttons_close);
    let slide_index_activate;

     class_buttons_close.on('click', function(){
        id_modal_window.addClass('hidden');
    });

    class_button_open.on('click', function(){
        id_modal_window.removeClass('hidden');
        if (slider){
            slide_index_activate = $(this).attr('data-idslid');
            id_modal_window.attr('data-idslidactiv', slide_index_activate);
        };
    });
};







