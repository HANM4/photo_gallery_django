import {use_modal_window} from './modal_window.js';

let use_modal_window_address = use_modal_window('modal_window_address', 'close_modal_window_address', 'open_modal_window_address');

$(document).on('submit','#form_order_bell',function(e){
    e.preventDefault();
    let phone = $("input[name='call']").val(); //call название поля в forms.py OrderCallForm
    let name = $("input[name='name']").val(); //name название поля в forms.py OrderCallForm
    let message = $("textarea[name='message']").val(); //message название поля в forms.py OrderCallForm
    const reg = new RegExp('\\+7 \\(\\d{3}\\) \\d{3}-\\d{2}-\\d{2}');
    console.log(phone)
    console.log(name)
    console.log(message)
    if (reg.test(phone) && name != ''){
        $.ajax({
        type:'POST',
        data:
        {
            call:phone,//call название поля в forms.py OrderCallForm
            name:name,//name название поля в forms.py OrderCallForm
            message:message,//message название поля в forms.py OrderCallForm
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            let use_modal_window_order_bell_ok = use_modal_window('modal_window_order_bell_ok', 'close_modal_window_order_bell_ok');
        }
    });
    }else{
        alert("Введите правильное значение.");
    }

});