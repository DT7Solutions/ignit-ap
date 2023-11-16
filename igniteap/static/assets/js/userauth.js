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


// function updateCountdown() {
//     let eventdate_time = document.getElementById('eventdatetime');
//     let mydate = eventdate_time.innerHTML;
//     var originalDateString = mydate;
//     var cleanedDateString = originalDateString.replace('at ', '');
//     var originalDate = new Date(cleanedDateString.replace('.', '').replace('midnight', '00:00:00'));
//     var options = { month: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
//     var formattedDateString = originalDate.toLocaleString('en-US', options);
//     console.log(formattedDateString);

   
//     var countdownDate = new Date(formattedDateString).getTime();
//     var now = new Date().getTime();
//     var timeRemaining = countdownDate - now;
  
//     if (timeRemaining <= 0) {
//       document.querySelector(".clock").innerHTML = "Countdown expired!";
//       return;
//     }
  
//     var days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
//     var hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//     var minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
//     var seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
  
//     updateContainer(document.querySelector(".days"), days.toString());
//     updateContainer(document.querySelector(".hours"), hours.toString());
//     updateContainer(document.querySelector(".minutes"), minutes.toString());
//     updateContainer(document.querySelector(".seconds"), seconds.toString());
//   }
  
//   function updateContainer(container, newTime) {
//     var time = newTime.split("");
  
//     if (time.length === 1) {
//       time.unshift("0");
//     }
  
//     var first = container.firstElementChild;
//     if (first.lastElementChild.textContent !== time[0]) {
//       updateNumber(first, time[0]);
//     }
  
//     var last = container.lastElementChild;
//     if (last.lastElementChild.textContent !== time[1]) {
//       updateNumber(last, time[1]);
//     }
//   }
  
//   function updateNumber(element, number) {
//     var second = element.lastElementChild.cloneNode(true);
//     second.textContent = number;
  
//     element.appendChild(second);
//     element.classList.add("move");
  
//     setTimeout(function () {
//       element.classList.remove("move");
//     }, 990);
//     setTimeout(function () {
//       element.removeChild(element.firstElementChild);
//     }, 990);
//   }
  
//   setInterval(updateCountdown, 1000);



// function convertDateFormat(x) {
   
//     var parts = x.match(/(\w{3}) (\d{1,2}), (\d{4}), (\d{1,2}) (a\.m\.|p\.m\.)/);

//     if (parts) {
//         var monthAbbreviation = parts[1];
//         var day = parts[2];
//         var year = parts[3];
//         var hour = parts[4];
//         var amPm = parts[5];

       
//         var months = {
//             'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
//             'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
//         };
//         var month = months[monthAbbreviation];

       
//         if (amPm === 'p.m.' && hour < 12) {
//             hour = parseInt(hour) + 12;
//         } else if (amPm === 'a.m.' && hour == 12) {
//             hour = 0;
//         }

        
//         var date = new Date(year, month, day, hour);

        
//         var options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
//         var formattedDate = date.toLocaleDateString('en-US', options);

//         return formattedDate;
       
//     }

//     return null;
// }


// var x = "Nov 21, 2023, 6 a.m.";
// var y = convertDateFormat(x);

// console.log(y);







function updateCountdown() {
    let eventdate_time = document.getElementById('eventdatetime');
    let mydate = eventdate_time.innerHTML;

    // Attempt to parse the date string
    let originalDate = parseDateString(mydate);

    if (!originalDate || isNaN(originalDate.getTime())) {
        console.error('Error parsing date:', mydate);
        return;
    }

    var options = { month: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' };
    var formattedDateString = originalDate.toLocaleString('en-US', options);
    console.log(formattedDateString);

    var countdownDate = originalDate.getTime();
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

function parseDateString(dateString) {
    // Remove "at" and replace "midnight" with "00:00:00"
    var cleanedDateString = dateString.replace(' at ', ' ').replace('midnight', '00:00:00');
    
    // Try to parse the date string
    var parsedDate = new Date(cleanedDateString.replace('.', ''));
    
    return parsedDate;
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
