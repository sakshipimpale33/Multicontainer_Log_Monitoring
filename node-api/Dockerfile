# Use Node.js official image
FROM node:18

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN npm install

# Expose port 4000
EXPOSE 4000

# Start Node.js server
CMD ["node", "server.js"]
