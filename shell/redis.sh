# docker run --name redis \
# -p 6379:6379 \
# -v /disc1/docker-data/redis/redis.conf:/etc/redis/redis.conf \
# -v /disc1/docker-data/redis:/data \
# -d redis redis-server /etc/redis/redis.conf --appendonly yes


# docker run -d --name redis \
#   -p 6379:6379 \
#   -v /disc1/docker-data/redis/redis.conf:/etc/redis/redis.conf \
#   -v /disc1/docker-data/redis/data:/data \
#   --restart=always \
#   redis \
#   redis-server /etc/redis/redis.conf --appendonly yes

docker run -d --name redis -p 6379:6379 redis