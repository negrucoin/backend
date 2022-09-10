$(document).ready(function() {
    $('.header__burger').click(function() {
        $('.header__burger,.header__menu').toggleClass('active');
        if ($('.user__menu').hasClass('active')) {
            $('body').removeClass('lock');
        }
        $('.user_button').html('<i class="fa-solid fa-user"></i>');
        $('.user_button,.user__menu').removeClass('active');

        if (document.documentElement.clientWidth < 993) {
            $('body').toggleClass('lock');
            $('.overlay').removeClass('active');
        } else {
            $('body').removeClass('lock');
            $('.overlay').removeClass('active');
        }
    });

    $('.user_button').click(function() {
        if ($('.header__menu').hasClass('active')) {
            $('body').removeClass('lock');
        }

        if ($('.user__menu').hasClass('active')) {
            $('.user_button').html('<i class="fa-solid fa-user"></i>');
        } else {
            $('.user_button').html('<i class="fa-solid fa-xmark"></i>');
        };

        $('.user_button,.user__menu').toggleClass('active');
        $('.header__burger,.header__menu').removeClass('active');

        if (document.documentElement.clientWidth < 993) {
            $('body').toggleClass('lock');
            $('.overlay').toggleClass('active');
        } else {
            $('body').removeClass('lock');
            $('.overlay').removeClass('active');
        }
    });

    $('.overlay').click(function() {
        $('body').removeClass('lock');
        $('.user_button').html('<i class="fa-solid fa-user"></i>');
        $('.user_button,.user__menu').toggleClass('active');
        $('.overlay').toggleClass('active');
        $('.header__burger,.header__menu').removeClass('active');
    });
});

var block = document.getElementById('block');
var wrap = document.getElementById('wrap');

jQuery(function($){
    $(document).mouseup(function(e){
        var div = $(".user__menu");
        var user_button = $(".user_button");
        var overlay = $(".overlay");
        if (div.hasClass('active')) {
            if ( !div.is(e.target) && div.has(e.target).length === 0
                && !user_button.is(e.target) && user_button.has(e.target).length === 0
                && !overlay.is(e.target) && overlay.has(e.target).length === 0 ) {
                $('.user_button').click()
            }
        }
    });
});