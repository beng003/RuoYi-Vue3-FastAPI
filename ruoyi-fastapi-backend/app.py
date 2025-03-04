# 导入UVicorn服务器库
import uvicorn
# 从server模块导入FastAPI实例(app)和应用配置(AppConfig)
from server import app, AppConfig  # noqa: F401

# 主程序入口
if __name__ == '__main__':
    # 启动UVicorn服务器
    uvicorn.run(
        app='app:app',                # 指定FastAPI实例位置（模块名:应用实例变量）
        host=AppConfig.app_host,      # 监听地址（0.0.0.0表示接受所有网络接口请求）
        port=AppConfig.app_port,       # 服务端口（默认9099）
        root_path=AppConfig.app_root_path,  # question:API根路径（与前端代理配置/dev-api对应）
        reload=AppConfig.app_reload,  # 开发模式热重载（代码修改自动重启）
    )
