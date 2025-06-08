import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../domain/chat_message.dart';

class ChatBubble extends StatelessWidget {
  final ChatMessage message;

  const ChatBubble({super.key, required this.message});

  @override
  Widget build(BuildContext context) {
    final isUser = message.sender == Sender.user;

    return Padding(
      padding: EdgeInsets.symmetric(
        horizontal: MediaQuery.of(context).size.width * 0.20, // 10% der Breite
        vertical: 5,
      ),
      child: Column(
        crossAxisAlignment: isUser ? CrossAxisAlignment.end : CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Bot-Icon (links)
              if (!isUser)
                CircleAvatar(
                  radius: 16,
                  backgroundColor: Colors.grey[300],
                  child: const Icon(Icons.rocket_rounded , color: Colors.black54),
                ),
              if (!isUser) const SizedBox(width: 8),

              // Chat-Bubble
              Flexible(
                child: Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: isUser ? Colors.blue[100] : Colors.grey[200],
                    borderRadius: BorderRadius.only(
                      topLeft: const Radius.circular(16),
                      topRight: const Radius.circular(16),
                      bottomLeft: Radius.circular(isUser ? 16 : 0),
                      bottomRight: Radius.circular(isUser ? 0 : 16),
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.05),
                        blurRadius: 4,
                        offset: const Offset(0, 2),
                      ),
                    ],
                  ),
                  child: (message.text.isEmpty && !isUser)
                      ? const _LoadingDots()
                      : Text(message.text),
                ),
              ),

              if (isUser) const SizedBox(width: 8),
              // User-Icon (rechts)
              if (isUser)
                CircleAvatar(
                  radius: 16,
                  backgroundColor: Colors.blue[300],
                  child: const Icon(Icons.person, color: Colors.white),
                ),
            ],
          ),
          // Copy button row
          Padding(
            padding: EdgeInsets.only(
              top: 4,
              left: isUser ? 0 : MediaQuery.of(context).size.width * 0.02,
              right: isUser ? MediaQuery.of(context).size.width * 0.02 : 0,
            ),
            child: Row(
              mainAxisAlignment: isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
              children: [
                if (!isUser)
                  IconButton(
                    icon: const Icon(Icons.copy, size: 20),
                    tooltip: 'Copy answer',
                    onPressed: () {
                      Clipboard.setData(ClipboardData(text: message.text));
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text('Answer copied to clipboard')),
                      );
                    },
                  ),
                if (isUser)
                  IconButton(
                    icon: const Icon(Icons.copy, size: 20),
                    tooltip: 'Copy question',
                    onPressed: () {
                      Clipboard.setData(ClipboardData(text: message.text));
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(content: Text('Question copied to clipboard')),
                      );
                    },
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _LoadingDots extends StatefulWidget {
  const _LoadingDots();

  @override
  State<_LoadingDots> createState() => _LoadingDotsState();
}

class _LoadingDotsState extends State<_LoadingDots> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<int> _dotCount;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 900),
      vsync: this,
    )..repeat();
    _dotCount = StepTween(begin: 1, end: 3).animate(
      CurvedAnimation(parent: _controller, curve: Curves.linear),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _dotCount,
      builder: (context, child) {
        final dots = '.' * _dotCount.value;
        return Text(
          dots,
          style: const TextStyle(fontSize: 20, color: Colors.black54, letterSpacing: 2),
        );
      },
    );
  }
}
