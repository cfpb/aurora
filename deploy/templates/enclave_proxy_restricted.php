<!DOCTYPE html>

<html>
  <head>
    <title>CFPB Data Enclave - Restricted Area</title>
  
    <style>
      #header, #content {
        width: 960px;
        margin: 0 auto;
      }

      #header {
        text-align: center;
        margin-top: 1em;
      }

      #header img {
        margin: 0;
        padding: 0;
        margin-bottom: 1em;
      }

      #content {
        margin: 2em 1em;
      }
    </style>
  </head>

  <body>
    <div id="header">
      <img src="http://www.consumerfinance.gov/wp-content/themes/cfpb_nemo/_/img/logo.svg" />
      <h1>Welcome to the CFPB Data Enclave Restricted Area, <?php echo $_SERVER['REMOTE_USER']; ?>!</h1>
    </div>

    <div id="content">
      Restricted content found here!

      <?php
      foreach (getallheaders() as $name => $value) {
          echo "$name: $value\n";
      }
      ?>
    </div>
  </body>
</html>