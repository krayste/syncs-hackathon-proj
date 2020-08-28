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
