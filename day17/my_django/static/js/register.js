$(function() {
    var user, password, repassword, telephone, code;
    var pass_reg = /^[a-zA-Z]\w{5,17}$/;
    var tele_reg = /^(13[0-9]|14[0-9]|15[0-9]|17[0-9]|18[0-9])\d{8}$/;
    $('#register_btn').on('click', isVerificationFn);

    function isVerificationFn() {
        user = $('#user').val();
        password = $('#password').val();
        repassword = $('#repeat_password').val();
        telephone = $('#telephone').val();
        code = $('#verification_code').val();


        if(!user) {
            isShowFn($('.user-tip'), '请填写用户名');
            return false;
        } else if(!password) {
            isShowFn($('.password-tip'), '请填写密码');
            return false;
        } else if(!pass_reg.test(password)) {
            isShowFn($('.password-tip'), '密码以字母开头，长度在6~18之间');
            return false;
        } else if(!repassword) {
            isShowFn($('.repassword-tip'), '请再次输入密码');
            return false;
        } else if(repassword != password) {
            isShowFn($('.repassword-tip'), '两次输入的密码不一致');
            return false;
        } else if(!telephone) {
            isShowFn($('.telephone-tip'), '请输入手机号');
            return false;
        } else if(!tele_reg.test(telephone)) {
            isShowFn($('.telephone-tip'), '请输入正确的手机号');
            return false;
        } else if(!code) {
            isShowFn($('.code-tip'), '请输入验证码');
            return false;
        }
    }



    $('#user').on('focus', function() {
        isHideFn($('.user-tip'));

    })

    $('#user').on('blur', function() {
        user = $('#user').val();
        if(!user) {
            isShowFn($('.user-tip'), '请输入用户名');
        } else {
            $.ajax({
                type: "POST",
                url: "/check_user_exit/",
                data: user,

            })
        }
    })

    $('#password').on('focus', function() {
        isHideFn($('.password-tip'));
    })

    $('#password').on('blur', function() {
        password = $('#password').val();
        if(!pass_reg.test(password)) {
            isShowFn($('.password-tip'), '密码以字母开头，长度在6~18之间');
        } else {
            isHideFn($('.password-tip'));
        }
    })

    $('#repeat_password').on('focus', function() {
        isHideFn($('.repassword-tip'));
    })

    $('#repeat_password').on('blur', function() {
        password = $('#password').val();
        repassword = $('#repeat_password').val();
        if(password != repassword) {
            isShowFn($('.repassword-tip'), '两次输入的密码不一致');
        } else {
            //$('.repassword-tip').css('visibility', 'hidden');
            isHideFn($('.repassword-tip'));
        }
    })

    $('#telephone').on('focus', function() {
        isHideFn($('.telephone-tip'));
    })

    $('#telephone').on('blur', function() {
        telephone = $('#telephone').val();
        if(!telephone) {
            isShowFn($('.telephone-tip'), '请输入手机号');
        } else if(!tele_reg.test(telephone)) {
            isShowFn($('.telephone-tip'), '请输入正确的手机号');
        } else {
            isHideFn($('.telephone-tip'));
        }
    })

    $('#verification_code').on('focus', function() {
        isHideFn($('.code-tip'));
    });

    $('#verification_code').on('blur', function() {
        code = $('#verification_code').val();
        if(!code) {
            isShowFn($('.code-tip'), '请输入验证码');
        } else {
            isHideFn($('.code-tip'));
        }

    });

    //点击验证码
    $('#yanzhenma').on('click', function() {
        telephone = $('#telephone').val();

        if(!telephone) {
            isShowFn($('.telephone-tip'), '请输入手机号');
        } else if(!tele_reg.test(telephone)) {
            isShowFn($('.telephone-tip'), '请输入正确的手机号');
        } else {
            isHideFn($('.telephone-tip'));
            getCodeFn();
        }
    });

    //错误提示  显示
    function isShowFn(ele, txt) {
        ele.text(txt).css('visibility', 'visible');
    }

    //错误提示   隐藏
    function isHideFn(ele) {
        ele.css('visibility', 'hidden');
    }

    //获取验证码
    function getCodeFn() {
        $('#yanzhenma_btn').addClass('yanzhengma-grey');
        $('#yanzhenma_btn').attr('disabled', 'disabled');
        var timer = null;
        $('#yanzhenma_btn').val(60 + '秒后重新获取');
        var yzm_val = parseInt($('#yanzhenma_btn').val());
        timer = setInterval(function() {
            yzm_val --;
            $('#yanzhenma_btn').val(yzm_val + '秒后重新获取');
            if(yzm_val == 0) {
                clearInterval(timer);
                $('#yanzhenma_btn').val('重新获取验证码');
                $('#yanzhenma_btn').removeClass('yanzhengma-grey');
            }
        }, 1000);
    }
})