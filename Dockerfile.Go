FROM golang:1.24-alpine

# Rest of your dockerfile remains the same
WORKDIR /app

# Install build dependencies
RUN apk add --no-cache git gcc musl-dev

# Copy go.mod and go.sum
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy source code
COPY . .

# Build the application
RUN go build -o whatsapp-bridge .

# Create directory for store
RUN mkdir -p store

# Run the application
CMD ["./whatsapp-bridge"]