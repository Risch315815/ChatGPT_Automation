import asyncio
from ai_openchat import Model, AsyncOpenAI


API_KEY = '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'
client = AsyncOpenAI(token = API_KEY)

#-------------------------------------------------------
async def sendMessages(prompt, message):
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": "hey"},
        {"role": "assistant", "content": "hey, nice to meet you. What can I do for you today?"},
        {"role": "user", "content": message},
    ]
    
    response = await client.generate_message('Your request?', Model().chat())
    print(response)

prompt1 = "You are a helpful assistant. You are helping user whose email: rmkkewec@gmail.com"
if __name__ == "__main__":
    asyncio.run(sendMessages(prompt1, "what is my email"))
    # response_message = response.choices[0].message.content
    # return response_message

#-------------------------------------------------------
# prompt1 = "You are a helpful assistant. You are helping user whose email: rmkkewec@gmail.com"
# prompt2 = "You are a helpful assistant. You are helping user: rmkkewec@gmail.com"
# convo_num = 5
# ans1 = sendMessages(prompt1, "what is my email", convo_num)
# ans2 = sendMessages(prompt2, "what is my email", convo_num)
# print(ans1)
# print(ans2)