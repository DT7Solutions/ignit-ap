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

            success:function(data,status, xhr){
                $('#register-form')[0].reset();
                if(data.success === true){
                    window.location.href = '/studentideaform/';
                } else{
                    alert(data.error)
                    window.location.href ='/register/'
                }
            },
            error:function(data){
                alert("fail, submitted data")
            }
        })
    })
})


// login form
$(document).ready(function(){
   
    $('#login-btn').click(function(){
        let username = $('#username').val()
        let password = $('#password').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        let data = new FormData()
        data.append('u_name', username),
        data.append('ps_word', password),
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)


        $.ajax({
            type:'POST',
            url:'/login/',
            processData:false,
            contentType:false,
            cache:false,
            data:data,

            success:function(data){
                $('#login-form')[0].reset();
                if(data.success === true){
                    window.location.href = '/studentideaform/';
                } else{
                    alert(data.error)
                    window.location.href ='/login/'
                }
            },
            error:function(data){
                alert("Fail, submitted data");
            }
        })
    })

       


       
})




// student idea  registred data
$(document).ready(function(){
    $('#student-btn').submit(function(event){
        event.preventDefault();
        let firstname = $('#firstname').val()
        let lastname = $('#lastname').val()
        let address = $('#address').val()
        let email = $('#email').val()
        let phone = $('#phone').val()
        let collagename = $('#collegename').val()
        let branchname = $('#branchname').val()
        let ideadescription = $('#ideadescription').val()
        let uploadurl = $('#uploadurl').val()
        let file = $('#pdfdocument')[0].files[0]; 
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        let data = new FormData()
        data.append('firstname', firstname)
        data.append('lastname', lastname)
        data.append('address', address)
        data.append('email', email)
        data.append('phone', phone)
        data.append('collagename', collagename)
        data.append('branchname', branchname)
        data.append('ideadescription', ideadescription)
        data.append('uploadurl', uploadurl)
        data.append('pdfdocument', file)
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)

        $.ajax({
            type: 'POST',
            url: '/studentideaform/',
            processData: false,
            contentType: false,
            cache: false,
            mimeType: 'multipart/form-data',
            data: data,

            success:function(data, status,xhr){
                $('#student-btn')[0].reset();
                alert("data save sucessfully")
                // if(data.success === true){
                //     window.location.href = '/studentideaform/';
                // }else{
                //     window.location.href = '/'
                // }
            },
          
                // if(data.success === true){
                //     alert(data.message)
                //     // window.location.href = '/';
                // } else{
                //     alert("data does not save sucessfully")
                //     window.location.href ='/ideaform/'
                // }
            error:function(data){
                alert("data does not save sucessfully");
            }
        });
    });
});



// contact form====================================


//Contact page 
$(document).ready(function(){
    $('#contact-btn').submit(function(event){
        event.preventDefault();

        let firstname = $('#firstname').val()
        let lastname = $('#lastname').val()
        let email = $('#email').val()
        let phone = $('#phone').val()
        let message = $('#message').val()
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        let data = new FormData()
        data.append('firstname', firstname),
        data.append('lastname', lastname),
        data.append('email', email),
        data.append('phone', phone)
        data.append('message', message),
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)

        $.ajax({
            type:'POST',
            url:'/contact/',
            processData:false,
            contentType:false,
            cache:false,
            data:data,
            success:function(data, status,xhr){
                $('#contact-btn')[0].reset();
                if(data.success === true){
                    alert('Your Request submited sucessfully!')
                }else{
                    alert(data.error)
                    window.location.href = '/contact/'
                }
            },
            error:function(data){
                alert("fail, submitted data")
            }
           
        })
    })
})

// end contact form data=================================================
//  partners or colobrations=============================================


function yesnoCheck(checkbox) {
    if(checkbox.checked == true){
        document.getElementById("ifYes").style.display = "block";
    
       
        // document.getElementById("submit").removeAttribute("disabled");
    }else{
        // document.getElementById("submit").setAttribute("disabled", "disabled");
        document.getElementById("ifYes").style.display = "none";
   }
}

// student registred data
$(document).ready(function(){
    $('#collaborate-btn').submit(function(event){
        event.preventDefault();
        let firstname = $('#firstname').val()
        let lastname = $('#lastname').val()
        let email = $('#email').val()
        let phone = $('#phone').val()
        let barand = $('#brand').val()
        let industry = $('#industry').val()

        let Collaboration_Type = [];
        $('input[name="check"]:checked').each(function() {
            Collaboration_Type.push($(this).val());
        });
        
        let colbtype = '';
        if (Collaboration_Type.includes('Other')) {
            colbtype = $('#ifYes').val();
        } else {
            colbtype = Collaboration_Type.join(', ');
        }

        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
    
        

        let data = new FormData()
        data.append('firstname', firstname)
        data.append('lastname', lastname)
        data.append('email', email)
        data.append('phone', phone)
        data.append('barand', barand)
        data.append('industry', industry)
        data.append("Collaboration_Type",colbtype);
        data.append('csrfmiddlewaretoken', csrfmiddlewaretoken)

        $.ajax({
            type: 'POST',
            url: '/partners/',
            processData: false,
            contentType: false,
            cache: false,
            data: data,

            success:function(data, status,xhr){
                $('#collaborate-btn')[0].reset();
                if(data.success === true){
                    alert("Sucessfully submited your request!")
                }else{
                    window.location.href = '/partners/'
                }
            },
            error:function(data){
                alert("data does not save sucessfully");
            }
        });
    });
});



// end partners coloborations ==========================================

// start================ banner evetn timw and date 
function updateCountdown() {
    let eventdate_time = document.getElementById('eventdatetime');
    let mydate = eventdate_time.innerHTML;
   


var dateComponents = mydate.match(/(\w+)\. (\d+), (\d+), (\d+)/);


var monthAbbreviations = {
  'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
  'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
};

var month = monthAbbreviations[dateComponents[1]];
var day = parseInt(dateComponents[2]);
var year = parseInt(dateComponents[3]);
var hour = parseInt(dateComponents[4]);


var formattedDate = new Date(Date.UTC(year, month, day, hour, 0, 0, 0));


var options = { 
  year: 'numeric', 
  month: 'long', 
  day: 'numeric', 
  hour: '2-digit', 
  minute: '2-digit', 
  second: '2-digit', 
  timeZone: 'UTC'
};

var result = formattedDate.toLocaleDateString('en-US', options).replace(" at", "");

console.log(result);

    var countdownDate = new Date(result).getTime();
    var now = new Date().getTime();
    var timeRemaining = countdownDate - now;
  
    if (timeRemaining <= 0) {
      document.querySelector(".clock").innerHTML = "Countdown expired!";
      return;
    }
  
    var days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    var hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
  
    updateContainer(document.querySelector(".days"), days.toString());
    updateContainer(document.querySelector(".hours"), hours.toString());
    updateContainer(document.querySelector(".minutes"), minutes.toString());
    updateContainer(document.querySelector(".seconds"), seconds.toString());
  }
  
  function updateContainer(container, newTime) {
    var time = newTime.split("");
  
    if (time.length === 1) {
      time.unshift("0");
    }
  
    var first = container.firstElementChild;
    if (first.lastElementChild.textContent !== time[0]) {
      updateNumber(first, time[0]);
    }
  
    var last = container.lastElementChild;
    if (last.lastElementChild.textContent !== time[1]) {
      updateNumber(last, time[1]);
    }
  }
  
  function updateNumber(element, number) {
    var second = element.lastElementChild.cloneNode(true);
    second.textContent = number;
  
    element.appendChild(second);
    element.classList.add("move");
  
    setTimeout(function () {
      element.classList.remove("move");
    }, 990);
    setTimeout(function () {
      element.removeChild(element.firstElementChild);
    }, 990);
  }
  
  setInterval(updateCountdown, 1000);

  
//   end banner time date =========================================





// var mydate = 'Nov. 22, 2023, 6 a.m.';

// var dateComponents = mydate.match(/(\w+)\. (\d+), (\d+), (\d+)/);


// var monthAbbreviations = {
//   'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
//   'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
// };

// var month = monthAbbreviations[dateComponents[1]];
// var day = parseInt(dateComponents[2]);
// var year = parseInt(dateComponents[3]);
// var hour = parseInt(dateComponents[4]);

// var formattedDate = new Date(Date.UTC(year, month, day, hour, 0, 0, 0));


// var options = { 
//   year: 'numeric', 
//   month: 'long', 
//   day: 'numeric', 
//   hour: '2-digit', 
//   minute: '2-digit', 
//   second: '2-digit', 
//   timeZone: 'UTC'
// };

// var result = formattedDate.toLocaleDateString('en-US', options);

// console.log(result);






