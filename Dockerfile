FROM alpine:3.8

WORKDIR /app

# Update
RUN apk add --update python3

# Copy app files
COPY . /app

# Install
RUN python3 setup.py install

# Setup port
EXPOSE  50051

# Run
CMD invertedindexserer