<?php
echo 'Change motion sensor state <br>';
echo '<form action="" method="post">';
echo '<input type="submit" name="btn1" value="ON">';
echo '<input type="submit" name="btn2" value="OFF">';
echo '</form>';


if ($_POST["btn1"] == "ON"){
    publish_message('on', 'paavo_cabin_motion_sensor', 'test.mosquitto.org', 1883, 60);
}
else if ($_POST["btn2"] == "OFF"){
	publish_message('off', 'paavo_cabin_motion_sensor', 'test.mosquitto.org', 1883, 60);
}
	
function publish_message($msg, $topic, $server, $port, $keepalive) {
	$client = new Mosquitto\Client();
	$client->onConnect('connect');
	$client->onDisconnect('disconnect');
	$client->onPublish('publish');
	$client->connect($server, $port, $keepalive);
	
	try {
		$client->loop();
		$mid = $client->publish($topic, $msg);
		$client->loop();
		}catch(Mosquitto\Exception $e){
				echo 'Exception';          
				return;
			}
    $client->disconnect();
    unset($client);					    
}

// Call back functions required for publish function
function connect($r) {
		if($r == 0) echo "{$r}-CONX-OK|";
		if($r == 1) echo "{$r}-Connection refused (unacceptable protocol version)|";
		if($r == 2) echo "{$r}-Connection refused (identifier rejected)|";
		if($r == 3) echo "{$r}-Connection refused (broker unavailable )|";        
}
 
function publish() {
        global $client;
        echo "Message published:";
}
 
function disconnect() {
        echo "Disconnected|";
}

?>