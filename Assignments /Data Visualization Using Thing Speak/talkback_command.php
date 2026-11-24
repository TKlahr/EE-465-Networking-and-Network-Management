<?php

header("Content-Type: application/json");

$talkbackID = "58563";
$talkbackKey = "YOUR_TALKBACK_API_KEY";

$data = json_decode(file_get_contents("php://input"), true);
$command = $data["command"] ?? "";

if ($_SERVER["REQUEST_METHOD"] !== "POST" ||
    !in_array($command, ["ON", "OFF"], true)) {
    http_response_code(400);
    echo json_encode(["ok" => false]);
    exit;
}

$url = "https://api.thingspeak.com/talkbacks/"
       . $talkbackID . "/commands.json";

$params = http_build_query([
    "api_key" => $talkbackKey,
    "command_string" => $command
]);

$ch = curl_init($url);

curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 15);

$response = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

$result = json_decode($response ?: "", true);

if ($status >= 200 && $status < 300 &&
    isset($result["id"])) {
    echo json_encode([
        "ok" => true,
        "command" => $command
    ]);
} else {
    http_response_code(502);
    echo json_encode(["ok" => false]);
}

?>
