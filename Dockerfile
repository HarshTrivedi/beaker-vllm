FROM nvcr.io/nvidia/pytorch:23.10-py3

RUN pip install vllm

COPY chat_templates/ /workspace/chat_templates/
COPY entrypoint.py /workspace/entrypoint.py

ENV MODEL_NAME="facebook/opt-125m"
ENV HF_HOME="~/.cache/huggingface/"
ENV NUM_GPUS=1

ENTRYPOINT ["sh", "-c", "python /workspace/entrypoint.py $MODEL_NAME --hf_home $HF_HOME --num_gpus $NUM_GPUS"]
