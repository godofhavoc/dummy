$(document).ready(function(){

    var csrftoken = Cookies.get('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#location').geocomplete();

    if ($('#user_submit').text() == 'Add') {
        $('#add_nav').addClass('active');
    } else {
        $('#listing_nav').addClass('active');
    }

    $('#myTable').DataTable( {
        pageLength: 5,
    });

    $('#form_submit').submit(function(event){
        event.preventDefault();
        console.log('here');

        first_name = $('#first_name').val();
        last_name = $('#last_name').val();
        email = $('#email').val();
        mobile = $('#mobile').val();
        age = $('#age').val();
        dob = $('#dob').val();
        user_location = $('#location').val();

        data_dict = {
            first_name: first_name,
            last_name: last_name,
            email: email,
            mobile: mobile,
            age: age,
            dob: dob,
            user_location: user_location,
        }

        if ($('#user_submit').text() == 'Add') {
            url = '/add/';
        } else {
            url = window.location.pathname;
        }
        console.log(url)

        $.post(url, data_dict, function(data, status) {
            if (status == "success"){
                window.location = '/listing'
            } else {
                console.log('error');
            }
        });
    });
});
