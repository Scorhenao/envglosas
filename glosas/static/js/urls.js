const BASE_URL = 'http://127.0.0.1:8000/api/' ;
export const GET_GLOSAS_LESS_DOCUMENTATION = `${BASE_URL}glosas/less_documentation/`;
export const GET_ONE_GLOSAS_LESS_DOCUMENTATION = `${BASE_URL}glosas/less_documentation/<int:pk>/`;
export const POST_GLOSAS_LESS_DOCUMENTATION = `${BASE_URL}glosas/less_documentation/add/`;
export const PUT_GLOSAS_LESS_DOCUMENTATION = `${BASE_URL}glosas/less_documentation/<int:pk>/update/`;
export const DELETE_GLOSAS_LESS_DOCUMENTATION = `${BASE_URL}glosas/less_documentation/<int:pk>/delete/`;