from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = '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'
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature = 0.7, 
    ) 
    print(response)
    answer = response.choices[0].text
    return answer 
def chatbots(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message , 'response':response})
    return render(request , 'chatbot.html')
    