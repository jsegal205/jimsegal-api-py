# Jim Segal API

Endpoints to get data back for different parts of my site. Also a learning experience for playing with python.

## Running locally

`docker-compose up`

## Endpoints

### Games

#### List all games

`GET /games`

#### Response

```json
[
  {
    "title": "7 Wonders",
    "link": "https://boardgamegeek.com/boardgame/68448/7-wonders",
    "image": "https://cf.geekdo-images.com/thumb/img/Grz-qM9xwxlvQGK7B-MiljtO9pQ=/fit-in/200x150/pic860217.jpg"
  }
]
```
