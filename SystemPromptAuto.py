import json
from openai import OpenAI

client = OpenAI(
  api_key='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',  # this is also the default, it can be omitted
)

def sendMessages(prompt, message):
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": "hey"},
        {"role": "assistant", "content": "hey, nice to meet you. What can I do for you today?"},
        {"role": "user", "content": message},
    ]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    response_message = response.choices[0].message.content
    return response_message

def sendMessages_long(prompt, message, conversation_number):
    messages = [{"role": "system", "content": prompt}]
    
    for _ in range(conversation_number):
        messages.append({"role": "user", "content": "hey"})
        messages.append({"role": "assistant", "content": "hello, nice to meet you. What can I do for you today?"})
    
    messages.append({"role": "user", "content": message})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    response_message = response.choices[0].message.content
    return response_message

#----------------------------------------------------------------------------
def send_email(sender, receiver):
    response = f'sending message from {sender} to {receiver}' 
    return response

functions = [
    {
        "name": "send_email",
        "description": "send email to a person",
        "parameters": {
            "type": "object",
            "properties": {
                "sender": {
                    "type": "string",
                    "description": "rmkkewec@gmail.com",
                },
                "receiver": {
                    "type": "string",
                    "description": "catchoco520@gmail.com",
                }
            },
            "required": ["sender", "receiver"],
        },
    }
]


def sendMessages_function(prompt, message, conversation_number):
    messages = [{"role": "system", "content": prompt}]
    
    for _ in range(conversation_number):
        messages.append({"role": "user", "content": "hey"})
        messages.append({"role": "assistant", "content": "hello, nice to meet you. What can I do for you today?"})
    
    messages.append({"role": "user", "content": message})
    
    response = client.chat.completions.create(
         model="gpt-3.5-turbo",
         messages=messages,
         functions=functions,
         function_call="auto",
     )
    
    first_response = response.choices[0].message.content
    
    first_response_dict = json.loads(first_response)
    if first_response_dict.get("function_call"):
        
        print("function call needed: ", first_response_dict["function_call"])
        available_functions = {
            "send_email": send_email,
        } 
        function_name = first_response_dict["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(first_response_dict["function_call"]["arguments"])
        function_response = fuction_to_call(
            query=function_args.get("query"),
        )
        return function_response 

    else:
        return first_response


prompt1 = "You are a helpful assistant. You are helping user whose email: rmkkewec@gmail.com"
prompt2 = "You are a helpful assistant. You are helping user: rmkkewec@gmail.com"
convo_num = 5
ans1 = sendMessages_function(prompt1, "what is my email", convo_num)
ans2 = sendMessages_function(prompt2, "what is my email", convo_num)
print(ans2)
print(ans2)
