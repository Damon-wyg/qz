/**
 * Desc: 作为qz所有js执行入口
 * autor: qz-team
**/
$(document).ready(function() {
    navbar_reset();
    set_current_bar();
});

function navbar_reset() {
    $("ul#qz-navbar > li").each(function() {
        if ($(this).hasClass("active")) {
            $(this).removeClass("active");
        }
    });
}

function set_current_bar() {
    var path = window.location.pathname;
    var id = "";
    if (path == "/") {
        id = "index";
    } else if (/problems/.test(path)) {
        id = "problems";
    } else if (/introduct/.test(path)) {
        id = "introduct";
    } else if (/discuss/.test(path)) {
        id = "discuss";
    }
    (id != "") && $("#" + id).addClass("active");

    id = "";
    if (/algorithms/.test(path)) {
        id = "algorithms";
    } else if (/projects/.test(path)) {
        id = "projects"
    }
    (id != "") && $("#" + id).addClass("active");
}

