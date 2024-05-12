FROM node:21-bullseye-slim as base

ARG PORT=3000

ENV NODE_ENV=production

WORKDIR /src

# Build
FROM base as build

COPY --link ./kitchenView-frontend/package.json ./kitchenView-frontend/package-lock.json ./
RUN npm install --production=false

COPY --link ./kitchenView-frontend .

RUN npm run build
RUN npm prune

# Run
FROM base

ENV PORT=$PORT

COPY --from=build /src/.output /src/.output

CMD [ "node", ".output/server/index.mjs" ]