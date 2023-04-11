export function auto_scroll(id_finish_scroll, class_buttons_scroll){
    let buttons_scroll = $('.'+class_buttons_scroll);
    buttons_scroll.on('click', function(){
        let finish_scroll = $('#'+id_finish_scroll),
            elem = $(document).find(finish_scroll);
        if(elem.length > 0) {
            let posY = elem.eq(0).offset().top;
            $('html, body').animate({
                scrollTop: posY
            }, 1000);
        }
        return false;
    });
};