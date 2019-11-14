# Ex 8_10 Messages

def show_texts(texts):
    """Display each message from the list"""
    for text in texts:
        print(f"Today's moto is: {text.title()}!")

texts = ['you can do it', 'good job', 'rise like a star', 'the more, the better']
show_texts(texts)


# Ex 8_10 Sending messages

# Define function with two parameters to print message.

print("\n")
def send_message(texts, sent_texts):
    while texts:
        current_text = texts.pop()
        print(f"Sending message: {current_text.title()}.")
        sent_texts.append(current_text)

#Define function with one parameter to display the summary.

def show_summary(sent_texts):
    """Display all sent messages in the list"""
    print("\nThe following texts have been sent:")
    for sent_text in sent_texts:
        print(f"{sent_text.title()}!")

texts = ['you can do it', 'good job', 'rise like a star', 'the more, the better']
sent_texts = []

send_message(texts, sent_texts)
show_summary(sent_texts)


# Ex 8_11 Archived messages

# Define function with two parameters to print message.

print("\n")
def send_message_1(texts, sent_texts):
    while texts:
        current_text = texts.pop()
        print(f"Sending message: {current_text.title()}.")
        sent_texts.append(current_text)

#Define function with one parameter to display the summary.

def show_summary_1(sent_texts):
    """Display all sent messages in the list"""
    print("\nThe following texts have been sent:")
    for sent_text in sent_texts:
        print(f"{sent_text.title()}!")

def show_source(texts, sent_texts):
    """Display the original list with texts and newly created list with sent texts"""
    print("\n")
    print(texts)
    print(sent_texts)

texts = ['you can do it', 'good job', 'rise like a star', 'the more, the better']
sent_texts = []

send_message_1(texts[:], sent_texts)
show_summary_1(sent_texts)
show_source(texts, sent_texts)