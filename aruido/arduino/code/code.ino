#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <ESPmDNS.h>

const char* ssid     = "";
const char* password = "";

WebServer server(80);

String GenerateMetrics() {
  String message = "";

  message += "# HELP pv_switch_free_memory Free Memory to monitor RAM health";
  message += "\n";
  message += "# TYPE pv_switch_free_memory gauge";
  message += "\n";
  message += "pv_switch_free_memory ";
  message += ESP.getFreeHeap();
  message += "\n";
    
  return message;
}

void handleRoot() {
  server.send(200, "text/plain", "metrics at /metrics");
}

void handleMetrics() {
  server.send(200, "text/plain", GenerateMetrics());
}

void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);  
}

void setup(void) {
  Serial.begin(115200);  
  Serial.println("Begin Setup");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println(WiFi.status());
  Serial.println(WL_CONNECTED);
  Serial.println(WL_NO_SHIELD);
  Serial.println(WL_IDLE_STATUS);
  Serial.println(WL_NO_SSID_AVAIL);
  Serial.println(WL_SCAN_COMPLETED);
  Serial.println(WL_CONNECT_FAILED);
  Serial.println(WL_CONNECTION_LOST);
  Serial.println(WL_DISCONNECTED);

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(5000);
    Serial.println(WiFi.status());
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp32")) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);

  server.on("/metrics", handleMetrics);

  server.on("/inline", []() {
    server.send(200, "text/plain", "this works as well");
  });

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  server.handleClient();
}
