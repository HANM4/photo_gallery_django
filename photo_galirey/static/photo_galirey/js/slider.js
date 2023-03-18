export function use_slider(id_button_arrow_left, id_button_arrow_right, id_slider_track, class_slids, id_slider_main, ){
    let button_arrow_left = $('#'+id_button_arrow_left),
        button_arrow_right = $('#'+id_button_arrow_right),
        slider_track = $('#'+id_slider_track),
        max_index = document.getElementsByClassName(class_slids).length - 1,
        slide_index = Number($('#'+id_slider_main).attr('data-idslidactiv')),
        transform_x = 0;

    console.log(slide_index);
    transform_x = -(transform_x + 100 * slide_index);
    console.log(transform_x);
    slider_track.css('transform', "translateX("  + transform_x + "%)");
    $('#indicator_index_activ').text(slide_index+1);
    $('#indicator_index_length').text(max_index+1);

    button_arrow_left.on('click', function(){
        if (slide_index > 0){
            console.log("<<<<<<");
            slide_index = slide_index - 1;
            transform_x = transform_x + 100;
            console.log(transform_x);
            slider_track.css('transform', "translateX("  + transform_x + "%)");
            console.log(slide_index);
            $('#indicator_index_activ').text(slide_index+1);
        };
    });


    button_arrow_right.on('click', function(){
        if (slide_index < max_index){
            console.log(">>>>>>>");
            slide_index = slide_index + 1;
            transform_x = transform_x - 100;
            console.log(transform_x);
            slider_track.css('transform', "translateX("  + transform_x + "%)");
            console.log(slide_index);
            $('#indicator_index_activ').text(slide_index+1);
        };

    });

};

export function off_slider_manage(id_button_arrow_left, id_button_arrow_right){
    let button_arrow_left = $('#'+id_button_arrow_left),
        button_arrow_right = $('#'+id_button_arrow_right);
    button_arrow_left.off("click");
    button_arrow_right.off("click");
};
