// change to content tab
$('#folder')
.on('click', '.content-unit-dropdown', function(e){
    e.preventDefault()
    var unit = $(this).attr('data-unit');
    $('#folder-assessment').hide()
    $('.folder-content-unit').hide()
    $('#folder-content').show()
    $('#folder-content-'+ unit +'').show()
    $('#assessment-tab').removeClass('active')
    $('#content-tab').addClass('active')
});

// change to assessment tab
$('#folder')
.on('click', '#assessment-tab', function(e){
    e.preventDefault()
    $('.folder-content-unit').hide()
    $('#folder-content').hide()
    $('#folder-assessment').show()
    $('#assessment-tab').addClass('active')
    $('#content-tab').removeClass('active')
});

// submit timetable form using ajax
$("#assessments-form").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    $('#folder').show();
    //loading icon
    $('#folder').html('<div class="lds-ring-parent"><div class="lds-ring-child"><div class="lds-ring"><div></div><div></div><div></div><div></div></div><div class="lds-ring-text my-3">Loading ...</div></div></div>');
    scrollToLink( $('#folder'));
    var form = $(this);
    var url = form.attr('action');
    $.ajax({
           type: "POST",
           url: url,
           dataType: 'html',
           data: form.serialize(), // serializes the form's elements.

            // handle a successful response
            success : function(data) {
                $('#folder').html(data)
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
         });
});

// button to auto scroll down to form start
var DELAY_SCROLLING = 1000;  // animation time in ms

function scrollToLink(link) {
  selectLink = $(link);
  if ( selectLink.length ) {
    var top = selectLink.offset().top;
    $('body,html').stop().animate({scrollTop: top}, DELAY_SCROLLING);
  } else {
    console.log('The link is not found: ' + link);
  }
}


// $("#pdfbutton").click(function(e) {
//     e.preventDefault(); // avoid to execute the actual submit of the form.
//     var form = $(this);
//     var url = form.attr('action');
//     $.ajaxSetup({
//         headers: { "X-CSRFToken": getCookie("csrftoken")}
//     });
//     $.ajax({
//            type: "POST",
//            url: url,
//            dataType: 'pdf',

//             // handle a successful response
//             success : function(data) {
//                 console.log("Success lmao")
//             },

//             // handle a non-successful response
//             error : function(xhr,errmsg,err) {
//                 $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                     " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//                 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//             }
//          });
// });



// prevent automatic selection events across browsers (fixed Safari issue)
function pauseEvent(e){
    if(e.stopPropagation) e.stopPropagation();
    if(e.preventDefault) e.preventDefault();
    e.cancelBubble=true;
    e.returnValue=false;
    return false;
}

// on render, adjust select box height to allow buttons without adjustment
$("#unit-select").on("rendered.bs.select", function(e) {
    $('#unit-select-container').find('.dropdown-toggle').addClass('dropdown-tall-title')
});

// show custom unit buttons in unit select title box
$("#unit-select").on("refreshed.bs.select changed.bs.select", function(e, clickedIndex, newValue, oldValue) {
    placeholder = $(this).attr('title');
    title = $('#unit-select-container').find('.filter-option-inner-inner');
    unit_array = title.text().replace(placeholder,'').split(', ');
    unit_array = unit_array.filter(elem => elem);

    if(title.text() != placeholder){
        title.html('');
        for(i=0; i<unit_array.length; i++){
            title.append('<span id="unitpill'+i+'"class="btn btn-sm btn-dark dropdown-unit-pill">'+unit_array[i]+'<span id="unitdelete'+i+'" class="close-white" data-value="'+unit_array[i]+'">x</span></span>');
            document.getElementById("unitdelete"+i).addEventListener('click',deleteUnit)
            document.getElementById("unitpill"+i).addEventListener('click',pillUnit)
        }
    }
});

// remove unit when delete button in pill is clicked
function deleteUnit(e){
    e.stopPropagation()
    delete_name = $(this).attr('data-value');
    unit_array = $('#unit-select-container').find('.dropdown-toggle').attr('title').replace(delete_name,'').split(', ');
    unit_array = unit_array.filter(elem => elem);
    $('#unit-select').selectpicker('val', unit_array);
    $('#unit-select').selectpicker('refresh');
};
function pillUnit(e){
    e.stopPropagation()
};

// cookie function used for finding csrf token
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }
