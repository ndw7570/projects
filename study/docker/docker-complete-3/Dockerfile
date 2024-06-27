FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

# == 이 아래부터는 소스코드 대입, 시간 감많이 걸리는 install 부분은 이미 캐싱되었으므로 빠르게 넘어감 ==
COPY . .

EXPOSE 3000

CMD [ "node", "app.mjs" ]