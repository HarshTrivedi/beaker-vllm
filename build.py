import argparse
import subprocess


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build/update docker and beaker images for vllm server."
    )
    parser.add_argument(
        "--username",
        type=str,
        help="beaker username",
        default="harsh-trivedi",
    )
    parser.add_argument(
        "--image",
        type=str,
        help="docker image name",
        default="vllm-server",
    )
    parser.add_argument(
        "--workspace",
        type=str,
        help="beaker workspace",
        default="ai2/toolgym",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="delete image first",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="run docker build with --no-cache",
    )

    args = parser.parse_args()

    if args.no_cache:
        command = f"docker build --no-cache -t {args.image} ."
    else:
        command = f"docker build -t {args.image} ."
    print(f"Running: {command}")
    subprocess.run(command, shell=True)

    if args.force:
        command = f"beaker image delete {args.username}/{args.image}"
        print(f"Running: {command}")
        subprocess.run(command, shell=True)

    command = f"beaker image create {args.image} --name {args.image} --workspace {args.workspace}"
    print(f"Running: {command}")
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
