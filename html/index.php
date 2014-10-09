<?php ?>
<html>
    <head>
        <!-- Bootstrap -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/css/datepicker3.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body>
        <!-- 10k steps, 50's 25 mins, 2min, bedtime -->
    <div class="container">
      <div class="page-header">
        <ul class="nav nav-pills pull-right">
          <li class="active"><a href="#">Home</a></li>
          <li><a href="/shannon/daily-tasks/">Daily Tasks</a></li>
          <li class="disabled"><a href="#">Quests</a></li>
          <li class="disabled"><a href="#">Missions</a></li>
          <li class="disabled"><a href="#">Rewards</a></li>
        </ul>
        <h2 class="text-muted">Bank of Fitness</h2>
      </div>

      <div class="row">
        <div class="col-lg-6">

        </div>

        <div class="col-lg-6">

        </div>
      </div>

      <div class="footer">
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