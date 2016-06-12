$(function() {
    var user, password;
    var pass_reg = /^[a-zA-Z]\w{5,17}$/;

    $('#submit_btn').on('click', submitFn);

    function submitFn() {
        user = $('#user').val();
        password = $('#password').val();
        console.log(user)
        if(!user) {
            $('.user-tip').text('请填写姓名').css('visibility','visible');
            return false;
        } else if(!password) {
            $('.password-tip').text('请填写密码').css('visibility','visible');
            return false;
        } else {
            if(!pass_reg.test(password)) {
                $('.password-tip').text('请填写正确密码').css('visibility','visible');
                return false;
            }
        }
    }

    function keyUpFn() {
        $('#user').on('keyup', function() {
            $('.user-tip').css('visibility','hidden');
        });

        $('#password').on('keyup', function() {
            $('.password-tip').css('visibility','hidden');
        });
    }

    keyUpFn();
})