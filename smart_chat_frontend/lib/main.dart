import 'package:flutter/material.dart';
import 'features/chat/presentation/chat_screen.dart';

void main() {
  runApp(const SmartChatApp());
}

class SmartChatApp extends StatelessWidget {
  const SmartChatApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Smart Chat',
      theme: ThemeData.light(useMaterial3: true),
      home: const ChatScreen(),
    );
  }
}
