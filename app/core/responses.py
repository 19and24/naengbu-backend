from typing import Any

from fastapi import HTTPException


def success(data: Any, message: str | None = None) -> dict[str, Any]:
    return {"success": True, "data": data, "message": message}


def api_error(status_code: int, message: str, error_code: str) -> HTTPException:
    return HTTPException(status_code=status_code, detail={
        "success": False,
        "data": None,
        "message": message,
        "errorCode": error_code,
    })


def pagination(items: list[Any], page: int, size: int, total: int) -> dict[str, Any]:
    return {
        "items": items,
        "page": page,
        "size": size,
        "totalElements": total,
        "totalPages": (total + size - 1) // size,
    }
