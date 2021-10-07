docker build -t predict:0.1 .

docker run --env X_PREDICT='2 0 0 10.5 31 0 1 0 0 1' predict:0.1
