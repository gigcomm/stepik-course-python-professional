from collections import defaultdict


def best_sender(messages, senders):
    senders_counts = defaultdict(int)
    for message, sender in zip(messages, senders):
        senders_counts[sender] += len(message.split())

    return max(senders_counts.items(), key=lambda x: (x[1], x[0]))[0]


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
print(best_sender(messages, senders))
