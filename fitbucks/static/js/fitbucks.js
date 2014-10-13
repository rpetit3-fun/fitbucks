/* -----------------------------------------------------------------------------
 * /daily-tasks/
 * ---------------------------------------------------------------------------*/
function init_datepicker() {
    var date = new Date();
    var today = date.getFullYear() + '-' +  (date.getMonth() + 1) + '-' + date.getDate();
    var previous_date = today;
    get_daily_stats(today);
    
    $('#datepicker').datepicker({
        format: 'yyyy-mm-dd',
        startDate: "2014-10-10",
        endDate: '0d'
    }).on('changeDate', function(e){
        var new_date = $('#datepicker').datepicker('getDate')
        if ( isNaN( new_date.getTime() ) ) {
            $('#datepicker').datepicker('setDate', previous_date);
        } else {
            new_date = new_date.getFullYear() + '-' +  (new_date.getMonth() + 1) + '-' + new_date.getDate()
            previous_date = new_date
            get_daily_stats(new_date);
        }
    });
    $('#datepicker').datepicker('setDate', today);  
};

function init_stats_form() {
    var frm = $('#save-daily-task');
    frm.submit(function () {
        $.ajax({
            type: 'POST',
            url: '/daily-tasks/',
            data: frm.serialize(),
            success: function (data) {
                console.log(data);
            },
            error: function(data) {
                console.log(data);
            }
        });
        return false;
    });
};


 
 function get_daily_stats(date) {
    $.ajax({ 
        type: 'POST',
        url: '/ajax/get_daily_stats/', 
        data: {'date':date},
        dataType: "json",
        success: function(data) { 
            var json = $.parseJSON(data);
            var field = json[0].fields
            $('#id_workout').val(field.workout);
            $('#id_planks').val(field.planks);
            $('#id_shinxes').val(field.sphinxes);
            $('#id_pushups').val(field.pushups);
            $('#id_situps').val(field.situps);
            $('#id_squats').val(field.squats);
            $('#id_date').val(date);
            
            if (field.steps == 0) {
                $('#id_steps').html("Total Steps: <em>Not Synced Yet</em>");
            } else {
                $('#id_steps').html("Total Steps: "+field.steps);
            }
        },
        error: function(error){
            if (error != 'DoesNotExist') {
                console.log("Error:");
                console.log(error);
            }
        }
    });
};
