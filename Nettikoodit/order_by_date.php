<?php
        $currentDateTime = date('Y-m-d H:i:s');
        $lastWeek = date('Y-m-d', strtotime('now - 7day'));
?>

<div style='border:1px solid green;border-radius: 5px;float:left;margin-left:22%;margin-bottom:10px;
  padding-top: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  padding-left: 10px;'>
<br>
<form id="order_by_date" action="" method="POST">
	Starting date(yyyy-mm-dd): <input type="text" name="sdate" value=<?php echo $lastWeek;?>>
	Ending date(yyyy-mm-dd): <input type="text" name="edate" value=<?php echo $currentDateTime;?>>
	<input type="submit">
</form>
<br>
</div>

<br>

<div style='border:1px solid green;border-radius: 5px;float:left;margin:10px;
  padding-top: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  padding-left: 10px;'>

<?php
	
	echo "Data from ";
	echo $_POST["sdate"];
	echo " to ";
	echo $_POST["edate"];

	$sdate = $_POST["sdate"];
	$edate = $_POST["edate"];

	$host='localhost';
	$dbname='cabin_monitor';
	$username='testi1';
	$password='!Anturidata123';
	$con = mysqli_connect($host,$username,$password,$dbname);
	if (mysqli_connect_errno()) {
	  echo "Failed to connect to MySQL: " . mysqli_connect_error();
	 }

	$result = mysqli_query($con,"SELECT location,ti.temperature AS tempin, teo.temperature AS tempout, hi.humidity AS humin, ho.humidity AS humout, pressure, date_time 
       FROM _events e JOIN temperature_inside ti ON e.id_temperature_inside=ti.id_temperature_inside JOIN temperature_outside teo ON e.id_temperature_outside=teo.id_temperature_outside 
       JOIN humidity_inside hi ON e.id_humidity_inside=hi.id_humidity_inside JOIN humidity_outside ho ON e.id_humidity_outside=ho.id_humidity_outside
       JOIN air_pressure a ON e.id_air_pressure=a.id_air_pressure JOIN raspberry r ON e.id_raspberry=r.id_raspberry WHERE location='Paavon Mökki' 
       AND date_time>='$sdate' AND date_time<='$edate'");

        $result2 = mysqli_query($con,"SELECT location, message,date_time FROM _events e JOIN message m ON e.id_message=m.id_message JOIN raspberry r ON e.id_raspberry=r.id_raspberry
        WHERE location='Paavon Mökki' AND date_time>='$sdate' AND date_time<='$edate' ORDER BY date_time DESC");

	echo "<br>";
	echo "<table style='border:2px solid green;float:left;margin:5px'>
	<tr>
	<th>Location</th>
	<th>Temperature Inside(°C)</th>
	<th>Temperature Outside(°C)</th>
	<th>Humidity Inside(%)</th>
	<th>Air Pressure(kPa)</th>
	<th>Time</th>
	</tr>";

	foreach ($result as $row) {
	    echo "<tr>";
	    echo "<td>" . $row['location'] . "</td>";
	    echo "<td>" . $row['tempin'] . "</td>";
	    echo "<td>" . $row['tempout'] . "</td>";
	    echo "<td>" . $row['humin'] . "</td>";
	    echo "<td>" . $row['pressure'] . "</td>";
	    echo "<td>" . $row['date_time'] . "</td>";
	    echo "</tr>";
	}
	echo "</table>";

        echo "<table style='border:2px solid green;float:left;margin:5px'>
       <tr>
       <th>Location</th>
       <th>Message</th>
       <th>Time</th>
       </tr>";

        foreach ($result2 as $row) {
            echo "<tr>";
            echo "<td>" . $row['location'] . "</td>";
            echo "<td>" . $row['message'] . "</td>";
            echo "<td>" . $row['date_time'] . "</td>";
            echo "</tr>";
       }
         echo "</table>";

        mysqli_close($con);
?>
</div>