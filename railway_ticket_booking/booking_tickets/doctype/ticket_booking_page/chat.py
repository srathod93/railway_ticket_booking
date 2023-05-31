import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the GPT model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Define the conversation loop
while True:
    # Prompt the user for input
    user_input = input('You: ')

    # Preprocess the user's input
    input_ids = tokenizer.encode(user_input, return_tensors='pt')

    # Generate a response
    response = model.generate(input_ids=input_ids, max_length=50, do_sample=True)

    # Convert the response to text
    response_text = tokenizer.decode(response[0], skip_special_tokens=True)

    # Display the response
    print('Chatbot:', response_text)
