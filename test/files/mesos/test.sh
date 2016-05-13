gcc -o simple_app simple_app.c
curl -F "name=file" -F "filename=simple_app" -F "file=@simple_app" http://10.0.1.31:8080/v2/artifacts/binaries/simple_app
