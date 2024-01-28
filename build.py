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

    args = parser.parse_args()

    command = f"docker build -t {args.username}/{args.image} ."
    print(f"Running: {command}")
    subprocess.run(command, shell=True)

    if args.force:
        command = f"beaker image delete {args.image}"
        print(f"Running: {command}")
        subprocess.run(command, shell=True)

    command = f"beaker image create {args.image} --name {args.image} --workspace {args.workspace}"
    print(f"Running: {command}")
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
