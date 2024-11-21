from django.http import JsonResponse
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

def validation_error_response(errors):
    """
    Devuelve una respuesta JSON estándar para errores de validación.
    """
    return JsonResponse({
        "status": "error",
        "data": errors,
        "message": "Validation failed"
    }, status=status.HTTP_400_BAD_REQUEST)


def exception_response(exception):
    """
    Maneja excepciones genéricas y devuelve una respuesta JSON estándar.
    """
    return JsonResponse({
        "status": "error",
        "data": str(exception),
        "message": "An unexpected error occurred"
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def method_not_allowed_response(method):
    """
    Maneja métodos HTTP no permitidos.
    """
    return JsonResponse({
        "status": "error",
        "message": f"Method {method} not allowed on this endpoint"
    }, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def object_not_found_response(model_name):
    """
    Maneja errores cuando un objeto no se encuentra en la base de datos.
    """
    return JsonResponse({
        "status": "error",
        "message": f"{model_name} not found"
    }, status=status.HTTP_404_NOT_FOUND)