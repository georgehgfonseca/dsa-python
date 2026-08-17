# How to run an LLM locally with llama.cpp

git clone https://github.com/ggml-org/llama.cpp.git

sudo apt-get install nvidia-cuda-toolkit

sudo apt-get install ninja-build cmake libcurl4-openssl-dev

cmake -B build -DLLAMA_CURL=ON -DGGML_CUDA=ON -DGGML_CCACHE=OFF -G Ninja

cd build

ninja


It is expected to rbeak, see: https://github.com/NVIDIA/apex/issues/1491

ninja

## Running

./bin/llama-server -hf bartowski/Llama-3.2-3B-Instruct-GGUF
-OR-
./bin/llama-server     -hf bartowski/Llama-3.2-3B-Instruct-GGUF     --jinja -fa    --host 0.0.0.0     --port 8080   --threads 14     --threads-batch 28     --parallel 4     --cont-batching     --n-gpu-layers 100     --tensor-split 100

## Using it

Open it on localhost:8080

How to use it as an API:
https://github.com/ggml-org/llama.cpp/blob/master/examples/server/README.md#post-v1chatcompletions-openai-compatible-chat-completions-api

Source:

import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required"
)

prompt = """
What is Ash's main Pokemon?
"""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)

# Run gemma (multimodal model):
export HF_TOKEN="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"
cd build/bin
 wget https://github.com/bebechien/gemma/blob/main/surprise.png?raw=true -O ~/Downloads/surprise.png
./llama-gemma3-cli -hf google/gemma-3-4b-it-qat-q4_0-gguf -p "Describe this image." --image ~/Downloads/surprise.png