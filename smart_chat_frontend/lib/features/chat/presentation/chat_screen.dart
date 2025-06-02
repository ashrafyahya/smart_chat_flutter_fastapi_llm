import 'package:flutter/material.dart';

import '../data/chat_api.dart'; // <--- Importiere die neue API-Datei
import '../domain/chat_message.dart';
import 'widgets/chat_bubble.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final List<ChatMessage> _messages = [];
  final TextEditingController _controller = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  bool _isLoading = false; // Ladezustand

  void _sendMessage() async {
    final text = _controller.text.trim();
    if (text.isEmpty || _isLoading) return;

    setState(() {
      _messages.add(ChatMessage(text: text, sender: Sender.user));
      _isLoading = true;
      // Lade-Bubble anzeigen
      _messages.add(ChatMessage(text: '...', sender: Sender.bot));
    });

    _controller.clear();

    // Scrollen nach User-Message
    Future.delayed(const Duration(milliseconds: 100), () {
      _scrollController.animateTo(
        _scrollController.position.maxScrollExtent,
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeOut,
      );
    });

    // Verwende die neue API-Funktion
    final botReply = await ChatApi.fetchBotResponse(text);

    setState(() {
      // Lade-Bubble entfernen
      if (_messages.isNotEmpty && _messages.last.text == '...' && _messages.last.sender == Sender.bot) {
        _messages.removeLast();
      }
      // Bot-Antwort hinzufügen
      _messages.add(ChatMessage(text: botReply, sender: Sender.bot));
      _isLoading = false;
    });

    // Scrollen nach Bot-Message
    Future.delayed(const Duration(milliseconds: 100), () {
      _scrollController.animateTo(
        _scrollController.position.maxScrollExtent,
        duration: const Duration(milliseconds: 300),
        curve: Curves.easeOut,
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Smart Chat'),
        centerTitle: true,
        backgroundColor: Colors.blue[700],
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              controller: _scrollController,
              itemCount: _messages.length,
              itemBuilder: (context, index) =>
                  ChatBubble(message: _messages[index]),
            ),
          ),
          const Divider(height: 1),
          Container(
            color: Colors.white,
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    onSubmitted: (_) => _sendMessage(),
                    decoration: InputDecoration(
                      hintText: 'Nachricht eingeben...',
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                      contentPadding: const EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 10,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                IconButton(
                  icon: const Icon(Icons.send),
                  onPressed: _sendMessage,
                  color: Colors.blue[600],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
