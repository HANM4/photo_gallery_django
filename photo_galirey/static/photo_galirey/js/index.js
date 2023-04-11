import {activ_or_unactiv_elements} from './interactive_list.js';
import {use_modal_window} from './modal_window.js';
import {auto_scroll} from './auto_scroll.js';


let list_services = activ_or_unactiv_elements('services_button_open', 'services_list_activ', 'services_list_unactiv', 'services_buttons_close');
let list_faq = activ_or_unactiv_elements('faq_button_open', 'faq_list_activ', 'faq_list_unactiv', 'faq_buttons_close');


let scroll_service = auto_scroll('scroll_service', 'button_scroll_service');


let use_modal_window_order_photo = use_modal_window('modal_window_order_photo', 'close_modal_window_order_photo', 'open_modal_window_order_photo', false, 'data-service');

$(document).on('submit','#form_order_service',function(e){
    e.preventDefault();
    let call = $("input[name='call']").val(); //call название поля в forms.py OrderServiceForm
    let service = $("#modal_window_order_photo").attr('data-service'); //service название поля в forms.py OrderServiceForm
    let name = $("input[name='name']").val(); //name название поля в forms.py OrderServiceForm
    let email = $("input[name='email']").val(); //email название поля в forms.py OrderServiceForm
    let message = $("textarea[name='message']").val(); //message название поля в forms.py OrderServiceForm
    console.log(call)
    console.log(service)
    console.log(name)
    console.log(email)
    console.log(message)

    const reg_call = new RegExp('\\+7 \\(\\d{3}\\) \\d{3}-\\d{2}-\\d{2}');
    const reg_email = new RegExp('[^а-яА-Я\\s]+@[^а-яА-Я\\s]+\\.[^а-яА-Я\\s]{2,}');
    if (reg_call.test(call) && service != '' && name != '' && reg_email.test(email)){
        $.ajax({
        type:'POST',
        data:
        {
            call:call,//call название поля в forms.py OrderServiceForm
            service:service,//service название поля в forms.py OrderServiceForm
            name:name,//name название поля в forms.py OrderServiceForm
            email:email,//email название поля в forms.py OrderServiceForm
            message:message,//message название поля в forms.py OrderServiceForm
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            let use_modal_window_order_photo_ok = use_modal_window('modal_window_order_photo_ok', 'close_modal_window_order_photo_ok');
        }
    });
    }else{
        alert("Введите правильное значение.");
    }

});