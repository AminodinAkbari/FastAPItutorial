from fastapi import FastAPI , Response , status , APIRouter , Cookie
from enum import Enum

blog_GET_router = APIRouter(prefix = '/blog' , tags=['blog'])
test_GET_router = APIRouter(prefix = '/test' , tags=['test'])
cookies 		= APIRouter(prefix = '/cookies' , tags=['Cookies'])

TEXT = "Test Text"

class BlogTypes(str , Enum):
	my_costum_type1 = "Custom1"
	my_costum_type2 = "Custom2"
	my_costum_type3 = "Custom3"

# @my_app.get('/blog/{id}/{type}')
# def blog_type(id , type:BlogTypes):
# 	return f"blog id is {id} and type is {type}"


#Test For Path Parametrs

	"""
	All Blogs Should be in Above the Detail Blog (Blog With ID)
	Also The Name of Defines Should Be Diffrent
	"""

@blog_GET_router.get('/all')
def blogs():
	return f"This is All Blogs"


@blog_GET_router.get('/{id}')
def blog(id):
	return f"Blog ID is {id}"
"""------------------------"""



# Testing status code
@test_GET_router.get('/test-status/{id}' , status_code=200 , tags=['test'])
def test_status(id:int , R:Response):
	if id > 5:
		R.status_code = status.HTTP_404_NOT_FOUND
		return f"Blog {id} Not Found"
	return "Blog {id} found"
#_________________________________________________


@test_GET_router.get("/test-path-parameters" , tags=['test'])
def test_path_parametrs(id:int=10 , test:str='Default'):
	return ["A" , "B"]


from fastapi.responses import HTMLResponse

@test_GET_router.get('/costum_response' , responses={
	404:{"content":{"text/html":{"Example" : "12"}},
	"description":"When Number Grater Than 10 , This Will Happend"},
	200:{"content":{"text/html":{"Example" : 5}}}
	})
def costum_response(num:int=0):
	if num >= 10:
		error = f"""
			<div>
				<h2> Not Valid : {num} </h2>
				<h5 style="color:red">your number should letter than 10</h5> 
			</div>
		"""
		return HTMLResponse(content=error , status_code=404)

	success = f"""
	<div>
		<h2 style="color:green"> Valid : {num} </h2>
	</div>
	"""

	return HTMLResponse(content=success , status_code=200)




""" ---- Cookies ----"""

# With This Function , Create a Cookie
@cookies.get('/')
def test_cookie():
	# test = Response(content=TEXT , media_type='text/plain')
	test = Response(content=TEXT , media_type='text/plain')
	test.set_cookie(key="Cookie2" , value="Value")
	return test


# With This Function See The Cookie We Created in Last Function !
@cookies.get('/see_cookie')
def see_cookie(Cookie2:str=Cookie(None)):
	return Cookie2

# ---------------------