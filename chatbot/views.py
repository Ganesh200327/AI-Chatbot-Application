from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from .models import Conversation
import torch

# Load AI model (run this once to cache the model)
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

def chat_view(request):
    return render(request, 'chatbot/chat.html')

def get_ai_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('message', '')
        
        # Generate response using AI
        chat_history_ids = None
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        
        # Generate response
        bot_output_ids = model.generate(
            new_user_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=100,
            top_p=0.7,
            temperature=0.8
        )
        
        response = tokenizer.decode(bot_output_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)
        
        # Save conversation to database
        Conversation.objects.create(
            user_input=user_input,
            bot_response=response
        )
        
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'})