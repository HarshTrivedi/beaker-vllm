# To Start Beaker VLLM Server

1. Create docker and beaker images

```bash
# Do only once from this directory locally.
python build.py --force
```

2. Run the Server

```bash
ssh {username}@{hostname}.reviz.ai2.in # ssh into one of the cirrascale servers

git clone https://github.com/HarshTrivedi/beaker-vllm # if not already done.

python beaker-vllm/start.py {model_name} --num_gpus {num_gpus} --port {port}
```


3. Temporary Note

The command to run TGI on beaker is:

```python
beaker session create --gpus=2 --image=docker://ghcr.io/huggingface/text-generation-inference:1.4 -- text-generation-launcher --json-output --model-id mosaicml/mpt-7b
```

The appropriate flags for port and volume need to be added. To be figured out when I get back to it.
