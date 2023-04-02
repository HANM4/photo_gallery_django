export function use_modal_window(id_modal_window, class_buttons_close, class_button_open = false, slider = false, data_name = false){
    if (class_button_open){
        class_button_open = $('.'+class_button_open);
    };
    id_modal_window = $('#'+id_modal_window);
    class_buttons_close = $('.'+class_buttons_close);
    let slide_index_activate;

     class_buttons_close.on('click', function(){
        id_modal_window.addClass('hidden');
    });

    if (class_button_open){
        class_button_open.on('click', function(){
        if (data_name){
            id_modal_window.attr(data_name, $(this).attr(data_name));
        };
        id_modal_window.removeClass('hidden');
        if (slider){
            slide_index_activate = $(this).attr('data-idslid');
            id_modal_window.attr('data-idslidactiv', slide_index_activate);
        };
        });
    }else{
        id_modal_window.removeClass('hidden');
    };
};







