# A Memory

This is A memory for AI Agent/Assistant

> **Note:** This project is currently under active development and is not finalized. You should expect bugs, unstable behavior, and breaking changes. Use with caution in any critical environments.


## Key Features in A-Memory v0.1

* **Short Term Memory:** A Simple Short-Term-Memory for active chat with 8 message limit,
* **Job map:** A map for Agent to plan it's job,
* **Chat Goals:** This feature use to set goals and fact in active chat even short-term-memory removed old messages.


## Requirements

Before setting up the project, ensure you have the following installed:

* Python 3.14 or above...


## Installation

### Manual Instalation:
  ```bash
  git clone https://github.com/iliakarimi/a-memory.git
  cd a-memory
  ```


## Usage

### Quick Start

To import and use, run:

```python
from amemory.shortmemory import ShortMem, GoalsMem
from amemory.jobmap import jobmap

sm = ShortMem()
gm = GoalsMem()
```
with openai library:

```python
from openai import OpenAI

client = Openai(apikey="OPENAI_API_KEY")

sm.store_messages(role='user', message='whats 2+2')

response = client.responses.create(
    model="gpt-5.6",
    input=remind_messages(),
)

print(response.output_text)
```

## Contributing

Contributions are welcome to help improve this agent. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

Please ensure your code passes all linters and tests before submitting a PR.


## License

Distributed under the Apache-2.0 License. See `LICENSE` for more information.


## Contact

Ilia Karimi - iliakarimi.dev@gmail.com
