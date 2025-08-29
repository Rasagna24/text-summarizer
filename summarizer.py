# Pre-processing the data
from transformers import BartForConditionalGeneration, BartTokenizer

# Load BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

while True:
    # Take user input
    input_text = input("\nEnter the text you want to summarize (or type 'exit' to quit):\n")
    
    if input_text.lower() == "exit":
        print("Exiting summarizer...")
        break
    
    # Tokenize and summarize
    inputs = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=150, early_stopping=True)

    # Decode and print the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print("\nOriginal Text:", input_text)
    print("Summary:", summary)
