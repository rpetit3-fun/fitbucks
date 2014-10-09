<?php ?>
<html>
    <head>
        <!-- Bootstrap -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/css/datepicker3.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <style>
            .btn-primary {
                float: right !important;
            }
            .datepicker {
                padding: 0px !important;
            }
            .datepicker-days {
                background-image: linear-gradient(to bottom,#d9edf7 0,#b9def0 100%);
                background-repeat: repeat-x;
                border-color: #9acfea;
                border: 1px solid transparent;
                border-radius: 4px;
                color: #31708f;
                background-color: #d9edf7;
            }

        </style>
    </head>

    <body>
        <!-- 10k steps, 50's 25 mins, 2min, bedtime -->
        <div class="container">
            <div class="page-header">
                <ul class="nav nav-pills pull-right">
                    <li><a href="/shannon/">Home</a></li>
                    <li class="active"><a href="/shannon/daily-tasks/">Daily Tasks</a></li>
                    <li class="disabled"><a href="#">Quests</a></li>
                    <li class="disabled"><a href="#">Missions</a></li>
                    <li class="disabled"><a href="#">Rewards</a></li>
                </ul>
                <h2 class="text-muted">Bank of Fitness</h2>
            </div>


            <div class="row">
                <div class="col-sm-4">
                    <div id="datepicker" class="nav nav-sidebar"></div>
                </div>

                <div class="col-sm-8">
                    <div class="row">
                        <div class="text-center">
                            <h3>Log Your Daily Tasks</h3>
                            <hr/>
                        </div>
                    </div>
                    <div class="row">
                        <form role="form">
                            <div class="col-sm-6">
                                <div class="form-group">
                                    <label for="workout">Workout (Minutes)</label>  
                                    <input id="workout" name="workout" type="number" min="25" 
                                           value=25 class="form-control input-lg" required="">
                                </div>
                                <div class="form-group">
                                    <label for="planks">Planks (Seconds)</label>  
                                    <input id="planks" name="planks" type="number" min="60" 
                                           value=60 class="form-control input-lg" required="">
                                </div>
                                <div class="form-group">
                                    <label for="sphinxes">Sphinxes (Seconds)</label>  
                                    <input id="sphinxes" name="sphinxes" type="number" min="60" 
                                           value=60 class="form-control input-lg" required="">
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="form-group">
                                    <label for="pushups">Push Ups</label>  
                                    <input id="pushups" name="pushups" type="number" min="50" 
                                           value=50 class="form-control input-lg" required="">
                                </div>
                                <div class="form-group">
                                    <label for="situps">Sit Ups</label>  
                                    <input id="situps" name="situps" type="number" min="50" 
                                           value=50 class="form-control input-lg" required="">
                                </div>
                                <div class="form-group">
                                    <label for="squats">Squats</label>  
                                    <input id="squats" name="squats" type="number" min="50" 
                                           value=50 class="form-control input-lg" required="">
                                </div>
                                <button type="submit" class="btn btn-lg btn-primary">Save</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>

            <div class="footer text-center">
            <hr />
            <p>&copy; Bank Of Fitness 2014</p>
            </div>

        </div> <!-- /container -->

    
        <!-- Javascript -->
        <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/js/bootstrap-datepicker.min.js"></script>
        <script>
            var date = new Date();
            var today = (date.getMonth() + 1) + '/' + date.getDate() + '/' +  date.getFullYear();
            var cal = $('#datepicker').datepicker({
                format: 'mm/dd/yyyy',
                startDate: "10/06/2014",
                endDate: '0d'
            })
            $('#datepicker').datepicker('setDate', today);
        </script>
    </body>
</html>