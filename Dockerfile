FROM node:24-alpine AS build
RUN apk add --no-cache python3
WORKDIR /site
COPY package*.json ./
RUN npm ci
COPY . .
ENV ASTRO_TELEMETRY_DISABLED=1
RUN npm run build

FROM nginx:alpine
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /site/dist /srv/venture/current
