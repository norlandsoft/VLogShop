import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse

app = FastAPI()

# 设置CORS策略，允许所有域名访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 将React应用的构建文件放在名为"frontend/dist"的目录中
app.mount("/", StaticFiles(directory="webui"), name="static")

# 定义一个中间件，将对根路径的请求重定向到index.html
class RedirectMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(request.url.path)
        if request.url.path == "/":
            return RedirectResponse(url="/index.html")
        return await call_next(request)

app.add_middleware(RedirectMiddleware)


if __name__ == "__main__":
    uvicorn.run("shop:app", host="0.0.0.0", port=6612, reload=True)