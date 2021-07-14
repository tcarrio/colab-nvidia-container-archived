# Container image of Colaboratory local runtime

## Install and Run

In order to build and run the image:

```
docker build -t colab-nvidia -f Containerfile .

docker run --runtime=nvidia -it --rm -p 8081:8081 --cap-add SYS_ADMIN --device /dev/fuse \
           --security-opt apparmor=unconfined colab-nvidia
```

## License

This repository is forked from
https://github.com/googlecolab/backend-container/blob/bcbbf44/containers/Dockerfile

The original license can be found in the [LICENSE file](./LICENSE).
