# SD12 Capstone: Comparative Analysis of Language Models for Game Script Generation
Explore the capabilities of leading LLMs in generating game scripts using Pygame that ensure game complexity (Features) and can run with no issues (Executable)

## Project Overview

This project aims to perform a comparative analysis of various large language models (LLMs) to determine which one performs best for generating game scripts in Python. The focus is on assessing the models based on accuracy to prompt, bug frequency, and completeness of the generated scripts. 

Read `Product Structure` for a review on how this project is organized so you can find everything easily.

Also, a base script written in GPT-4 is also under `/models` just for fun. Spoiler and shocker, it performed better than everything else.

## Language Models Used

- GPT-3.5 by OpenAI
- Claude Haiku by Anthropic
- Gemma 1.1 by Google

## Getting Started

### Prerequisites

- Create account with OpenAI for GPT 3.5.
- Create account with Anthropic for Claude Haiku.
- Create account with HuggingFace and request free access for Gemma 1.1.
- Python 3.11 or higher.
- Visual Studio Code or any preferred IDE for Python development.

### Setup

1. **Clone the Repository:**
```
git clone https://github.com/defford/Capstone_Project.git
cd Capstone Project
```
 
2. **Environment Setup:**
Ensure you have Python installed, and then set up a virtual environment:
```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```


## Project Structure

- `/models` - Contains folders for each LLM that was tested
- `/models/[LLM]/scripts` - Generated Python script from the parent folder model (Base, Feature, Execute)
- `/models/[LLM]/analysis` - Analysis reports for each prompt, covering a summary of it's performance, a list of features involved, and a bug report in case there were any.
- `/models/[LLM]/screenshots` - Screenshots of both the game play and game over screens for each program. Where some programs could not run, no game play screen was able to be captured. There is also no gme over screenshot if no game over screen was implemented in the code.

## Prompts

Each prompt was selected for minimal detail, but focused on the main intention of this project which is to generate code that is feature-full as well as executable. The inclusion of "Write only the code" is aimed to accomodate max output lengths in order to maximize code output.

### Base Prompt

`"write a snake game using pygame. Write only the code."`
- This prompts aims to be minimal and provides a use case for measuring the effects of single keywords.

### Feature Prompt

`"write a snake game using pygame that has a lot of features. Write only the code."`
- The addition of 'a lot' aims to prioritize an increase in the quantity of features (rather than focusing on quality of features, which could be considered in future analysis)

### Executable Prompt

`"write a snake game using pygame that contains no bugs in the script. Write only the code."`
- The addition of 'no bugs' aims to prioritize executable code, but bugs can be found in many places outside of the script (proper dependenies, environments, etc) and could cause the AI to make special considerations outside of simply generating code, so thats why 'in the script' is added to avoid these circumstances.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Authors

- **Daniel Efford** - *Initial work* - [defford](https://github.com/defford)
