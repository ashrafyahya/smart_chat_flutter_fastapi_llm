import 'dart:convert';
import 'dart:async';

import 'package:http/http.dart' as http;

class ChatApi {
  static const String baseUrl = 'http://localhost:8000';
  static const String generateEndpoint = '$baseUrl/generate';

  static Stream<String> fetchBotResponse(String prompt) async* {
    final client = http.Client();
    final request = http.Request('POST', Uri.parse(generateEndpoint));
    request.headers['Content-Type'] = 'application/json';
    request.body = jsonEncode({'prompt': prompt});

    final response = await client.send(request);

    if (response.statusCode == 200) {
      yield* response.stream.transform(utf8.decoder);
    } else {
      yield 'Fehler vom Server (${response.statusCode})';
    }
  }
}
