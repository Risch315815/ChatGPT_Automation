import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('OPENAI_API_KEY', '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')
)


async def main():
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Mirror, mirror on the wall, who is the fairest of them all?"
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)


asyncio.run(main())