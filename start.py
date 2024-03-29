import argparse
import os
import subprocess
from textwrap import dedent


def main() -> None:
    parser = argparse.ArgumentParser(description="Start VLLM server on beaker.")
    parser.add_argument("model_name", type=str, help="model id/name")
    parser.add_argument(
        "--hf_home",
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

    if args.hf_home is None:
        is_on_cirrascale = os.path.exists(os.path.join("/net", "nfs.cirrascale"))
        is_on_elanding = os.path.exists(os.path.join("/net", "nfs2.aristo"))
        default_hf_home_cirrascale = os.path.join(
            "/net", "nfs.cirrascale", "aristo", "vllm_server"
        )
        default_hf_home_elanding = os.path.join("/net", "nfs2.aristo", "vllm_server")
        if is_on_cirrascale:
            args.hf_home = default_hf_home_cirrascale
        elif is_on_elanding:
            args.hf_home = default_hf_home_elanding

    command = dedent(
        f"""
    beaker session create \
        --image beaker://{args.username}/{args.image} \
        --workspace {args.workspace} --port {args.port}:{args.port} \
        --gpus {args.num_gpus} \
        --memory {args.memory}GiB \
        --shared-memory 15GiB \
        --env MODEL_NAME={args.model_name} \
        --env HF_HOME={args.hf_home} \
        --env NUM_GPUS={args.num_gpus}
    """
    ).strip()
    print(f"Running: {command}")
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
