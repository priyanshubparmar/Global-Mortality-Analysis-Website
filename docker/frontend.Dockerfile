FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY frontend/package*.json ./

RUN npm install

# Copy ALL frontend code
COPY frontend .

# Build React app
RUN npm run build

# Install serve
RUN npm install -g serve

EXPOSE 3000

# 🔥 IMPORTANT: specify build folder
CMD ["serve", "-s", "dist", "-l", "3000"]