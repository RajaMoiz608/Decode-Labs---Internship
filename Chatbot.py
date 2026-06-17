# NexusBot — Rule-Based AI Chatbot | DecodeLabs Project 1
# Author: Raja Moiz Khalid

from datetime import datetime

responses = {
    # Greetings
    "hello": None,
    "hi": None,
    "hey": None,
    "good morning": None,
    "good evening": None,
    "good afternoon": None,

    # Identity
    "what is your name": "I'm NexusBot — your rule-based AI assistant built by Raja Moiz Khalid.",
    "who are you": "I'm NexusBot, a deterministic AI chatbot. No hallucinations, just hard logic.",
    "who made you": "I was built by Raja Moiz Khalid as part of DecodeLabs AI Internship — Project 1.",
    "how are you": None,

    # AI & Tech Knowledge
    "what is ai": "AI stands for Artificial Intelligence — the simulation of human intelligence by machines using logic, rules, or learning algorithms.",
    "what is machine learning": "Machine Learning is a subset of AI where machines learn patterns from data instead of being explicitly programmed.",
    "what is deep learning": "Deep Learning uses neural networks with many layers to learn from massive amounts of data. It powers image recognition, ChatGPT, and more.",
    "what is a neural network": "A Neural Network is inspired by the human brain — it consists of layers of nodes that process inputs and produce outputs by adjusting weights.",
    "what is nlp": "NLP stands for Natural Language Processing — it allows machines to understand, interpret, and generate human language.",
    "what is python": "Python is a high-level, easy-to-read programming language widely used in AI, ML, data science, and web development.",
    "what is a chatbot": "A chatbot is a program that simulates human conversation. Rule-based bots use logic; AI bots use machine learning.",
    "what is the difference between ai and ml": "AI is the broad concept of machines being smart. ML is a technique used to achieve AI by learning from data.",
    "what is a large language model": "An LLM like GPT or Claude is trained on massive text data and generates human-like responses using probability — not hard rules like me!",
    "what is rule based ai": "Rule-based AI uses explicit if-else logic or dictionary lookups to respond. It's deterministic — same input always gives same output.",
    "what is a algorithm": "An algorithm is a step-by-step set of instructions to solve a problem. Every program you write is built on algorithms.",
    "what is data science": "Data Science combines statistics, programming, and domain knowledge to extract insights from data.",
    "what is oop": "OOP stands for Object-Oriented Programming — a paradigm based on objects and classes. Python, Java, and C++ support it.",

    # Python Specific
    "what is a dictionary in python": "A Python dictionary stores key-value pairs and allows O(1) lookups using hashing — exactly how I work!",
    "what is a list in python": "A Python list is an ordered, mutable collection of items. Example: my_list = [1, 2, 3]",
    "what is a loop in python": "Loops in Python repeat code. 'for' loops iterate over sequences; 'while' loops run until a condition is false.",

    # CS Fundamentals
    "what is a data structure": "A data structure organizes data for efficient access. Common ones: arrays, linked lists, stacks, queues, trees, graphs.",
    "what is a stack": "A stack follows LIFO — Last In, First Out. Think of a stack of plates. Used in undo/redo, function calls.",
    "what is a queue": "A queue follows FIFO — First In, First Out. Like a line at a counter. Used in scheduling and BFS.",
    "what is a binary tree": "A binary tree is a tree where each node has at most 2 children. BST (Binary Search Tree) keeps them sorted.",
    "what is big o notation": "Big O describes algorithm efficiency. O(1) is instant, O(n) scales linearly, O(n²) is slow. Always aim for O(1) or O(log n).",
    "what is recursion": "Recursion is when a function calls itself. It needs a base case to stop. Used in trees, graphs, and divide-and-conquer.",

    # Career & Motivation
    "how to become an ai engineer": "Study Python, math (linear algebra, stats), ML algorithms, and build projects. Consistency beats talent every time.",
    "what skills does an ai engineer need": "Python, ML frameworks (sklearn, TensorFlow, PyTorch), data handling (pandas, numpy), and strong problem-solving.",
    "is ai a good career": "Absolutely. AI engineering is one of the highest-demand and highest-paying fields globally right now.",
    "how to learn python fast": "Build projects from day one. Don't just read — code. Start small, stay consistent, and Google fearlessly.",
    "motivate me": None,

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "tell me another joke": "How many programmers does it take to change a light bulb? None — that's a hardware problem!",
    "what is the meaning of life": "42. At least that's what Douglas Adams said. In AI terms — it's the objective function you're optimizing for.",
    "are you smarter than chatgpt": "ChatGPT guesses. I'm certain. Different tools for different jobs — I never hallucinate.",

    # Date & Time — handled separately below
    "what time is it": None,
    "what is today's date": None,
    "what day is it": None,

    # Help & Exit
    "help": None,
}

GREETING_RESPONSE = None  # filled after name is collected
user_name = ""

def get_time_response():
    now = datetime.now()
    return f"Current time is {now.strftime('%I:%M %p')} and today is {now.strftime('%A, %B %d %Y')}."

def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        period = "Good Morning"
    elif hour < 17:
        period = "Good Afternoon"
    else:
        period = "Good Evening"
    return f"{period}, {user_name}! How can I help you today?"

def get_motivation():
    from random import choice
    quotes = [
        "The expert in anything was once a beginner. Keep going.",
        "Code is like humor. When you have to explain it, it's bad. Write clean code.",
        "Every large AI system started with someone writing their first if-else. Just like you.",
        "Push yourself, because no one else is going to do it for you.",
        "An AI engineer is just a problem-solver with Python installed.",
    ]
    return f"💡 {choice(quotes)}"

def get_help_message():
    return (
        f"\nHere's what I know, {user_name}:\n"
        "  • AI & ML concepts    → 'what is ai', 'what is machine learning'\n"
        "  • Deep Learning       → 'what is deep learning', 'what is a neural network'\n"
        "  • Python              → 'what is python', 'what is a dictionary in python'\n"
        "  • Data Structures     → 'what is a stack', 'what is big o notation'\n"
        "  • Career advice       → 'how to become an ai engineer', 'motivate me'\n"
        "  • Date & Time         → 'what time is it', 'what day is it'\n"
        "  • Fun                 → 'tell me a joke', 'are you smarter than chatgpt'\n"
        "  • Exit                → 'bye', 'exit', or 'quit'\n"
    )

def get_reply(clean_input):
    # Time & date
    if clean_input in ("what time is it", "what is today's date", "what day is it"):
        return get_time_response()

    # Greetings
    if clean_input in ("hello", "hi", "hey", "good morning", "good evening", "good afternoon"):
        return get_greeting()

    # How are you
    if clean_input == "how are you":
        return f"I'm running at 100% efficiency, {user_name}! No bugs detected. How about you?"

    # Motivation
    if clean_input == "motivate me":
        return get_motivation()

    # Help
    if clean_input == "help":
        return get_help_message()

    # Partial match — catches "hello there", "hey bot", etc.
    for key in responses:
        if key in clean_input:
            result = responses[key]
            if result:
                return result

    # O(1) exact dictionary lookup with fallback
    return responses.get(clean_input, f"I don't know that yet, {user_name}. Type 'help' to see what I can do!")


# ── Startup ──────────────────────────────────────────────────────────────────
print("\n" + "="*55)
print("        NEXUSBOT — Rule-Based AI Assistant")
print("        DecodeLabs AI Internship | Project 1")
print("="*55 + "\n")

user_name = input("NexusBot: Before we begin, what's your name? → ").strip().title()
if not user_name:
    user_name = "Friend"

print(f"\nNexusBot: Welcome aboard, {user_name}! I'm NexusBot.")
print(f"NexusBot: I know AI, ML, Python, Data Structures, and more.")
print(f"NexusBot: Type 'help' to explore or just start chatting!\n")

# ── Main Loop ─────────────────────────────────────────────────────────────────
while True:
    raw = input(f"{user_name}: ")
    clean = raw.lower().strip()

    if not clean:
        continue

    # Exit strategy
    if clean in ("bye", "exit", "quit"):
        print(f"\nNexusBot: Goodbye, {user_name}! Keep building. See you next session. 🚀\n")
        break

    reply = get_reply(clean)
    print(f"\nNexusBot: {reply}\n")