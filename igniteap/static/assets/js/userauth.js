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


//login form
$(document).ready(function(){
    $('#login-btn').click(function(){
        
        let username = $('#username').val()
        let password = $('#password').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        let data= new FormData()
        data.append('username',username),
        data.append('password',password),
        data.append("csrfmiddlewaretoken", csrfmiddlewaretoken)


        $.ajax({
            type:'POST',
            url:'/',
            processData:false,
            contentType:false,
            cache:false,
            data:data,


            success:function(data){
                $('#login-form')[0].reset();
                alert("success, submitted date")
            },
            error:function(data){
                alert("fail, submitted data")
            }
        })
    })
})



$(document).ready(function(){
    $('#student-btn').click(function(){

        let firstname = $('#firstname').val()
        let lastname = $('#lastname').val()
        let address = $('#address').val()
        let email = $('#email').val()
        let phone = $('#phone').val()
        let collegname = $('#collegename').val()
        let branchname = $('#branchname').val()
        let ideadescription = $('#ideadescription').val()
        let file = $('#pdfdocument')[0].files[0];
        let uploadurl = $('#uploadurl').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()


        let data = new FormData()
        data.append('firstname', firstname),
        data.append('lastname', lastname),
        data.append('address', address),
        data.append('email', email),
        data.append('phone', phone),
        data.append('collegname', collegname),
        data.append('branchname', branchname),
        data.append('ideadescription', ideadescription),
        data.append('pdfdocument', file),
        data.append('uploadurl', uploadurl),
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)

        $.ajax({
            type:'POST',
            url:'/ideaform/',
            processData:false,
            contentType:false,
            cache:false,
            mimeType:"multipart/form-data",
            data:data,


            success:function(data){
                $('#student-form')[0].reset();
                alert("Success, Submitted data")
            },

            error:function(data){
                alert("fail, Submitted data")
            }
        })

    })
})