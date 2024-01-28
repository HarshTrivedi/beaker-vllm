# To Start Beaker VLLM Server

1. Create docker and beaker images

```bash
# Do only once from this directory locally.
python build.py  # if beaker image already exists, delete it based on the error message.
```

2. Run the Server

```bash
ssh {username}@{hostname}.reviz.ai2.in # ssh into one of the cirrascale servers

git clone https://github.com/HarshTrivedi/beaker-vllm # if not already done.

python beaker-vllm/start.py {model_name} --num_gpus {num_gpus} --port {port}
```
