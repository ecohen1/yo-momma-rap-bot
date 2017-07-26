function generateRap() {
    $.get( "/rap", function( rap_string ) {
        $('#rap').html(rap_string)        
    });
}
