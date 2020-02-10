import graphene as gp
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from databases import Database

database = Database('postgresql://db:5432', user='postgres', password='test')

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

class Places(gp.ObjectType):
    async_places = gp.String(description='places', start_date=gp.DateTime(), end_date=gp.DateTime())

    async def resolve_async_places(self, info, start_date, end_date):
        print(start_date)
        print(end_date)
        rows = await database.fetch_all(query='''SELECT * FROM places where last_review >= :start_date AND last_review < :end_date''' )
        print(rows)
        return "xd"




app.add_route("/", GraphQLApp(schema=gp.Schema(query=Places)))
