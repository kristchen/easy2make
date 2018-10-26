$("#cliente").autocomplete({
source:function(request, response){
    $.ajax({
        type:'POST',
        headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
        url: "/clientes/",
        data:{'nome' : request.term}
    }).done(function(data){
        
        response($.map(data.cliente_list, function(item){
            return{
                label: item.nome,
                id: item.id,
                cliente : item
            }
        }));
    });
},

select:function(event, ui){
    var cliente = ui.item.cliente;

    var $tr = $("<tr/>");
    var $td = $("<td/>");
    var $i = $("<i/>").addClass('fa fa-trash cliente-remove').css('cursor','pointer');
    
    $tr.append($td.clone().append(cliente.nome))
        .append($td.clone().append(cliente.telefone))
        .append($td.clone().css('text-align','right').append($i))
        .appendTo($("#tbody-cliente"));
    
    $("#cliente").val("").attr('readonly', true);

    $.ajax({
        type:'POST',
        headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
        url:'/vendas/adicionar/',
        accept:'application/json',
        data:{'cliente':cliente.id}
        }).done(function(response){
            $("#id_venda").val(response.id);
            $("#descricao").attr('readonly', false);
        });

},
    
});

$("#descricao").autocomplete({
    source:function(request, response){
        $.ajax({
            type:'POST',
            headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
            url: "/estoque/produtos/",
            data:{'descricao' : request.term}
        }).done(function(data){
            
            response($.map(data.produto_list, function(item){
                return{
                    label: item.descricao,
                    id: item.id,
                    produto:item
                }
            }));
        });
    },
    
    select:function(event, ui){
        
        var produto = ui.item.produto;
        var $select = $("<select/>").addClass('form-control');
        var $option = $("<option/>");
        var $tr = $("<tr/>");
        var $td = $("<td/>");
        var $i = $("<i/>").addClass('fa fa-trash produto-remove').css('cursor','pointer');
        
        for(var i = 1; i <= produto.quantidade; i++){
            $option.clone().append(i).val(i).appendTo($select);
        }

        if(produto.quantidade > 0){
            $tr.append($td.clone().append(produto.descricao))
                .append($td.clone().append(produto.preco))
                .append($td.clone().attr('estoque', produto.quantidade).append(--produto.quantidade))
                .append($td.clone().append($select))
                .append($td.clone().css('text-align','right').append($i))
                .appendTo($("#tbody-produto"));
    
            $.ajax({
                type:'POST',
                headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
                url:'/vendas/itens/adicionar/',
                accept:'application/json',
                data:{'venda':$("#id_venda").val(), 'produto':produto.id, 'quantidade':1}
            }).done(function(response){
                $tr.attr('id', response.id);
                $("#descricao").val("");
            });

            atualizarTotal();

        }else {
            $("<div class='alert alert-danger' title='Cadastrar item'>Produto não disponível no momento</div>").dialog();
        }


    },
        
});

$(document).ready(function(){
    
    $('#tbody-produto').on('click', '.produto-remove', function(){
        var id = $(this).parents().eq(1).attr('id');
        
        $.ajax({
            type:'POST',
            headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
            url:'/vendas/itens/remover/'+id+'/',
            accept:'application/json',
        });
        
        $(this).parents().eq(1).remove();
        
        atualizarTotal();
    });

    $('#tbody-cliente').on('click', '.cliente-remove', function(){
        var id = $("#id_venda").val();
        
        $.ajax({
            type:'POST',
            headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
            url:'/vendas/remover/'+id+'/',
            accept:'application/json',
        });
        
        $(this).parents().eq(1).remove();
        $("#cliente").removeAttr('readonly');
        $('#tbody-produto').children().remove();
        $("#descricao").attr('readonly', false);                
    });

    $('#tbody-produto').on('change', 'select', function(){
        
        var quantidadeAtual = $(this).val();
        var id = $(this).parents().eq(1).attr('id');

        $.ajax({
            type:'POST',
            headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
            url:'/vendas/itens/alterar/'+id+'/',
            data:{'quantidade':quantidadeAtual},
            accept:'application/json',
        });

        atualizarTotal();

    });


    $("#btn-finalizar").click(function(){
        var id = $("#id_venda").val();
        $.ajax({
            type:'POST',
            headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
            url:'/vendas/alterar/'+id+'/',
            accept:'application/json',
        }).done(function(){

            $(".fa-trash").remove();
            $('select').attr('disabled',true);
            $("#tbody-produto tr td:nth-child(3)").text('');
            $("#btn-finalizar").hide();
            $("#btn-cupom").show();

        });
    });

    $("#btn-cupom").click(function(){
        var id = $("#id_venda").val();
        
        $.ajax({
            type:'GET',
            headers: {'X-CSRFToken':$("input[name=csrfmiddlewaretoken]").val()},
            url:'/vendas/'+id+'/cupom/',
            accept:'application/json'
            }).done(function(response){
            
                var $print = $("<div/>");
                $print.html(response);
                $print.printThis();
        });

    });

});

function atualizarTotal(){

    var total = 0;

    $("#tbody-produto tr").each(function(event){
        
        var valor = parseFloat($(this).children(':nth-child(2)').text());
        var quantidade = parseInt($(this).children(':nth-child(4)').find('select').val()); 
        var estoque = parseInt($(this).children(':nth-child(3)').attr('estoque'));
        $(this).children(':nth-child(3)').text(estoque - quantidade);
        total += parseFloat((valor * quantidade).toFixed(2));
        
    });

    var text = total == 0 ? '0.00' : total;
    $("#total").text("Total: R$ "+ text);

}