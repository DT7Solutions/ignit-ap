// Registration form

$(document).ready(function(){
    $('#register-button').click(function(){

        let firstname = $('#firstname').val()
        let lastname = $ ('#lastname').val()
        let email = $ ('#email').val()
        // let phone = $ ('#phone').val()
        let username = $ ('#username').val()
        let password = $ ('#password').val()
        let confirm_passw = $ ('#confirm_password').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()


        let data = new FormData()
        data.append("firstname", firstname),
        data.append("lastname", lastname),
        data.append("email", email),
        // data.append("phone", phone),
        data.append("username", username),
        data.append("password", password),
        data.append("confirm_password", confirm_passw),
        data.append("csrfmiddlewaretoken", csrfmiddlewaretoken)

        $.ajax({
            type:'POST',
            url:'/register/',
            processData:false,
            contentType:false,
            cache:false,
            data:data,

            success:function(data, xhr){
                $('#registration-form')[0].reset();
                if(xhr === 'success'){
                    window.location.href = '/';
                } else{

                }
                // alert("success, submitted data")
                // $('#success-message').html("Success: Data submitted successfully");
            },
            error:function(data){
                alert("fail, submitted data")
            }
        
        
        

        })
        

    })
})
