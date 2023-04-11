import {use_modal_window} from './modal_window.js';

//маска для поля номер телефона в форме заказать звонок
$("input[type='phone']").mask('+7 (999) 999-99-99');

let use_modal_window_menu = use_modal_window('modal_window_menu', 'close_modal_window_menu', 'open_modal_window_menu');


