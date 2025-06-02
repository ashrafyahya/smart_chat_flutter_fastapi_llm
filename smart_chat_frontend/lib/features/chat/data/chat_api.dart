import 'dart:convert';
import 'package:http/http.dart' as http;

class ChatApi {
  static const String baseUrl = 'http://localhost:8000';
  static const String generateEndpoint = '$baseUrl/generate';

  static Future<String> fetchBotResponse(String prompt) async {
    final response = await http.post(
      Uri.parse(generateEndpoint),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'prompt': prompt}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['response'] ?? response.body;
    } else {
      return 'Fehler vom Server (${response.statusCode})';
    }
  }
}
