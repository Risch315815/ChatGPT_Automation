from openai import OpenAI

API_KEY = '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'
client = OpenAI(api_key = API_KEY)

def sendMessages(Prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=Prompt,
        temperature=0
    )
    response_message = response.choices[0].message.content
    return response_message

def Messages(Premise, Order):
    messages = [
    {"role": "system", "content": Premise},
    {"role": "user", "content": "hey"},
    {"role": "assistant", "content": "hey, nice to meet you. What can I do for you today?"},
    {"role": "user", "content": Order},
    ]
    return messages

#-------------------------------------------------------
premise00 = "You are a professional zoologist. You job is to answer all of the questions regarding names of species using 'Binomial nomenclature' and nothing else."
order00 = "Please list 5 random animals in the form of [a, b, c, d, e]. Please just list the names of the animals, and nothing else. Do not use bullet or numeric or alphabetics, and do not include introduction. "
order01 = "Please make a list of 5 animals most closely related to each of the animals in the list in the form of [a, b, c, d, e]. Please just append the names of the animals behind the names of the animals in the original list, and nothing else. Do not use bullet or numeric or alphabetics, and do not include introduction."
ans1 = sendMessages(Messages(premise00, order00))
sequ = [0]
sequ[0] = ans1
print(ans1)
for i in (0, 1, 2):
    ansx = sendMessages(Messages(sequ[i], order01))
    sequ.append(ansx)
print(sequ[2])

