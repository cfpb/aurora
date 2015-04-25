<!DOCTYPE html>

<html>
	<head>
		<title>CFPB Data Enclave</title>
	
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
		  <h1>Welcome to the CFPB Data Enclave, <?php echo $_SERVER['REMOTE_USER']; ?>!</h1>
    </div>

    <div id="content">
      <?php
        echo "<hr />";
        foreach($_SERVER as $key_name => $key_value) {
          print $key_name . " = " . $key_value . "<br />";
        }

        echo "<hr />";

        // AD server
        $ldaphost = "{{ kdc_domain_name }}";
        $ldapport = 389;

        $tab = explode('@', $_SERVER['REMOTE_USER']);
        $person = $tab[0];
        $domain = $tab[1];

        $ldapconn = ldap_connect($ldaphost, $ldapport);

        echo "<p>";
        echo "LDAP Connection: ";
        echo $ldapconn;
        echo "<br />";
        echo "LDAP Group(s): ";
        echo $_SERVER['AUTHENTICATE_MEMBEROF'];
        echo "</p>";
        //or die("Unable to connect to the LDAP server {$ldaphost}" );
      ?>
    </div>
  </body>
</html>