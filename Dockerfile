FROM nvcr.io/nvidia/pytorch:23.10-py3

RUN pip install vllm

ENV MODEL_NAME="facebook/opt-125m"
ENV HF_HOME="~/.cache/huggingface/"
ENV NUM_GPUS=1

ENTRYPOINT ["python", "entrypoint.py", $MODEL_NAME, "--hf_home", $HF_HOME, "--num_gpus", $NUM_GPUS]
