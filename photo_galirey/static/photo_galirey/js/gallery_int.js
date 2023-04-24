import {use_modal_window} from './modal_window.js';
import {use_slider, off_slider_manage} from './slider.js';

function assignment_index(class_slids){
    let slids = document.getElementsByClassName(class_slids);
    for (let i = 0; i < slids.length; i++) {
        slids[i].setAttribute('data-idslid',i);
    };
};

let slids = assignment_index('oneclick_open_slider');
let slider_modal_window = use_modal_window('slider', 'but_close_slider', 'oneclick_open_slider', true);

$('.oneclick_open_slider').on('click', function(){
    let slider_gallery = use_slider('slider_arrows_left', 'slider_arrows_right', 'slider_track', 'oneclick_open_slider', 'slider');
});

$('.but_close_slider').on('click', function(){
    off_slider_manage('slider_arrows_left', 'slider_arrows_right');
});



// обработчик отправки данных из формы WriteReviewForm на сервер
$(document).on('submit','#form_write_review',function(e){
    e.preventDefault();
    let name_reviewer = $("input[name='name_reviewer']").val(); //name_reviewer название поля в forms.py WriteReviewForm
    let social_networks = $("input[name='social_networks']").val(); //social_networks название поля в forms.py WriteReviewForm
    let review = $("textarea[name='review']").val(); //review название поля в forms.py WriteReviewForm
    let gallery = $("#form_write_review").attr('data-gallery'); //gallery название поля в forms.py WriteReviewForm
    console.log(name_reviewer)
    console.log(social_networks)
    console.log(review)
    console.log(gallery)

    if (name_reviewer != '' && social_networks != '' && review != '' && gallery != ''){
        $.ajax({
        type:'POST',
        data:
        {
            social_networks:social_networks,//social_networks название поля в forms.py WriteReviewForm
            name_reviewer:name_reviewer,//name_reviewer название поля в forms.py WriteReviewForm
            review:review,//review название поля в forms.py WriteReviewForm
            gallery:gallery,//gallery название поля в forms.py WriteReviewForm
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            let use_modal_window_send_review_ok = use_modal_window('modal_window_send_review_ok', 'close_modal_window_send_review_ok');
        }
    });
    }else{
        alert("Введите правильное значение.");
    }

});
