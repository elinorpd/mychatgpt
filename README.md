# mychatgpt

Simple code to simulate querying from GPT and recreating ChatGPT in your terminal.

## Steps
1. Get your own API key from openai.com and set it as an environment variable `OPENAI_API_KEY`
2. From the current directory, run `./askai.sh [--model MODEL] [--q QUERY] [--c chat mode]` where
  a. `--model` defaults to gpt-3.5-turbo
  b. `--q` is a query for the model OR
  c. `--c` flags interactive chat mode (to end, type exit or Ctrl+c)

## Setting up aliases
Here are example aliases to use in your terminal for easier use:
```
alias gpt4="<your_path>/mychatgpt/askai.sh --model gpt-4-1106-preview --q"
alias gpt3="<your_path>/mychatgpt/askai.sh --q"
alias chatgpt="<your_path>/mychatgpt/askai.sh --model gpt-4-1106-preview --c"
alias chatgpt3="<your_path>/mychatgpt/askai.sh --c"
```
(You may need to replace line 4 in `askai.sh` to the absolute path to the python script in order for this to work)
