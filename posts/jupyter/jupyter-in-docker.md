# 在 docker 中运行 jupyter，并在本机上打开网页

 - docker run
 ```
 docker run -it -p 7000:7000 --rm --name test docker_image_id
 ```
 - docker 启动 jupyter notebook
 ```
 jupyter-notebook --no-browser --ip 0.0.0.0 --port=7000 --allow-root
 ```
 - 打开网址 http://localhost:7000/tree
 - 填写 token
 如，
 ```
 http://(e4a1a7bc8829 or 127.0.0.1):7000/?token=609cbbee2c5feed5a2d3065c7846d6501c43ba35cd7828a4
 ```
 指定

# 参考
在 docker 中指定运行 ip 为 `0.0.0.0` https://stackoverflow.com/a/38936551/4647978

