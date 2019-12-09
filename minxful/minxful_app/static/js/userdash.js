$("#userPost").hide();
$("#comment").hide();

$("#yourPost").click(function () {
    $("#userPost").show();
    $("#comment").hide();
});

$("#yourcmt").click(function () {
    $("#userPost").hide();
    $("#comment").show();
});

$("#btnLogout").click(function(){
    location.href = '/';
});