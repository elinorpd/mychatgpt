import openai
import os
import argparse

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

def query(args):
    response = openai.ChatCompletion.create(
                    model=args.model,
                    messages=[
                        # {"role": "system", "content": "You are an expert in AI literacy and middle school education. We will give you an existing lesson plan from a middle school teacher. For each component of the plan, it will indicate whether or not you should edit that section. For any activities that have 'editable: True', please modify or replace the activity with an engaging, safe, and time-appropriate AI literacy activity relevant to the lesson. Do not change any components with 'editable: False'. For other editable sections, modify if you think it is necessary to incorporate AI Literacy learning objectives and maintain coherence.\n\nReturn only the lesson plan in the same format, with your edits to the editable sections with no additional text or references to your edits. Don't include the (editable: value) statements."},
                        {"role": "user", "content": args.q },
                    ],
                    )

    return response["choices"][0]["message"]["content"]

def chat(messages, args):
    response = openai.ChatCompletion.create(
                    model=args.model,
                    messages=messages,
                    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--q', type=str, default=None, help='query to ask the AI')
    # add flag for chat mode
    argparse.add_argument('--c', action='store_true', help='chat mode')
    argparse.add_argument('--model', type=str, default='gpt-3.5-turbo', help='openai model to use, default "gpt-3.5-turbo" or use "gpt-4-1106-preview"')
    args = argparse.parse_args()
    
    
    if args.c:
        messages = []
        while True:
            inp = input("You: ")
            if inp == "exit":
                break
            messages.append({"role": "user", "content": inp})
            response = chat(messages,args)
            print("AI: " + response)
            messages.append({"role": "assistant", "content": response})
    elif args.q:
        response = query(args)
        print(response)
    
