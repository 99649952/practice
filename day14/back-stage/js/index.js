/**
 * Created by Damin on 16-2-16.
 */
function Go(){
    var content = document.title;
    var firstChar = content.charAt(0)
    var sub = content.substring(1,content.length)
    document.title = sub + firstChar;
}
setInterval('Go()',1000);

$(function() {
    $('#main-menu>li>a').on('click', function() {
        if($(this).next('ul').is(':hidden')) {
            $(this).next('ul').addClass('in');
            $(this).parent('li').addClass('active')
        } else {
            $(this).next('ul').removeClass('in');
            $(this).parent('li').removeClass('active')
        }

        $(this).parent('li').siblings().removeClass('active').find('ul').removeClass('in');
    });

    $('#nav-icon').on('click', function() {
        $('#navbar-side').show();
    });

})
