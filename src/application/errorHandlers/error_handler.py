from fastapi import Request
from fastapi.responses import JSONResponse

async def error_handler(request: Request, call_next):
    """Middleware para capturar e tratar erros da aplicação."""
    try:
        return await call_next(request)
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": "Erro na aplicação", "message": str(e)}
        )
