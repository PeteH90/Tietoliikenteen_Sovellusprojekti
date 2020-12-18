<?php
$host='localhost';
$dbname='cabin_monitor';
$username='testi1';
$password='!Anturidata123';
$con = mysqli_connect($host,$username,$password,$dbname);
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
 }

$result = mysqli_query($con,"SELECT location, ti.temperature AS tempin, teo.temperature tempout, date_time FROM _events e 
JOIN temperature_inside ti ON e.id_temperature_inside=ti.id_temperature_inside JOIN temperature_outside teo ON e.id_temperature_outside=teo.id_temperature_outside 
JOIN raspberry r ON e.id_raspberry=r.id_raspberry WHERE location = 'Paavon Mökki' ORDER BY date_time DESC LIMIT 10");

$result2 = mysqli_query($con,"SELECT * FROM recent_message");

echo"<div style='border:1px solid green; border-radius: 5px; float:left; margin-left:14%; padding-top:10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;'>";
echo "Latest temperature readings and messages ";
echo "<br>";

echo "<table style='border:2px solid green;float:left;margin:10px'>
<tr>
<th>Location</th>
<th>Temperature Inside(°C)</th>
<th>Temperature Outside(°C)</th>
<th>Time</th>
</tr>";

foreach ($result as $row) {
  echo "<tr>";
  echo "<td>" . $row['location'] . "</td>";
  echo "<td>" . $row['tempin'] . "</td>";
  echo "<td>" . $row['tempout'] . "</td>";
  echo "<td>" . $row['date_time'] . "</td>";
  echo "</tr>";
}
echo "</table>";

 echo "<table style='border:2px solid green;float:left;margin:10px'>
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