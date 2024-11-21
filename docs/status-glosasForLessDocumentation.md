# Status responses
- 200 OK: Respuesta exitosa en glosa_less_docs_list y glosa_less_docs_detail.
- 201 Created: Glosa creada exitosamente en glosa_less_docs_create.
- 204 No Content: Glosa eliminada exitosamente en glosa_less_docs_delete.
- 400 Bad Request: Datos inválidos en glosa_less_docs_create o glosa_less_docs_update.
- 404 Not Found: Glosa no encontrada (se maneja automáticamente con get_object_or_404).
- 405 Method Not Allowed: Método no permitido en las vistas glosa_less_docs_create, glosa_less_docs_update, y glosa_less_docs_delete.