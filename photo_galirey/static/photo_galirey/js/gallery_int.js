import {modal_window_us} from './modal_window.js';
import {use_slider, off_slider_manage} from './slider.js';

function assignment_index(class_slids){
    let slids = document.getElementsByClassName(class_slids);
    for (let i = 0; i < slids.length; i++) {
        slids[i].setAttribute('data-idslid',i);
    };
};

let slids = assignment_index('oneclick_open_slider');
let slider_modal_window = modal_window_us('oneclick_open_slider', 'slider', 'oneclick_close_slider', true);

$('.oneclick_open_slider').on('click', function(){
    let slider_gallery = use_slider('slider_arrows_left', 'slider_arrows_right', 'slider_track', 'oneclick_open_slider', 'slider');
});

$('.oneclick_close_slider').on('click', function(){
    off_slider_manage('slider_arrows_left', 'slider_arrows_right');
});


