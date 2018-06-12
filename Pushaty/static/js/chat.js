// the following ajax call collects information from the form

$('#chat-form').on('submit',function(event){
    event.preventDefault();

    $.ajax({
        url:'/post/',
        type: 'POST',
        data: {msgbox: $('#chat-msg').val()},

        success:function(json){
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="text-right list-group-item">'+json.msg+'</li>');
            var chatlist = document.getElementById('msg-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
        }
    });
});

// this function gets all the chat messages objects
function getMessages(){
    if(!scrolling){
        $.get('/messages',function(messages){
            $('#msg-list').html(messages);
            var chatlist = document.getElementById('msg-list-div');
            chatlist.scrollTop = chatlist.scrollHeight()
        });
    }
    scrolling = false;
}


// this functions fetches any new messages after every 500 milliseconds
var scrolling = false;
$(function(){
    $('msg-list-div').on('scroll', function(){
        scrolling = true;
    })
    refreshTimer = setInterval(getMessages,500)
})

// the function below disables the send button whenever input field is empty

$(document).ready(function(){
    $('#send').attr('disabled','disabled');
    $('#chat-msg').keyup(function(){
        if($(this).val() != ''){
            $('#send').removeAttr('disabled');
        }
        else{
            $('#send').attr('disabled','disabled');
        }
    });
});