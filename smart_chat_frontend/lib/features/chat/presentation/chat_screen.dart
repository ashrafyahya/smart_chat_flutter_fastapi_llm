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
      // Lade-Bubble anzeigen (leerer Text, spezieller Ladezustand)
      _messages.add(ChatMessage(text: '', sender: Sender.bot));
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

    // Verwende die neue API-Funktion und fange mögliche Fehler ab
    var botReply;
    try {
      botReply = await ChatApi.fetchBotResponse(text);
    } catch (e) {
      print('Error fetching bot response: $e');
      botReply = 'Entschuldigung, es gab einen Fehler.';
    }

    setState(() {
      // Lade-Bubble entfernen
      if (_messages.isNotEmpty && _messages.last.text == '' && _messages.last.sender == Sender.bot && _isLoading) {
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
        backgroundColor: const Color.fromARGB(255, 48, 139, 230),
      ),
      body: Column(
        children: [
          Expanded(
            child: _messages.isEmpty
                ? const Center(
                    child: Text(
                      'Welcome to the smart chat',
                      style: TextStyle(fontSize: 18, color: Colors.grey),
                    ),
                  )
                : Row(
                    children: [
                      Expanded(
                        child: ListView.builder(
                          controller: _scrollController,
                          itemCount: _messages.length,
                          itemBuilder: (context, index) =>
                              ChatBubble(message: _messages[index]),
                        ),
                      ),
                      IconButton(
                        icon: const Icon(Icons.delete),
                        color: Colors.blueAccent,
                        tooltip: 'Clear Chat',
                        onPressed: () {
                          setState(() {
                            _messages.clear();
                          });
                        },
                      ),
                    ],
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
