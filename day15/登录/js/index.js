$(function() {
    //左侧菜单展开
    $('#main-menu>li>a').on('click', function() {
    if($(this).next('ol').height() == 0) {
        $(this).next('ol').animate({
            'height': '120px'
        }, 'slow');
    } else {
        $(this).next('ol').animate({
            'height': '0'
        }, 'slow');
    }
    $(this).parent('li').siblings().find('ol').animate({
        'height': '0'
    }, 'slow');
    });

    //全选和取消全选
    $("#check_all").click(function(){
        if(this.checked){
            $("#table :checkbox").attr("checked", true);
            $(this).next().text('取消')
        }else{
            $("#table :checkbox").attr("checked", false);
            $(this).next().text('全选')
        }
    });

    //在单击列表中某个选项时，如果勾选的项刚好满足全部选中的条件，或全部不选中
    $("#table :checkbox").live('click', function(){
        allchk();
    });

    //检测全选框#all应该是选中状态还是未选中状态的
    function allchk(){
        console.log($('#table :checkbox:checked').parents('tr').length + ',' + $('#table tbody tr').length);
        if($("#table :checkbox:checked").parents('tr').length == $('#table tbody tr').length) {
            $("#check_all").attr("checked", true);
            $("#check_all").next('span').text('取消');
        } else {
            $("#check_all").attr("checked", false);
            $("#check_all").next('span').text('全选');
        }
    }

    //反选
    $("#reverse").click(function () {
        $("#table :checkbox").each(function () {
            $(this).attr("checked", !$(this).attr("checked"));
        });
        allchk()
    });

    //点击添加
    $('.add-btn').click(function() {
        var id_num = $('#table tbody tr').length;
        var str;
        str = '<tr class="tr-row" id="'+ (id_num+1) +'">';
        str += '<td><input type="checkbox" value="'+ (id_num+1) +'"></td>';
        str += '<td>'+ (id_num+1) +'</td>';
        str += '<td><input type="text" value="10.1.6.230" readonly="readonly" data-num="'+(id_num+1)+'"></td>';
        str += '<td><input type="text" value="10.1.6.1" readonly="readonly" data-num="'+(id_num+1)+'"></td>';
        str += '<td><input type="text" value="255.255.255.0" readonly="readonly" data-num="'+(id_num+1)+'"></td>';
        str += '<td><input type="button" value="编辑" readonly="readonly" class="num-editor-btn" data-num="true"></td>';
        $('#table tbody').append($(str));
    });

    /**点击删除
    $('.remove-btn').click(function() {
        if($('#check_all').attr('checked')) {
            $('#table tr td :checkbox:checked').each(function(index) {
                $('#'+this.value).remove();
            });
        } else {
            $(':checkbox:checked').each(function(index) {
                if(this.checked){
                    $('#'+this.value).remove();
                }
            })
        }
    })**/
    //点击删除
    $('.remove-btn').click(function() {
        $(this).parents('body').find("#table input:checked").parents('tr.tr-row').remove();
    });

    //点击编辑模式
    $('.editor-btn').click(function() {
        if($(this).parents('body').find('#table :checkbox').attr('checked')) {
            $(":checkbox:checked").parents("tr").find("input[type='text']").removeAttr('readonly');
            $(":checkbox:checked").parents("tr").find("input[type='text']").addClass('editor-input');
        }
    });

      //编辑选中复选框
    $('.num-editor-btn').live('click',function() {
        $(this).parents('tr.tr-row').find('input[type="text"]').removeAttr('readonly');
        $(this).parents('tr.tr-row').find(':checkbox').attr('checked',true);
    });

    //点击保存
    $('.save-btn').click(function() {
        $(":checkbox:checked").parents("tr").find("input[type='text']").attr('readonly', 'readonly');
        $(":checkbox:checked").removeAttr('checked');

    });

    //点击刷新
    $('.refresh-btn').click(function() {
        window.location.reload();
    })

});
