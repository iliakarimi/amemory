# ShortMem Example and etc... :

This file contains detailed usage examples for `ShortMem`.


### the basic one:

```python
from amemory.shortmemory import ShortMem

# At first Instantiation the Class:

# m_delete default value's 2 && always_keep is 0
sm = ShortMem(m_delete=2, always_keep=1)

system_text = "You are a helpful assistant;"

# This message never delete in chat
# The first store message basicly use for system message and you should add value to always_keep to use it.
sm.store_messages(role="developer", messages=system_text)


sm.store_messages(role="user", message="hey")
sm.store_messages(role="assistant", message="Hey, How can I help you?")

sm.store_messages(role="user", message="tell me a joke")
sm.store_messages(role="assistant", message="You.")


print(sm.remind_messages())
```

**or**

### With OpenAI models:

```python
from openai import OpenAI
from amemory.shortmemory import ShortMem


sm = ShortMem(m_delete=2, always_keep=1)
client = OpenAI(api_key="...")

system_text = "You are Terry, A helpful assistant."

while True:
    user_input = str(input("User: "))
    sm.store_messages(role="user", messages=user_input)

    response = client.responses.create(
        model="gpt-6-astra",
        input=sm.remind_messages()
    )

    sm.store_messages(role="assistant", message=response.output_text)
    print(f"Assistant: {response.output_text}")
```


## add_rag_base(self, text:str = None):

For add **system-text** or **RAG-text** to model you can use **`add_rag_base()`** method.\
Here's an example:\
``` python
from amemory.shortmemory import ShortMem


sm = ShortMem(m_delete=2, always_keep=1)
client = OpenAI(api_key="...")


system_text = "You are Terry, A helpful assistant."

# add system_text to memory with add_rag_base
sm.add_rag_base(text=system_text)

while True:
    user_input = str(input("User: "))
    sm.store_messages(role="user", messages=user_input)

    response = client.responses.create(
        model="gpt-6-sol",
        input=sm.remind_messages()
    )

    sm.store_messages(role="assistant", message=response.output_text)
    print(f"Assistant: {response.output_text}")
    
```

```terminal
User: What's your name?

Assistant: I'm Terry, Your Helpful assistant.
```
<br />
<br />


## clear_messages(self):
This method just clear entire chat memory, but this method's not delete **system_text**.

Here's an example for `clear_messages`:\

```python
from amemory.shortmemory import ShortMem
import subprocess

sm = ShortMem(m_delete=2, always_keep=1)
client = OpenAI(api_key="...")


system_text = "You are Terry, A helpful assistant."

# add system_text to memory with add_rag_base
sm.add_rag_base(text=system_text)

while True:
    user_input = str(input("User: "))
    sm.store_messages(role="user", messages=user_input)

        if user_input == "/clear_chat":
            
            sm.clear_messages()
            subprocess.run(["clear"])

        else:
            response = client.responses.create(
                model="gpt-6-sol",
                input=sm.remind_messages()
            )

            sm.store_messages(role="assistant", message=response output_text)
            print(f"Assistant: {response.output_text}")
    
```

That's it.