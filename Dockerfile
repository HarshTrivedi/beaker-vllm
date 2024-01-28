FROM nvcr.io/nvidia/pytorch:23.10-py3

RUN pip install vllm

ENV MODEL_NAME="facebook/opt-125m"
ENV HF_HOME="~/.cache/huggingface/"
ENV NUM_GPUS=1

ENTRYPOINT ["sh", "-c", "HF_HOME=$HF_HOME python -m vllm.entrypoints.openai.api_server --model $MODEL_NAME --tensor-parallel-size $NUM_GPUS"]
