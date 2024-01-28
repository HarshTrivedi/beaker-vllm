FROM nvcr.io/nvidia/pytorch:23.10-py3

RUN pip install vllm

COPY chat_templates chat_templates
COPY entrypoint.py entrypoint.py

ENV MODEL_NAME="facebook/opt-125m"
ENV HF_HOME="~/.cache/huggingface/"
ENV NUM_GPUS=1

# ENTRYPOINT ["sh", "-c", "HF_HOME=$HF_HOME python -m vllm.entrypoints.openai.api_server --model $MODEL_NAME --tensor-parallel-size $NUM_GPUS --chat-template chat_templates/template_chatml.jinja2"]
ENTRYPOINT ["sh", "-c", "python entrypoint.py $MODEL_NAME --hf_home $HF_HOME --num_gpus $NUM_GPUS"]
