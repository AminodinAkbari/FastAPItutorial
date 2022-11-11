from fastapi import FastAPI , Response , status
from router import router_get
from router import router_post
from fastapi.requests import Request
import time
from fastapi.middleware.cors import CORSMiddleware


my_app = FastAPI()
my_app.include_router(router_get.blog_GET_router)
my_app.include_router(router_get.test_GET_router)
my_app.include_router(router_get.cookies)
my_app.include_router(router_post.router)

origins = [
	'*'
]

my_app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*']
)

#the 'http' in right here , means : all requests sended to explorer , including this define
@my_app.middleware('http')
async def my_middleware(request:Request , call_next):
	print('Before Call')
	start_time = time.time()
	response = await call_next(request)
	duration = time.time() - start_time
	response.headers['duration'] = str(duration)
	print(response.headers['duration'])
	# print(f'header is {response.headers.duration}')
	print('Call Ended')
	return response


@my_app.get('/')
def index():
	return "Test Text"
