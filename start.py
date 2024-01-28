import argparse
import os
import subprocess
from textwrap import dedent


def main() -> None:
    parser = argparse.ArgumentParser(description="Start VLLM server on beaker.")
    parser.add_argument("model_name", type=str, help="model id/name")
    parser.add_argument(
        "--cache_dir",
        type=str,
        help="huggingface cache directory",
        default=None,
    )
    parser.add_argument(
        "--num_gpus",
        type=int,
        help="number of GPUs to use",
        default=1,
    )
    parser.add_argument(
        "--port",
        type=str,
        help="port to run server on",
        default=8000,
    )
    parser.add_argument(
        "--memory",
        type=int,
        help="GBs of memory to request",
        default=50,
    )
    parser.add_argument(
        "--username",
        type=str,
        help="beaker username",
        default="harsh-trivedi",
    )
    parser.add_argument(
        "--workspace",
        type=str,
        help="beaker workspace",
        default="ai2/toolgym",
    )
    parser.add_argument(
        "--image",
        type=str,
        help="docker image name",
        default="vllm-server",
    )
    args = parser.parse_args()

    if args.cache_dir is None:
        default_cache_dir_cirrascale = os.path.join(
            "/net", "nfs.cirrascale", "aristo", "vllm_server"
        )
        default_cache_dir_elanding = os.path.join("/net", "nfs2.aristo", "vllm_server")
        if os.path.exists(default_cache_dir_cirrascale):
            args.cache_dir = default_cache_dir_cirrascale
        elif os.path.exists(default_cache_dir_elanding):
            args.cache_dir = default_cache_dir_elanding

    command = dedent(
        f"""
    beaker session create \
        --image beaker://{args.username}/{args.image} \
        --workspace {args.workspace} --port {args.port}:{args.port} \
        --gpus {args.num_gpus} \
        --memory {args.memory}GiB \
        --env MODEL_NAME={args.model_name} \
        --env HF_HOME={args.cache_dir} \
        --env NUM_GPUS={args.num_gpus}
    """
    ).strip()
    print(f"Running: {command}")
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
