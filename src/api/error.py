from fastapi import Request
from fastapi.responses import JSONResponse


async def error_request(request: Request, call_next):
    """Middleware para capturar e tratar erros da aplicação."""
    try:
        return await call_next(request)
    except ValueError as e:
        return JSONResponse(
            status_code=400,
            content={"detail": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )