import argparse
import os
import subprocess


file_directory = os.path.dirname(os.path.abspath(__file__))
MODEL_NAME_TO_CHAT_TEMPLATE = {
    "OpenLemur/lemur-70b-chat-v1": os.path.join(file_directory, "chat_templates", "template_chatml.jinja"),
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Entry point for docker run to start the vllm server.")
    parser.add_argument("model_name", type=str, help="model id/name")
    parser.add_argument(
        "--hf_home",
        type=str,
        help="huggingface cache directory",
        default="~/.cache/huggingface/",
    )
    parser.add_argument(
        "--num_gpus",
        type=int,
        help="number of GPUs to use",
        default=1,
    )
    args = parser.parse_args()

    command = (
        f"HF_HOME={args.hf_home} python -m vllm.entrypoints.openai.api_server "
        f"--model {args.model_name} --tensor-parallel-size {args.num_gpus}"
    )
    chat_template = MODEL_NAME_TO_CHAT_TEMPLATE.get(args.model_name, None)
    if chat_template is not None: # Disable temporarily.
        assert os.path.exists(chat_template), f"Chat template {chat_template} does not exist."
        command += f" --chat-template {chat_template}"

    print(f"Running: {command}")
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
